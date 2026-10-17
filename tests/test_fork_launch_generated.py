from unittest import TestCase
import json
import httpx
from sandbox0.apispec.client import AuthenticatedClient
from sandbox0.apispec.api.sandbox_rootfs import launch_sandbox_root_fs_fork, get_sandbox_root_fs_fork_launch
from sandbox0.apispec.models.sandbox_root_fs_fork_launch_request import SandboxRootFSForkLaunchRequest
from sandbox0.apispec.models.success_sandbox_root_fs_fork_launch_response import SuccessSandboxRootFSForkLaunchResponse
from sandbox0.apispec.models.error_envelope import ErrorEnvelope

class ForkLaunchGeneratedTests(TestCase):
    def test_original_conditions_and_single_request(self):
        expected = dict(fork_operation_id="fork", filesystem_id="child", head_generation_id="head", writer_epoch=7)
        for method in ["GET", "POST"]:
            for status in [200, 202, 404, 409, 503]:
                if method == "GET" and status == 202:
                    continue
                with self.subTest(method=method, status=status):
                    calls = []
                    def handler(request):
                        calls.append(request)
                        self.assertEqual(request.method, method)
                        self.assertEqual(request.url.path, "/api/v1/sandboxes/child/fork-launch")
                        self.assertEqual(request.headers["Idempotency-Key"], "original")
                        if method == "POST":
                            self.assertEqual(json.loads(request.content), expected)
                            self.assertEqual(request.url.query, b"")
                        else:
                            self.assertEqual(request.content, b"")
                            self.assertEqual(dict(request.url.params), {**expected, "writer_epoch": "7"})
                        return httpx.Response(status, json={"success": True, "data": {"operation_id": "launch", "sandbox_id": "child", **expected, "lifecycle_epoch": 1, "runtime_generation": 0, "state": "pending", "current": True}} if status < 400 else {"success": False, "error": {"code": "unavailable", "message": "retain original"}})
                    client = AuthenticatedClient(base_url="https://example.test", token="test")
                    client.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                    if method == "POST":
                        response = launch_sandbox_root_fs_fork.sync_detailed("child", client=client, body=SandboxRootFSForkLaunchRequest(**expected), idempotency_key="original")
                    else:
                        response = get_sandbox_root_fs_fork_launch.sync_detailed("child", client=client, idempotency_key="original", **expected)
                    self.assertEqual(response.status_code, status)
                    self.assertIsInstance(response.parsed, SuccessSandboxRootFSForkLaunchResponse if status < 400 else ErrorEnvelope)
                    self.assertEqual(len(calls), 1)
                    client.get_httpx_client().close()
