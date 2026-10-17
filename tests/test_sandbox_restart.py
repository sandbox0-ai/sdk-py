import json
from unittest import TestCase
import httpx
from sandbox0 import Client, APIError

OPERATION = "40ea02de-5ef4-4710-a742-c9854cdfb6ce"
RECEIPT = {"id": OPERATION, "sandbox_id": "sandbox", "request_key": "retry-key", "from_runtime_generation": 7, "state": "pausing", "created_at": "2026-10-15T00:00:00Z", "updated_at": "2026-10-15T00:00:00Z"}

class TestSandboxRestart(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_exact_routes_and_read_only_receipt_recovery(self):
        calls = []
        def handler(request):
            calls.append(request)
            if request.method == "POST":
                self.assertEqual(request.headers["Idempotency-Key"], "retry-key")
                self.assertEqual(json.loads(request.content), {"expected_runtime_generation": 7})
            data = RECEIPT if len(calls) == 1 else {**RECEIPT, "state": "succeeded", "result_runtime_generation": 8}
            return httpx.Response(202 if len(calls) == 1 else 200, json={"success": True, "data": data})
        client = self.client(handler)
        self.assertEqual(client.sandboxes.restart("sandbox", expected_runtime_generation=7, idempotency_key="retry-key").state, "pausing")
        self.assertEqual(client.sandboxes.find_restart_operation("sandbox", "retry-key").result_runtime_generation, 8)
        self.assertEqual(client.sandboxes.get_restart_operation("sandbox", OPERATION).state, "succeeded")
        self.assertEqual([(r.method, r.url.path) for r in calls], [("POST", "/api/v1/sandboxes/sandbox/restart"), ("GET", "/api/v1/sandboxes/sandbox/restart-operations"), ("GET", f"/api/v1/sandboxes/sandbox/restart-operations/{OPERATION}")])
        self.assertEqual(calls[1].url.params["request_key"], "retry-key")

    def test_errors_never_replay_or_fallback(self):
        for status in (404, 409, 503):
            calls = []
            def handler(request):
                calls.append(request)
                return httpx.Response(status, json={"success": False, "error": {"code": "unavailable", "message": "unavailable"}})
            client = self.client(handler)
            with self.assertRaises(APIError):
                client.restart_sandbox("sandbox", expected_runtime_generation=7, idempotency_key="retry-key")
            self.assertEqual(len(calls), 1)

    def test_invalid_inputs_do_not_reach_transport(self):
        def handler(request):
            self.fail("invalid input reached transport")
        client = self.client(handler)
        for generation in (-1, True, 1.5, 2**63-1, 2**63):
            with self.assertRaises(ValueError):
                client.restart_sandbox("sandbox", expected_runtime_generation=generation, idempotency_key="retry-key")
        for key in ("", " spaced", "x"*256):
            with self.assertRaises(ValueError):
                client.restart_sandbox("sandbox", expected_runtime_generation=7, idempotency_key=key)
            with self.assertRaises(ValueError):
                client.find_sandbox_restart_operation("sandbox", key)
        with self.assertRaises(ValueError):
            client.get_sandbox_restart_operation("sandbox", "not-an-operation")

    def test_invalid_receipts_are_rejected(self):
        for change in ({"sandbox_id": "foreign"}, {"request_key": "wrong"}, {"from_runtime_generation": 8}, {"state": "succeeded"}, {"state": "succeeded", "result_runtime_generation": 9}, {"result_runtime_generation": 8}, {"state": "unknown"}):
            def handler(request):
                return httpx.Response(202, json={"success": True, "data": {**RECEIPT, **change}})
            with self.assertRaises(ValueError):
                self.client(handler).restart_sandbox("sandbox", expected_runtime_generation=7, idempotency_key="retry-key")

    def test_exact_int64_generation_and_zero(self):
        for generation in (0, 2**63-2):
            def handler(request):
                self.assertEqual(json.loads(request.content)["expected_runtime_generation"], generation)
                return httpx.Response(200, json={"success": True, "data": {**RECEIPT, "from_runtime_generation": generation, "state": "succeeded", "result_runtime_generation": generation+1}})
            result = self.client(handler).restart_sandbox("sandbox", expected_runtime_generation=generation, idempotency_key="retry-key")
            self.assertEqual(result.result_runtime_generation, generation+1)

    def test_storage_diagnostic_decodes_without_completion(self):
        def handler(request):
            return httpx.Response(200, json={"success": True, "data": {**RECEIPT, "state": "resuming", "retry": {"attempts": 3, "observed_stage": "resuming", "blocked_reason": "storage_not_writable"}}})
        result = self.client(handler).sandboxes.get_restart_operation("sandbox", OPERATION)
        self.assertEqual(result.retry.blocked_reason, "storage_not_writable")
        self.assertFalse(result.result_runtime_generation)
