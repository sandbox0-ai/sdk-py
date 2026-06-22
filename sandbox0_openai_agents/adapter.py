from __future__ import annotations

import asyncio
import io
import json
import os
import time
import uuid
from pathlib import Path
from typing import Any, Dict, Literal, Optional, Sequence, Tuple, Union, cast

from agents.sandbox.errors import (
    ExecTimeoutError,
    ExecTransportError,
    SandboxError,
    WorkspaceArchiveReadError,
    WorkspaceArchiveWriteError,
    WorkspaceReadNotFoundError,
    WorkspaceStartError,
    WorkspaceStopError,
)
from agents.sandbox.manifest import Manifest
from agents.sandbox.session import (
    BaseSandboxClient,
    BaseSandboxClientOptions,
    BaseSandboxSession,
    SandboxSession,
    SandboxSessionState,
)
from agents.sandbox.session.workspace_payloads import coerce_write_payload
from agents.sandbox.snapshot import SnapshotBase, SnapshotSpec, resolve_snapshot
from agents.sandbox.types import ExecResult, User

from sandbox0.apispec.models.claim_mount_request import ClaimMountRequest
from sandbox0.apispec.models.create_cmd_context_request import CreateCMDContextRequest
from sandbox0.apispec.models.create_context_request import CreateContextRequest
from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest
from sandbox0.apispec.models.create_snapshot_request import CreateSnapshotRequest
from sandbox0.apispec.models.process_type import ProcessType
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_lifecycle_status import SandboxLifecycleStatus
from sandbox0.apispec.types import UNSET
from sandbox0.client import DEFAULT_BASE_URL, Client as Sandbox0Client
from sandbox0.errors import APIError
from sandbox0.sandbox import Sandbox

BACKEND_ID = "sandbox0"
DEFAULT_TEMPLATE = "default"
DEFAULT_WORKSPACE = "/workspace"
DEFAULT_POLL_INTERVAL_SEC = 0.1
DEFAULT_START_TIMEOUT_SEC = 60.0
SANDBOX0_WORKSPACE_REFERENCE_TYPE = "sandbox0_volume_reference"


class Sandbox0SandboxClientOptions(BaseSandboxClientOptions):
    """Options for creating OpenAI Agents SDK sessions backed by Sandbox0."""

    type: Literal["sandbox0"] = "sandbox0"
    template: str = DEFAULT_TEMPLATE
    workspace_mount_path: str = DEFAULT_WORKSPACE
    volume_id: Optional[str] = None
    volume_snapshot_id: Optional[str] = None
    sandbox_ttl_sec: Optional[int] = None
    delete_sandbox_on_delete: bool = True
    delete_volume_on_delete: bool = True
    create_volume_snapshot_on_stop: bool = True
    exposed_ports: Tuple[int, ...] = ()
    poll_interval_sec: float = DEFAULT_POLL_INTERVAL_SEC
    start_timeout_sec: float = DEFAULT_START_TIMEOUT_SEC
    default_posix_uid: int = 0
    default_posix_gid: int = 0


class Sandbox0SandboxSessionState(SandboxSessionState):
    """Serialized state needed to resume an OpenAI Agents SDK Sandbox0 session."""

    type: Literal["sandbox0"] = "sandbox0"
    sandbox_id: Optional[str] = None
    volume_id: str
    volume_snapshot_id: Optional[str] = None
    template: str = DEFAULT_TEMPLATE
    workspace_mount_path: str = DEFAULT_WORKSPACE
    sandbox_ttl_sec: Optional[int] = None
    delete_sandbox_on_delete: bool = True
    delete_volume_on_delete: bool = True
    create_volume_snapshot_on_stop: bool = True
    poll_interval_sec: float = DEFAULT_POLL_INTERVAL_SEC
    start_timeout_sec: float = DEFAULT_START_TIMEOUT_SEC
    volume_workspace_ready: bool = False
    replacement_count: int = 0


