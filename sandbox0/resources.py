from __future__ import annotations

import time
from typing import Any, Callable, List, Optional, TYPE_CHECKING, Union

from sandbox0.apispec.api.sandboxes import delete_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_status
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_pause
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_refresh
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_resume
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id
from sandbox0.apispec.api.sandbox_rootfs import (
    delete_api_v1_sandbox_rootfs_snapshots_snapshot_id,
)
from sandbox0.apispec.api.sandbox_rootfs import (
    get_api_v1_sandbox_rootfs_snapshots_snapshot_id,
)
from sandbox0.apispec.api.sandbox_rootfs import get_api_v1_sandboxes_id_snapshots
from sandbox0.apispec.api.sandbox_rootfs import post_api_v1_sandboxes_id_fork
from sandbox0.apispec.api.sandbox_rootfs import post_api_v1_sandboxes_id_rootfs_restore
from sandbox0.apispec.api.sandbox_rootfs import post_api_v1_sandboxes_id_snapshots
from sandbox0.apispec.api.sandbox_rootfs import put_api_v1_sandboxes_id_rootfs_rebase
from sandbox0.apispec.models.claim_request import ClaimRequest
from sandbox0.apispec.models.create_sandbox_root_fs_snapshot_request import (
    CreateSandboxRootFSSnapshotRequest,
)
from sandbox0.apispec.models.fork_sandbox_request import ForkSandboxRequest
from sandbox0.apispec.models.fork_sandbox_response import ForkSandboxResponse
from sandbox0.apispec.models.pause_sandbox_response import PauseSandboxResponse
from sandbox0.apispec.models.rebase_sandbox_root_fs_request import (
    RebaseSandboxRootFSRequest,
)
from sandbox0.apispec.models.rebase_sandbox_root_fs_response import (
    RebaseSandboxRootFSResponse,
)
from sandbox0.apispec.models.sandbox_refresh_request import SandboxRefreshRequest
from sandbox0.apispec.models.refresh_response import RefreshResponse
from sandbox0.apispec.models.restore_sandbox_root_fs_request import (
    RestoreSandboxRootFSRequest,
)
from sandbox0.apispec.models.restore_sandbox_root_fs_response import (
    RestoreSandboxRootFSResponse,
)
from sandbox0.apispec.models.resume_sandbox_response import ResumeSandboxResponse
from sandbox0.apispec.models.sandbox import Sandbox as APISandbox
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_lifecycle_status import SandboxLifecycleStatus
from sandbox0.apispec.models.sandbox_resource_config import SandboxResourceConfig
from sandbox0.apispec.models.sandbox_root_fs_snapshot import SandboxRootFSSnapshot
from sandbox0.apispec.models.sandbox_status import SandboxStatus
from sandbox0.apispec.models.sandbox_summary import SandboxSummary
from sandbox0.apispec.models.sandbox_update_request import SandboxUpdateRequest
from sandbox0.apispec.models.success_claim_response import SuccessClaimResponse
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_pause_sandbox_response import (
    SuccessPauseSandboxResponse,
)
from sandbox0.apispec.models.success_rebase_sandbox_root_fs_response import (
    SuccessRebaseSandboxRootFSResponse,
)
from sandbox0.apispec.models.success_fork_sandbox_response import (
    SuccessForkSandboxResponse,
)
from sandbox0.apispec.models.success_refresh_response import SuccessRefreshResponse
from sandbox0.apispec.models.success_restore_sandbox_root_fs_response import (
    SuccessRestoreSandboxRootFSResponse,
)
from sandbox0.apispec.models.success_resume_sandbox_response import (
    SuccessResumeSandboxResponse,
)
from sandbox0.apispec.models.success_sandbox_root_fs_snapshot_list_response import (
    SuccessSandboxRootFSSnapshotListResponse,
)
from sandbox0.apispec.models.success_sandbox_root_fs_snapshot_response import (
    SuccessSandboxRootFSSnapshotResponse,
)
from sandbox0.apispec.models.success_sandbox_list_response import (
    SuccessSandboxListResponse,
)
from sandbox0.apispec.models.success_sandbox_response import SuccessSandboxResponse
from sandbox0.apispec.models.success_sandbox_status_response import (
    SuccessSandboxStatusResponse,
)
from sandbox0.apispec.types import UNSET
from sandbox0.response import ensure_data, ensure_model
from sandbox0.errors import SandboxWaitTimeoutError
from sandbox0.sessions import SandboxSession

if TYPE_CHECKING:
    from sandbox0.client import Client
    from sandbox0.sandbox import Sandbox


