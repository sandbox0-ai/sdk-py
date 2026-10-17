from unittest import TestCase
import json
import httpx
from sandbox0 import Client, APIError
from sandbox0.apispec.models.capture_sandbox_root_fs_snapshot_request import CaptureSandboxRootFSSnapshotRequest


class TestConditionalSnapshot(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_exact_request_after_uncertain_reply(self):
        calls = []
        def handler(request):
            calls.append(request)
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.url.path, "/api/v1/sandboxes/source/snapshots/capture")
            self.assertEqual(request.headers["Idempotency-Key"], "capture-7")
            self.assertEqual(json.loads(request.content), {"expected_runtime_generation": 7})
            if len(calls) == 1:
                return httpx.Response(503, json={"success": False, "error": {"code": "unavailable", "message": "uncertain"}})
            return httpx.Response(201, json={"success": True, "data": {"id": "snapshot", "sandbox_id": "source", "generation_id": "captured-head", "created_at": "2026-10-16T00:00:00Z"}})
        client = self.client(handler)
        body = CaptureSandboxRootFSSnapshotRequest(expected_runtime_generation=7)
        with self.assertRaises(APIError):
            client.sandboxes.capture_rootfs_snapshot("source", body, idempotency_key="capture-7")
        self.assertEqual(len(calls), 1)
        self.assertEqual(client.sandboxes.capture_rootfs_snapshot("source", body, idempotency_key="capture-7").generation_id, "captured-head")
        self.assertEqual(len(calls), 2)

    def test_invalid_generation_never_sends(self):
        client = self.client(lambda request: self.fail("unexpected network request"))
        for generation in [True, 0, -1, 1.5, 9007199254740992]:
            with self.subTest(generation=generation), self.assertRaises(ValueError):
                client.sandboxes.capture_rootfs_snapshot("source", CaptureSandboxRootFSSnapshotRequest(expected_runtime_generation=generation), idempotency_key="capture-7")

    def test_observation_only_reads_original_coordinates(self):
        for status in [200, 404, 409, 503]:
            with self.subTest(status=status):
                calls = []
                def handler(request):
                    calls.append(request)
                    self.assertEqual(request.method, "GET")
                    self.assertEqual(request.url.path, "/api/v1/sandboxes/source/snapshots/capture")
                    self.assertEqual(request.url.params["expected_runtime_generation"], "7")
                    self.assertEqual(request.headers["Idempotency-Key"], "capture-7")
                    self.assertEqual(request.content, b"")
                    body = {"success": True, "data": {"id": "original", "sandbox_id": "source", "generation_id": "captured-head", "created_at": "2026-10-16T00:00:00Z"}} if status == 200 else {"success": False, "error": {"code": "unavailable", "message": "retained request"}}
                    return httpx.Response(status, json=body)
                client = self.client(handler)
                if status == 200:
                    self.assertEqual(client.sandboxes.get_captured_rootfs_snapshot("source", expected_runtime_generation=7, idempotency_key="capture-7").generation_id, "captured-head")
                else:
                    with self.assertRaises(APIError):
                        client.sandboxes.get_captured_rootfs_snapshot("source", expected_runtime_generation=7, idempotency_key="capture-7")
                self.assertEqual(len(calls), 1)