class Sandbox0SandboxSession(BaseSandboxSession):
    """OpenAI Agents SDK sandbox session backed by a Sandbox0 sandbox and volume."""

    state: Sandbox0SandboxSessionState

    def __init__(
        self,
        *,
        state: Sandbox0SandboxSessionState,
        client: Sandbox0Client,
    ) -> None:
        self.state = state
        self._client = client
        self._sandbox: Optional[Sandbox] = (
            Sandbox(id=state.sandbox_id, client=client, template=state.template)
            if state.sandbox_id
            else None
        )

    @classmethod
    def from_state(
        cls,
        *,
        state: Sandbox0SandboxSessionState,
        client: Sandbox0Client,
    ) -> "Sandbox0SandboxSession":
        return cls(state=state, client=client)

    async def _ensure_backend_started(self) -> None:
        if self.state.sandbox_id:
            sandbox = await self._try_reconnect_sandbox(self.state.sandbox_id)
            if sandbox is not None:
                self._sandbox = sandbox
                self._set_start_state_preserved(self.state.volume_workspace_ready, system=True)
                return

        sandbox = await self._claim_replacement_sandbox()
        self._sandbox = sandbox
        self.state.sandbox_id = sandbox.id
        self.state.replacement_count += 1
        self._set_start_state_preserved(self.state.volume_workspace_ready, system=True)

    async def _prepare_backend_workspace(self) -> None:
        result = await self.exec("mkdir", "-p", self.state.workspace_mount_path, shell=False)
        if not result.ok():
            raise WorkspaceStartError(
                path=Path(self.state.workspace_mount_path),
                context={
                    "stdout": result.stdout.decode("utf-8", errors="replace"),
                    "stderr": result.stderr.decode("utf-8", errors="replace"),
                    "exit_code": result.exit_code,
                },
            )

    async def _after_start(self) -> None:
        self.state.volume_workspace_ready = True

    def _wrap_start_error(self, error: Exception) -> Exception:
        if isinstance(error, SandboxError):
            return error
        return WorkspaceStartError(path=Path(self.state.workspace_mount_path), cause=error)

    def _wrap_stop_error(self, error: Exception) -> Exception:
        if isinstance(error, SandboxError):
            return error
        return WorkspaceStopError(path=Path(self.state.workspace_mount_path), cause=error)

    async def _exec_internal(
        self,
        *command: Union[str, Path],
        timeout: Optional[float] = None,
    ) -> ExecResult:
        sandbox = self._require_sandbox(command)
        request = CreateContextRequest(
            type_=ProcessType.CMD,
            cmd=CreateCMDContextRequest(command=[str(arg) for arg in command]),
            wait_until_done=False,
            cwd=self.state.workspace_mount_path,
        )

        try:
            context = await asyncio.to_thread(sandbox.create_context, request=request)
        except Exception as exc:
            raise ExecTransportError(command=command, cause=exc) from exc

        context_id = context.id
        deadline = None if timeout is None else time.monotonic() + timeout
        context_deleted = False
        try:
            while True:
                current = await asyncio.to_thread(sandbox.get_context, context_id=context_id)
                exit_code = _optional_int(getattr(current, "exit_code", UNSET))
                running = bool(getattr(current, "running", False))
                if not running or exit_code is not None:
                    return ExecResult(
                        stdout=_optional_text(getattr(current, "stdout", UNSET)).encode(),
                        stderr=_optional_text(getattr(current, "stderr", UNSET)).encode(),
                        exit_code=0 if exit_code is None else exit_code,
                    )

                if deadline is not None and time.monotonic() >= deadline:
                    await self._delete_context_best_effort(sandbox, context_id)
                    context_deleted = True
                    raise ExecTimeoutError(command=command, timeout_s=timeout)

                await asyncio.sleep(max(self.state.poll_interval_sec, 0.01))
        except ExecTimeoutError:
            raise
        except Exception as exc:
            raise ExecTransportError(command=command, cause=exc) from exc
        finally:
            if not context_deleted:
                await self._delete_context_best_effort(sandbox, context_id)

    async def read(self, path: Path, *, user: Union[str, User, None] = None) -> io.IOBase:
        try:
            workspace_path = (
                await self._check_read_with_exec(path, user=user)
                if user is not None
                else await self._validate_remote_path_access(path)
            )
            sandbox = self._require_sandbox(("read", path))
            data = await asyncio.to_thread(sandbox.read_file, str(workspace_path))
            return io.BytesIO(data)
        except APIError as exc:
            if _api_status(exc) == 404:
                raise WorkspaceReadNotFoundError(path=Path(path), cause=exc) from exc
            raise WorkspaceArchiveReadError(path=Path(path), cause=exc, retryable=False) from exc

    async def write(
        self,
        path: Path,
        data: io.IOBase,
        *,
        user: Union[str, User, None] = None,
    ) -> None:
        try:
            payload = coerce_write_payload(path=Path(path), data=data)
            workspace_path = (
                await self._check_write_with_exec(path, user=user)
                if user is not None
                else await self._validate_remote_path_access(path, for_write=True)
            )
            sandbox = self._require_sandbox(("write", path))
            await asyncio.to_thread(sandbox.write_file, str(workspace_path), payload.stream.read())
        except APIError as exc:
            raise WorkspaceArchiveWriteError(path=Path(path), cause=exc, retryable=False) from exc

    async def running(self) -> bool:
        sandbox_id = self.state.sandbox_id
        if not sandbox_id:
            return False
        try:
            status = await asyncio.to_thread(self._client.status_sandbox, sandbox_id)
        except APIError as exc:
            if _api_status(exc) == 404:
                return False
            raise
        return _status_value(getattr(status, "status", UNSET)) == SandboxLifecycleStatus.RUNNING.value

    async def persist_workspace(self) -> io.IOBase:
        if self.state.create_volume_snapshot_on_stop and self.state.volume_id:
            await self._create_volume_snapshot_best_effort()

        payload = {
            "type": SANDBOX0_WORKSPACE_REFERENCE_TYPE,
            "volume_id": self.state.volume_id,
            "volume_snapshot_id": self.state.volume_snapshot_id,
            "workspace_mount_path": self.state.workspace_mount_path,
        }
        return io.BytesIO(json.dumps(payload, sort_keys=True).encode())

    async def hydrate_workspace(self, data: io.IOBase) -> None:
        try:
            payload = json.loads(data.read().decode())
        except Exception as exc:
            raise WorkspaceArchiveWriteError(path=Path(self.state.workspace_mount_path), cause=exc) from exc

        if not isinstance(payload, dict) or payload.get("type") != SANDBOX0_WORKSPACE_REFERENCE_TYPE:
            raise WorkspaceArchiveWriteError(
                path=Path(self.state.workspace_mount_path),
                context={"reason": "unsupported_workspace_payload"},
            )

        volume_id = payload.get("volume_id")
        if isinstance(volume_id, str) and volume_id:
            self.state.volume_id = volume_id

        snapshot_id = payload.get("volume_snapshot_id")
        if isinstance(snapshot_id, str) and snapshot_id:
            self.state.volume_snapshot_id = snapshot_id

        mount_path = payload.get("workspace_mount_path")
        if isinstance(mount_path, str) and mount_path:
            self.state.workspace_mount_path = mount_path

        self.state.volume_workspace_ready = True

    async def _persist_snapshot(self) -> None:
        data = await self.persist_workspace()
        try:
            await self.state.snapshot.persist(data, dependencies=self.dependencies)
        finally:
            data.close()

    async def _try_reconnect_sandbox(self, sandbox_id: str) -> Optional[Sandbox]:
        try:
            status = await self._wait_sandbox_running(sandbox_id)
        except APIError as exc:
            if _api_status(exc) == 404:
                self.state.sandbox_id = None
                return None
            raise

        if status is None:
            return None
        return Sandbox(id=sandbox_id, client=self._client, template=self.state.template)

    async def _wait_sandbox_running(self, sandbox_id: str) -> Optional[Any]:
        deadline = time.monotonic() + self.state.start_timeout_sec
        while True:
            status = await asyncio.to_thread(self._client.status_sandbox, sandbox_id)
            status_value = _status_value(getattr(status, "status", UNSET))
            if status_value == SandboxLifecycleStatus.RUNNING.value:
                return status
            if status_value == SandboxLifecycleStatus.PAUSED.value:
                await asyncio.to_thread(self._client.resume_sandbox, sandbox_id)
            elif status_value in (
                SandboxLifecycleStatus.FAILED.value,
                SandboxLifecycleStatus.TERMINATING.value,
            ):
                return None

            if time.monotonic() >= deadline:
                raise WorkspaceStartError(
                    path=Path(self.state.workspace_mount_path),
                    context={"sandbox_id": sandbox_id, "status": status_value},
                )
            await asyncio.sleep(max(self.state.poll_interval_sec, 0.01))

    async def _claim_replacement_sandbox(self) -> Sandbox:
        config = None
        if self.state.sandbox_ttl_sec is not None:
            config = SandboxConfig(ttl=self.state.sandbox_ttl_sec)

        try:
            sandbox = await asyncio.to_thread(
                self._client.sandboxes.claim,
                self.state.template,
                config=config,
                mounts=[
                    ClaimMountRequest(
                        sandboxvolume_id=self.state.volume_id,
                        mount_point=self.state.workspace_mount_path,
                    )
                ],
            )
        except Exception as exc:
            raise WorkspaceStartError(path=Path(self.state.workspace_mount_path), cause=exc) from exc

        await self._wait_sandbox_running(sandbox.id)
        return sandbox

    async def _create_volume_snapshot_best_effort(self) -> None:
        request = CreateSnapshotRequest(
            name="openai-agents-{}".format(self.state.session_id.hex),
            description="OpenAI Agents SDK workspace snapshot",
        )
        try:
            snapshot = await asyncio.to_thread(
                self._client.volumes.create_snapshot,
                self.state.volume_id,
                request,
            )
        except APIError:
            return
        self.state.volume_snapshot_id = snapshot.id

    async def _delete_context_best_effort(self, sandbox: Sandbox, context_id: str) -> None:
        try:
            await asyncio.to_thread(sandbox.delete_context, context_id=context_id)
        except Exception:
            return

    def _require_sandbox(self, command: Sequence[Union[str, Path]]) -> Sandbox:
        if self._sandbox is None:
            raise ExecTransportError(
                command=command,
                context={"reason": "sandbox_not_started"},
                retryable=True,
            )
        return self._sandbox