def _sandbox_config_with_memory(config: Optional[SandboxConfig], memory: Optional[str]) -> Optional[SandboxConfig]:
    if memory is None:
        return config
    resources = SandboxResourceConfig(memory=memory)
    if config is None:
        return SandboxConfig(resources=resources)
    data = config.to_dict()
    data["resources"] = resources.to_dict()
    return SandboxConfig.from_dict(data)


class Sandboxes:
    def __init__(self, client: "Client") -> None:
        self._client = client

    def claim(
        self,
        template: str,
        config: Optional[SandboxConfig] = None,
        snapshot_id: Optional[str] = None,
        memory: Optional[str] = None,
    ) -> "Sandbox":
        request = ClaimRequest(template=template)
        config = _sandbox_config_with_memory(config, memory)
        if config is not None:
            request.config = config
        if snapshot_id is not None:
            request.snapshot_id = snapshot_id
        resp = post_api_v1_sandboxes.sync_detailed(client=self._client.api, body=request)
        data = ensure_data(resp, SuccessClaimResponse)
        from sandbox0.sandbox import Sandbox

        return Sandbox(
            id=data.sandbox_id,
            client=self._client,
            template=data.template,
            cluster_id=None if data.cluster_id.__class__.__name__ == "Unset" else data.cluster_id,
            runtime_id=data.runtime_id,
            status=data.status,
        )

    def open(
        self,
        template: str,
        config: Optional[SandboxConfig] = None,
        snapshot_id: Optional[str] = None,
        memory: Optional[str] = None,
    ) -> SandboxSession:
        sandbox = self.claim(
            template,
            config=config,
            snapshot_id=snapshot_id,
            memory=memory,
        )
        return SandboxSession(sandbox, closer=lambda: None if self.delete(sandbox.id) else None)

    def get(self, sandbox_id: str) -> APISandbox:
        resp = get_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxResponse)

    def wait_for_lifecycle(
        self,
        sandbox_id: str,
        predicate: Callable[[APISandbox], bool],
        *,
        timeout_sec: float = 60.0,
        poll_interval_sec: float = 0.5,
    ) -> APISandbox:
        """Poll committed sandbox details until ``predicate`` matches."""
        if timeout_sec < 0:
            raise ValueError("timeout_sec cannot be negative")
        if poll_interval_sec <= 0:
            raise ValueError("poll_interval_sec must be positive")

        started_at = time.monotonic()
        last_sandbox: Optional[APISandbox] = None
        while True:
            last_sandbox = self.get(sandbox_id)
            if predicate(last_sandbox):
                return last_sandbox

            remaining = timeout_sec - (time.monotonic() - started_at)
            if remaining <= 0:
                raise SandboxWaitTimeoutError(
                    sandbox_id=sandbox_id,
                    timeout_sec=timeout_sec,
                    last_sandbox=last_sandbox,
                )
            time.sleep(min(poll_interval_sec, remaining))

    def update(self, sandbox_id: str, request: SandboxUpdateRequest) -> APISandbox:
        resp = put_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api, body=request)
        return ensure_data(resp, SuccessSandboxResponse)

    def delete(self, sandbox_id: str) -> SuccessMessageResponse:
        resp = delete_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_model(resp, SuccessMessageResponse)

    def status(self, sandbox_id: str) -> SandboxStatus:
        resp = get_api_v1_sandboxes_id_status.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxStatusResponse)

    def pause(self, sandbox_id: str) -> PauseSandboxResponse:
        resp = post_api_v1_sandboxes_id_pause.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessPauseSandboxResponse)

    def pause_and_wait(
        self,
        sandbox_id: str,
        *,
        timeout_sec: float = 60.0,
        poll_interval_sec: float = 0.5,
    ) -> APISandbox:
        """Request a pause and wait for its durable checkpoint to commit."""
        self.pause(sandbox_id)
        return self.wait_for_lifecycle(
            sandbox_id,
            lambda sandbox: sandbox.status == SandboxLifecycleStatus.PAUSED and sandbox.paused,
            timeout_sec=timeout_sec,
            poll_interval_sec=poll_interval_sec,
        )

    def resume(self, sandbox_id: str) -> ResumeSandboxResponse:
        resp = post_api_v1_sandboxes_id_resume.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessResumeSandboxResponse)

    def resume_and_wait(
        self,
        sandbox_id: str,
        *,
        timeout_sec: float = 60.0,
        poll_interval_sec: float = 0.5,
    ) -> APISandbox:
        """Request a resume and wait for the committed running generation."""
        before = self.get(sandbox_id)
        self.resume(sandbox_id)
        minimum_generation = before.runtime_generation
        if before.paused or before.status == SandboxLifecycleStatus.PAUSED:
            minimum_generation += 1
        return self.wait_for_lifecycle(
            sandbox_id,
            lambda sandbox: sandbox.status == SandboxLifecycleStatus.RUNNING and not sandbox.paused and sandbox.runtime_generation >= minimum_generation,
            timeout_sec=timeout_sec,
            poll_interval_sec=poll_interval_sec,
        )

    def refresh(self, sandbox_id: str, request: Optional[SandboxRefreshRequest] = None) -> RefreshResponse:
        body = request if request is not None else SandboxRefreshRequest()
        resp = post_api_v1_sandboxes_id_refresh.sync_detailed(id=sandbox_id, client=self._client.api, body=body)
        return ensure_data(resp, SuccessRefreshResponse)

    def create_rootfs_snapshot(
        self,
        sandbox_id: str,
        request: Optional[CreateSandboxRootFSSnapshotRequest] = None,
    ) -> SandboxRootFSSnapshot:
        body = request if request is not None else CreateSandboxRootFSSnapshotRequest()
        resp = post_api_v1_sandboxes_id_snapshots.sync_detailed(id=sandbox_id, client=self._client.api, body=body)
        return ensure_data(resp, SuccessSandboxRootFSSnapshotResponse)

    def list_rootfs_snapshots(self, sandbox_id: str) -> List[SandboxRootFSSnapshot]:
        resp = get_api_v1_sandboxes_id_snapshots.sync_detailed(id=sandbox_id, client=self._client.api)
        data = ensure_data(resp, SuccessSandboxRootFSSnapshotListResponse)
        return data.snapshots

    def get_rootfs_snapshot(self, snapshot_id: str) -> SandboxRootFSSnapshot:
        resp = get_api_v1_sandbox_rootfs_snapshots_snapshot_id.sync_detailed(
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_data(resp, SuccessSandboxRootFSSnapshotResponse)

    def delete_rootfs_snapshot(self, snapshot_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandbox_rootfs_snapshots_snapshot_id.sync_detailed(
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_model(resp, SuccessDeletedResponse)

    def restore_rootfs(
        self,
        sandbox_id: str,
        request: RestoreSandboxRootFSRequest,
    ) -> RestoreSandboxRootFSResponse:
        resp = post_api_v1_sandboxes_id_rootfs_restore.sync_detailed(
            id=sandbox_id,
            client=self._client.api,
            body=request,
        )
        return ensure_data(resp, SuccessRestoreSandboxRootFSResponse)

    def rebase_rootfs(
        self,
        sandbox_id: str,
        request: RebaseSandboxRootFSRequest,
    ) -> RebaseSandboxRootFSResponse:
        resp = put_api_v1_sandboxes_id_rootfs_rebase.sync_detailed(
            id=sandbox_id,
            client=self._client.api,
            body=request,
        )
        return ensure_data(resp, SuccessRebaseSandboxRootFSResponse)

    def fork(self, sandbox_id: str, request: Optional[ForkSandboxRequest] = None) -> ForkSandboxResponse:
        body = request if request is not None else ForkSandboxRequest()
        resp = post_api_v1_sandboxes_id_fork.sync_detailed(id=sandbox_id, client=self._client.api, body=body)
        return ensure_data(resp, SuccessForkSandboxResponse)

    def list(
        self,
        *,
        status: Union[SandboxLifecycleStatus, str] = UNSET,  # type: ignore[assignment]
        template_id: str = UNSET,  # type: ignore[assignment]
        paused: bool = UNSET,  # type: ignore[assignment]
        limit: int = 50,
        offset: int = 0,
    ) -> List[SandboxSummary]:
        status_enum: Union[SandboxLifecycleStatus, Any] = UNSET
        if status != UNSET:
            if isinstance(status, str):
                status_enum = SandboxLifecycleStatus(status)
            else:
                status_enum = status
        resp = get_api_v1_sandboxes.sync_detailed(
            client=self._client.api,
            status=status_enum,
            template_id=template_id,
            paused=paused,
            limit=limit,
            offset=offset,
        )
        data = ensure_data(resp, SuccessSandboxListResponse)
        return data.sandboxes

    def sandbox(self, sandbox_id: str) -> "Sandbox":
        from sandbox0.sandbox import Sandbox

        return Sandbox(id=sandbox_id, client=self._client)
