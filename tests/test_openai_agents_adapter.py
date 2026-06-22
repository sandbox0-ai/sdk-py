from __future__ import annotations

import asyncio
import io
import unittest
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Literal, Optional

from agents.sandbox.errors import ExecTimeoutError
from agents.sandbox.manifest import Manifest
from agents.sandbox.snapshot import NoopSnapshot, SnapshotBase

from sandbox0.apispec.models.sandbox_lifecycle_status import SandboxLifecycleStatus
from sandbox0.sandbox import Sandbox
from sandbox0_openai_agents import (
    Sandbox0SandboxClient,
    Sandbox0SandboxClientOptions,
    Sandbox0SandboxSession,
    Sandbox0SandboxSessionState,
)


class _FakeSnapshot(SnapshotBase):
    type: Literal["sandbox0-test-snapshot"] = "sandbox0-test-snapshot"

    async def persist(self, data: io.IOBase, *, dependencies: Any = None) -> None:
        return None

    async def restore(self, *, dependencies: Any = None) -> io.IOBase:
        return io.BytesIO()

    async def restorable(self, *, dependencies: Any = None) -> bool:
        return True


class _FakeVolumes:
    def __init__(self) -> None:
        self.created_request: Any = None
        self.snapshots: list[tuple[str, Any]] = []
        self.deleted: list[tuple[str, bool]] = []
        self.files: dict[tuple[str, str], bytes] = {("vol_1", "/nested/file.txt"): b"existing"}
        self.writes: list[tuple[str, str, bytes]] = []

    def create(self, request: Any) -> Any:
        self.created_request = request
        return SimpleNamespace(id="vol_1")

    def create_snapshot(self, volume_id: str, request: Any) -> Any:
        self.snapshots.append((volume_id, request))
        return SimpleNamespace(id="snap_1")

    def delete(self, volume_id: str, *, force: bool = False) -> Any:
        self.deleted.append((volume_id, force))
        return SimpleNamespace()

    def read_file(self, volume_id: str, path: str) -> bytes:
        return self.files[(volume_id, path)]

    def write_file(self, volume_id: str, path: str, data: bytes) -> Any:
        self.writes.append((volume_id, path, data))
        self.files[(volume_id, path)] = data
        return SimpleNamespace()


class _FakeSandboxes:
    def __init__(self, client: "_FakeSandbox0Client") -> None:
        self._client = client
        self.claims: list[tuple[str, Any, Any]] = []

    def claim(self, template: str, config: Any = None, mounts: Optional[list[Any]] = None, snapshot_id: Optional[str] = None) -> Sandbox:
        self.claims.append((template, config, mounts))
        return Sandbox(id="sb_1", client=self._client, template=template, status="running")


class _FakeSandbox0Client:
    def __init__(self) -> None:
        self.volumes = _FakeVolumes()
        self.sandboxes = _FakeSandboxes(self)
        self.deleted_sandboxes: list[str] = []

    def status_sandbox(self, sandbox_id: str) -> Any:
        return SimpleNamespace(status=SandboxLifecycleStatus.RUNNING)

    def resume_sandbox(self, sandbox_id: str) -> Any:
        return SimpleNamespace()

    def delete_sandbox(self, sandbox_id: str) -> Any:
        self.deleted_sandboxes.append(sandbox_id)
        return SimpleNamespace()


class _FakeCommandSandbox:
    def __init__(self, responses: list[Any]) -> None:
        self.responses = responses
        self.created_request: Any = None
        self.deleted_contexts: list[str] = []
        self.files: dict[str, bytes] = {"/workspace/nested/file.txt": b"existing"}
        self.writes: list[tuple[str, bytes]] = []

    def create_context(self, request: Any) -> Any:
        self.created_request = request
        return SimpleNamespace(id="ctx_1")

    def get_context(self, context_id: str) -> Any:
        if self.responses:
            return self.responses.pop(0)
        return SimpleNamespace(id=context_id, running=True)

    def delete_context(self, context_id: str) -> Any:
        self.deleted_contexts.append(context_id)
        return SimpleNamespace()

    def read_file(self, path: str) -> bytes:
        return self.files[path]

    def write_file(self, path: str, data: bytes) -> Any:
        self.writes.append((path, data))
        self.files[path] = data
        return SimpleNamespace()


def _state(**updates: Any) -> Sandbox0SandboxSessionState:
    values: dict[str, Any] = {
        "snapshot": NoopSnapshot(id="noop_1"),
        "manifest": Manifest(),
        "sandbox_id": "sb_1",
        "volume_id": "vol_1",
        "poll_interval_sec": 0.01,
        "start_timeout_sec": 1.0,
    }
    values.update(updates)
    return Sandbox0SandboxSessionState(**values)