class Sandbox0SandboxClient(BaseSandboxClient[Sandbox0SandboxClientOptions]):
    """OpenAI Agents SDK sandbox client for Sandbox0."""

    backend_id = BACKEND_ID
    supports_default_options = True

    def __init__(
        self,
        *,
        token: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        client: Optional[Sandbox0Client] = None,
        timeout: Optional[float] = None,
        user_agent: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        verify_ssl: bool = True,
        instrumentation: Any = None,
        dependencies: Any = None,
    ) -> None:
        self._instrumentation = instrumentation
        self._dependencies = dependencies

        if client is not None:
            self._client = client
            return

        resolved_token = token or api_key or os.environ.get("SANDBOX0_TOKEN") or os.environ.get("SANDBOX0_API_KEY")
        if not resolved_token:
            raise ValueError("Sandbox0SandboxClient requires token/api_key or SANDBOX0_TOKEN")

        self._client = Sandbox0Client(
            token=resolved_token,
            base_url=base_url or os.environ.get("SANDBOX0_BASE_URL") or DEFAULT_BASE_URL,
            timeout=timeout,
            user_agent=user_agent,
            headers=headers,
            verify_ssl=verify_ssl,
        )

    async def create(
        self,
        *,
        snapshot: Union[SnapshotSpec, SnapshotBase, None] = None,
        manifest: Optional[Manifest] = None,
        options: Sandbox0SandboxClientOptions = Sandbox0SandboxClientOptions(),
    ) -> SandboxSession:
        manifest = manifest or Manifest()
        if manifest.root != options.workspace_mount_path:
            raise ValueError(
                "manifest.root must match Sandbox0 workspace_mount_path "
                "({!r} != {!r})".format(manifest.root, options.workspace_mount_path)
            )

        resolved_snapshot = resolve_snapshot(snapshot, str(uuid.uuid4()))
        if getattr(resolved_snapshot, "type", None) != "noop":
            raise ValueError(
                "Sandbox0SandboxClient uses Sandbox0 SandboxVolume persistence; "
                "use Sandbox0SandboxClientOptions(volume_snapshot_id=...) instead of an OpenAI SDK snapshot"
            )
        volume_id = options.volume_id
        volume_workspace_ready = bool(options.volume_id or options.volume_snapshot_id)
        if not volume_id:
            volume = await asyncio.to_thread(
                self._client.volumes.create,
                CreateSandboxVolumeRequest(
                    snapshot_id=options.volume_snapshot_id or UNSET,
                    default_posix_uid=options.default_posix_uid,
                    default_posix_gid=options.default_posix_gid,
                ),
            )
            volume_id = volume.id

        config = None
        if options.sandbox_ttl_sec is not None:
            config = SandboxConfig(ttl=options.sandbox_ttl_sec)

        sandbox = await asyncio.to_thread(
            self._client.sandboxes.claim,
            options.template,
            config=config,
            mounts=[
                ClaimMountRequest(
                    sandboxvolume_id=volume_id,
                    mount_point=options.workspace_mount_path,
                )
            ],
        )

        state = Sandbox0SandboxSessionState(
            snapshot=resolved_snapshot,
            manifest=manifest,
            exposed_ports=options.exposed_ports,
            sandbox_id=sandbox.id,
            volume_id=volume_id,
            volume_snapshot_id=options.volume_snapshot_id,
            template=options.template,
            workspace_mount_path=options.workspace_mount_path,
            sandbox_ttl_sec=options.sandbox_ttl_sec,
            delete_sandbox_on_delete=options.delete_sandbox_on_delete,
            delete_volume_on_delete=options.delete_volume_on_delete,
            create_volume_snapshot_on_stop=options.create_volume_snapshot_on_stop,
            poll_interval_sec=options.poll_interval_sec,
            start_timeout_sec=options.start_timeout_sec,
            volume_workspace_ready=volume_workspace_ready,
        )
        inner = Sandbox0SandboxSession.from_state(state=state, client=self._client)
        return self._wrap_session(inner, instrumentation=self._instrumentation)

    async def resume(self, state: SandboxSessionState) -> SandboxSession:
        parsed = Sandbox0SandboxSessionState.model_validate(state.model_dump())
        inner = Sandbox0SandboxSession.from_state(state=parsed, client=self._client)
        return self._wrap_session(inner, instrumentation=self._instrumentation)

    async def delete(self, session: SandboxSession) -> SandboxSession:
        inner = _unwrap_sandbox0_session(session)
        if inner.state.delete_sandbox_on_delete and inner.state.sandbox_id:
            sandbox_id = inner.state.sandbox_id
            try:
                await asyncio.to_thread(self._client.delete_sandbox, sandbox_id)
            except APIError as exc:
                if _api_status(exc) != 404:
                    raise
            inner.state.sandbox_id = None
            inner._sandbox = None

        if inner.state.delete_volume_on_delete and inner.state.volume_id:
            try:
                await asyncio.to_thread(self._client.volumes.delete, inner.state.volume_id, force=True)
            except APIError as exc:
                if _api_status(exc) != 404:
                    raise

        return session

    def deserialize_session_state(self, payload: Dict[str, object]) -> SandboxSessionState:
        return Sandbox0SandboxSessionState.model_validate(payload)


def _unwrap_sandbox0_session(session: SandboxSession) -> Sandbox0SandboxSession:
    inner = getattr(session, "_inner", session)
    if not isinstance(inner, Sandbox0SandboxSession):
        raise TypeError("expected a Sandbox0 SandboxSession")
    return inner


def _optional_text(value: Any) -> str:
    if _is_unset(value) or value is None:
        return ""
    return cast(str, value)


def _optional_int(value: Any) -> Optional[int]:
    if _is_unset(value) or value is None:
        return None
    return int(value)


def _is_unset(value: Any) -> bool:
    return value is UNSET or value.__class__.__name__ == "Unset"


def _status_value(value: Any) -> Optional[str]:
    if _is_unset(value) or value is None:
        return None
    if isinstance(value, SandboxLifecycleStatus):
        return value.value
    return str(value)


def _api_status(error: APIError) -> int:
    return int(getattr(error, "status_code", 0))
