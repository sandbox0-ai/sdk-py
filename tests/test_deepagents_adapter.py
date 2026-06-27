from __future__ import annotations

import unittest
import importlib.metadata
from types import SimpleNamespace
from typing import Any

try:
    from deepagents.backends.protocol import FileDownloadResponse, FileUploadResponse
except ImportError as exc:  # pragma: no cover - exercised when the extra is absent
    raise unittest.SkipTest("deepagents extra is not installed") from exc

from sandbox0.errors import APIError
from sandbox0.models import CmdResult
from sandbox0.sandbox import Sandbox
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0_deepagents import Sandbox0DeepAgentsSandbox, Sandbox0Provider
from sandbox0_deepagents.backend import _map_file_error
from sandbox0_deepagents.provider import (
    DEFAULT_SANDBOX_HARD_TTL_SEC,
    DEFAULT_SANDBOX_TTL_SEC,
)


class _FakeCommandSandbox:
    id = "sb_1"

    def __init__(self) -> None:
        self.cmd_calls: list[tuple[str, Any]] = []
        self.files: dict[str, bytes] = {}

    def cmd(self, command: str, options: Any) -> CmdResult:
        self.cmd_calls.append((command, options))
        return CmdResult(
            sandbox_id=self.id,
            context_id="ctx_1",
            output_raw="raw",
            stdout="out",
            stderr="err",
            exit_code=7,
        )

    def write_file(self, path: str, data: bytes) -> object:
        if path == "/missing-parent/file.txt":
            raise APIError(status_code=404, message="not found")
        self.files[path] = data
        return SimpleNamespace()

    def read_file(self, path: str) -> bytes:
        if path == "/missing.txt":
            raise APIError(status_code=404, message="not found")
        return self.files[path]


class _FakeSandboxes:
    def __init__(self, client: "_FakeClient") -> None:
        self._client = client
        self.claims: list[tuple[str, Any]] = []
        self.deleted: list[str] = []
        self.gets: list[str] = []

    def claim(self, template: str, config: Any = None) -> Sandbox:
        self.claims.append((template, config))
        return Sandbox(id="sb_claimed", client=self._client, template=template)

    def get(self, sandbox_id: str) -> Any:
        self.gets.append(sandbox_id)
        return SimpleNamespace(
            template_id="default",
            status="running",
            pod_name="pod-a",
        )

    def delete(self, sandbox_id: str) -> object:
        self.deleted.append(sandbox_id)
        return SimpleNamespace()


class _FakeClient:
    def __init__(self) -> None:
        self.sandboxes = _FakeSandboxes(self)


class TestDeepAgentsAdapter(unittest.TestCase):
    def test_execute_uses_shell_command_and_combines_stderr(self) -> None:
        sandbox = _FakeCommandSandbox()
        backend = Sandbox0DeepAgentsSandbox(sandbox=sandbox, working_dir="/workspace")

        result = backend.execute("printf out; printf err >&2; exit 7", timeout=5)

        self.assertEqual(result.exit_code, 7)
        self.assertEqual(result.output, "out\n<stderr>err</stderr>")
        self.assertFalse(result.truncated)
        _, options = sandbox.cmd_calls[0]
        self.assertEqual(options.command, ["bash", "-lc", "printf out; printf err >&2; exit 7"])
        self.assertEqual(options.cwd, "/workspace")
        self.assertEqual(options.ttl_sec, 5)

    def test_upload_and_download_files_preserve_order_and_map_errors(self) -> None:
        sandbox = _FakeCommandSandbox()
        backend = Sandbox0DeepAgentsSandbox(sandbox=sandbox)

        upload = backend.upload_files(
            [
                ("/ok.txt", b"ok"),
                ("relative.txt", b"bad"),
                ("/missing-parent/file.txt", b"bad"),
            ]
        )

        self.assertEqual(
            upload,
            [
                FileUploadResponse(path="/ok.txt", error=None),
                FileUploadResponse(path="relative.txt", error="invalid_path"),
                FileUploadResponse(path="/missing-parent/file.txt", error="file_not_found"),
            ],
        )

        download = backend.download_files(["/ok.txt", "relative.txt", "/missing.txt"])

        self.assertEqual(
            download,
            [
                FileDownloadResponse(path="/ok.txt", content=b"ok", error=None),
                FileDownloadResponse(path="relative.txt", content=None, error="invalid_path"),
                FileDownloadResponse(path="/missing.txt", content=None, error="file_not_found"),
            ],
        )

    def test_provider_claims_default_template_reattaches_and_deletes(self) -> None:
        client = _FakeClient()
        provider = Sandbox0Provider(client=client)  # type: ignore[arg-type]

        created = provider.get_or_create()
        reattached = provider.get_or_create(sandbox_id="sb_existing")
        provider.delete(sandbox_id="sb_claimed")

        self.assertIsInstance(created, Sandbox0DeepAgentsSandbox)
        self.assertIsInstance(reattached, Sandbox0DeepAgentsSandbox)
        self.assertEqual(client.sandboxes.claims[0][0], "default")
        self.assertEqual(client.sandboxes.claims[0][1].ttl, DEFAULT_SANDBOX_TTL_SEC)
        self.assertEqual(
            client.sandboxes.claims[0][1].hard_ttl,
            DEFAULT_SANDBOX_HARD_TTL_SEC,
        )
        self.assertEqual(client.sandboxes.gets, ["sb_existing"])
        self.assertEqual(client.sandboxes.deleted, ["sb_claimed"])
        self.assertEqual(Sandbox0Provider.metadata.name, "sandbox0")
        self.assertTrue(Sandbox0Provider.metadata.supports_sandbox_id)
        self.assertFalse(Sandbox0Provider.metadata.supports_snapshot_name)

    def test_provider_lifecycle_ttls_can_be_overridden(self) -> None:
        client = _FakeClient()
        provider = Sandbox0Provider(client=client)  # type: ignore[arg-type]

        provider.get_or_create(sandbox_ttl_sec=120, sandbox_hard_ttl_sec=240)

        config = client.sandboxes.claims[0][1]
        self.assertEqual(config.ttl, 120)
        self.assertEqual(config.hard_ttl, 240)

    def test_provider_preserves_explicit_sandbox_config_ttls(self) -> None:
        client = _FakeClient()
        provider = Sandbox0Provider(client=client)  # type: ignore[arg-type]

        provider.get_or_create(sandbox_config=SandboxConfig(ttl=7200))

        config = client.sandboxes.claims[0][1]
        self.assertEqual(config.ttl, 7200)
        self.assertEqual(config.hard_ttl, DEFAULT_SANDBOX_HARD_TTL_SEC)

    def test_deepagents_code_entry_point_loads_provider(self) -> None:
        entries = importlib.metadata.entry_points(
            group="deepagents_code.sandbox_providers"
        )
        providers = {entry.name: entry for entry in entries}

        self.assertIn("sandbox0", providers)
        self.assertIs(providers["sandbox0"].load(), Sandbox0Provider)

    def test_path_not_file_error_maps_to_directory(self) -> None:
        error = APIError(
            status_code=500,
            message=(
                'Unexpected API response: {"success":false,"error":'
                '{"code":"path_not_file","message":"path is not a file"}}'
            ),
        )

        self.assertEqual(_map_file_error(error), "is_directory")


if __name__ == "__main__":
    unittest.main()