class TestOpenAIAgentsAdapter(unittest.TestCase):
    def test_create_claims_workspace_volume_and_delete_removes_volume_by_default(self) -> None:
        fake_client = _FakeSandbox0Client()
        client = Sandbox0SandboxClient(client=fake_client)  # type: ignore[arg-type]

        session = asyncio.run(
            client.create(options=Sandbox0SandboxClientOptions(template="default"))
        )

        self.assertEqual(session.state.sandbox_id, "sb_1")
        self.assertEqual(session.state.volume_id, "vol_1")
        self.assertFalse(session.state.volume_workspace_ready)
        self.assertEqual(fake_client.sandboxes.claims[0][0], "default")
        mount = fake_client.sandboxes.claims[0][2][0]
        self.assertEqual(mount.sandboxvolume_id, "vol_1")
        self.assertEqual(mount.mount_point, "/workspace")

        asyncio.run(client.delete(session))

        self.assertEqual(fake_client.deleted_sandboxes, ["sb_1"])
        self.assertEqual(fake_client.volumes.deleted, [("vol_1", True)])
        self.assertIsNone(session.state.sandbox_id)

    def test_delete_preserves_volume_when_configured(self) -> None:
        fake_client = _FakeSandbox0Client()
        client = Sandbox0SandboxClient(client=fake_client)  # type: ignore[arg-type]

        session = asyncio.run(
            client.create(
                options=Sandbox0SandboxClientOptions(
                    template="default",
                    delete_volume_on_delete=False,
                )
            )
        )

        asyncio.run(client.delete(session))

        self.assertEqual(fake_client.deleted_sandboxes, ["sb_1"])
        self.assertEqual(fake_client.volumes.deleted, [])
        self.assertEqual(session.state.volume_id, "vol_1")

    def test_state_round_trips_through_client_serialization(self) -> None:
        fake_client = _FakeSandbox0Client()
        client = Sandbox0SandboxClient(client=fake_client)  # type: ignore[arg-type]
        state = _state(volume_snapshot_id="snap_1", volume_workspace_ready=True)

        payload = client.serialize_session_state(state)
        parsed = client.deserialize_session_state(payload)

        self.assertIsInstance(parsed, Sandbox0SandboxSessionState)
        self.assertEqual(parsed.volume_id, "vol_1")
        self.assertEqual(parsed.volume_snapshot_id, "snap_1")
        self.assertTrue(parsed.volume_workspace_ready)

    def test_create_rejects_generic_openai_snapshot_specs(self) -> None:
        fake_client = _FakeSandbox0Client()
        client = Sandbox0SandboxClient(client=fake_client)  # type: ignore[arg-type]

        with self.assertRaisesRegex(ValueError, "volume_snapshot_id"):
            asyncio.run(
                client.create(
                    snapshot=_FakeSnapshot(id="snapshot_1"),
                    options=Sandbox0SandboxClientOptions(),
                )
            )

    def test_exec_internal_polls_context_and_returns_split_output(self) -> None:
        session = Sandbox0SandboxSession(
            state=_state(),
            client=_FakeSandbox0Client(),  # type: ignore[arg-type]
        )
        command_sandbox = _FakeCommandSandbox(
            [
                SimpleNamespace(id="ctx_1", running=True),
                SimpleNamespace(
                    id="ctx_1",
                    running=False,
                    stdout="out",
                    stderr="err",
                    exit_code=7,
                ),
            ]
        )
        session._sandbox = command_sandbox  # type: ignore[assignment]

        result = asyncio.run(session._exec_internal("sh", "-c", "printf out; printf err >&2; exit 7"))

        self.assertEqual(result.stdout, b"out")
        self.assertEqual(result.stderr, b"err")
        self.assertEqual(result.exit_code, 7)
        self.assertEqual(command_sandbox.created_request.cmd.command, ["sh", "-c", "printf out; printf err >&2; exit 7"])
        self.assertIs(command_sandbox.created_request.wait_until_done, False)
        self.assertEqual(command_sandbox.created_request.cwd, "/workspace")
        self.assertEqual(command_sandbox.deleted_contexts, ["ctx_1"])

    def test_exec_timeout_deletes_context(self) -> None:
        session = Sandbox0SandboxSession(
            state=_state(poll_interval_sec=0.01),
            client=_FakeSandbox0Client(),  # type: ignore[arg-type]
        )
        command_sandbox = _FakeCommandSandbox([SimpleNamespace(id="ctx_1", running=True)])
        session._sandbox = command_sandbox  # type: ignore[assignment]

        with self.assertRaises(ExecTimeoutError):
            asyncio.run(session._exec_internal("sleep", "10", timeout=0.01))

        self.assertEqual(command_sandbox.deleted_contexts, ["ctx_1"])

    def test_read_and_write_use_live_sandbox_file_api_under_workspace_mount(self) -> None:
        fake_client = _FakeSandbox0Client()
        session = Sandbox0SandboxSession(
            state=_state(),
            client=fake_client,  # type: ignore[arg-type]
        )
        command_sandbox = _FakeCommandSandbox([])
        session._sandbox = command_sandbox  # type: ignore[assignment]

        async def fake_validate(path: Path, *, for_write: bool = False) -> Path:
            return Path("/workspace/nested/file.txt")

        session._validate_remote_path_access = fake_validate  # type: ignore[method-assign]

        data = asyncio.run(session.read(Path("nested/file.txt")))
        self.assertEqual(data.read(), b"existing")

        asyncio.run(session.write(Path("nested/file.txt"), io.BytesIO(b"updated")))
        self.assertEqual(command_sandbox.writes, [("/workspace/nested/file.txt", b"updated")])
        self.assertEqual(fake_client.volumes.writes, [])

    def test_persist_workspace_records_volume_snapshot_when_available(self) -> None:
        fake_client = _FakeSandbox0Client()
        session = Sandbox0SandboxSession(
            state=_state(),
            client=fake_client,  # type: ignore[arg-type]
        )

        payload = asyncio.run(session.persist_workspace())
        data = payload.read().decode()

        self.assertIn('"type": "sandbox0_volume_reference"', data)
        self.assertIn('"volume_id": "vol_1"', data)
        self.assertEqual(session.state.volume_snapshot_id, "snap_1")
        self.assertEqual(len(fake_client.volumes.snapshots), 1)


if __name__ == "__main__":
    unittest.main()
