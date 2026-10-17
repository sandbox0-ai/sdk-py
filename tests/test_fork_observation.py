from unittest import TestCase
import json
import httpx
from sandbox0 import Client, APIError
FIXTURE = json.loads(r'''{"operation_id":"fork-op","source_sandbox_id":"source","target_sandbox_id":"child","source_runtime_generation":7,"source_filesystem_id":"source-fs","source_head_generation_id":"source-head","target_filesystem_id":"child","target_head_generation_id":"child-head","base_artifact_digest":"base","source_oci_digest":"oci","writer_epoch":1,"managed_files_size_bytes":100,"auto_resume":false,"automatic_routes":false,"sandbox_created_at":"2026-10-17T00:00:00Z","filesystem_created_at":"2026-10-17T00:00:00Z","observed_at":"2026-10-17T00:00:00Z"}''')

class TestForkObservation(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_original_coordinates_without_retry_or_submission(self):
        for generation in [0, 7]:
            for status in [200, 404, 409, 503]:
                with self.subTest(generation=generation, status=status):
                    calls = []
                    def handler(request):
                        calls.append(request)
                        self.assertEqual(request.method, "GET")
                        self.assertEqual(request.url.path, "/api/v1/sandboxes/source/fork")
                        self.assertEqual(request.url.params["expected_runtime_generation"], str(generation))
                        self.assertEqual(request.headers["Idempotency-Key"], "original-fork")
                        self.assertEqual(request.content, b"")
                        return httpx.Response(status, json={"success": True, "data": {**FIXTURE, "source_runtime_generation": generation}} if status == 200 else {"success": False, "error": {"code": "unavailable", "message": "retain request"}})
                    client = self.client(handler)
                    if status == 200:
                        self.assertEqual(client.sandboxes.get_rootfs_fork("source", expected_runtime_generation=generation, idempotency_key="original-fork").target_sandbox_id, "child")
                    else:
                        with self.assertRaises(APIError):
                            client.sandboxes.get_rootfs_fork("source", expected_runtime_generation=generation, idempotency_key="original-fork")
                    self.assertEqual(len(calls), 1)

    def test_invalid_inputs_and_mismatched_receipts(self):
        calls = []
        data = dict(FIXTURE)
        def handler(request):
            calls.append(request)
            return httpx.Response(200, json={"success": True, "data": data})
        client = self.client(handler)
        for generation in [True, -1, 1.5, 9007199254740992]:
            with self.assertRaises(ValueError):
                client.sandboxes.get_rootfs_fork("source", expected_runtime_generation=generation, idempotency_key="original-fork")
        for key in ["", "bad key"]:
            with self.assertRaises(ValueError):
                client.sandboxes.get_rootfs_fork("source", expected_runtime_generation=7, idempotency_key=key)
        self.assertEqual(len(calls), 0)
        for field, value in [("source_sandbox_id", "foreign"), ("source_runtime_generation", 8), ("target_filesystem_id", "foreign"), ("writer_epoch", 9007199254740992), ("auto_resume", None)]:
            data = {**FIXTURE, field: value}
            with self.subTest(field=field), self.assertRaises(ValueError):
                client.sandboxes.get_rootfs_fork("source", expected_runtime_generation=7, idempotency_key="original-fork")
        self.assertEqual(len(calls), 5)
