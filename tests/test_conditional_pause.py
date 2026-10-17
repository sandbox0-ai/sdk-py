import json
from unittest import TestCase

import httpx

from sandbox0 import Client
from sandbox0.errors import APIError


class TestConditionalMemoryPause(TestCase):
    def test_stable_intent_after_uncertain_reply(self) -> None:
        for resource in (True, False):
            calls = []
            operation = "idem-" + "a" * 64
            def handler(request: httpx.Request) -> httpx.Response:
                calls.append(request)
                self.assertEqual(request.url.path, "/api/v1/sandboxes/sb_1/pause")
                self.assertEqual(request.headers["Idempotency-Key"], "pause-7")
                self.assertEqual(json.loads(request.content), {"memory": True, "expected_runtime_generation": 7})
                if len(calls) == 1:
                    return httpx.Response(503, json={"success": False, "error": {"code": "unavailable", "message": "reply uncertain"}})
                return httpx.Response(202 if len(calls) == 2 else 200, json={"success": True, "data": {
                    "sandbox_id": "sb_1", "paused": len(calls) == 3, "runtime_generation": 7, "operation_id": operation}})
            with Client(token="test-token", base_url="https://example.test") as client:
                client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                method = client.sandboxes.pause_memory_for_operation if resource else client.pause_sandbox_memory_for_operation
                with self.assertRaises(APIError):
                    method("sb_1", expected_runtime_generation=7, idempotency_key="pause-7")
                self.assertEqual(len(calls), 1)
                pending = method("sb_1", expected_runtime_generation=7, idempotency_key="pause-7")
                self.assertFalse(pending.paused)
                self.assertEqual(pending.operation_id, operation)
                complete = method("sb_1", expected_runtime_generation=7, idempotency_key="pause-7")
                self.assertTrue(complete.paused)
                self.assertEqual(complete.operation_id, pending.operation_id)
                self.assertEqual(len(calls), 3)

    def test_invalid_input_and_unbound_responses(self) -> None:
        calls = []
        data = {"sandbox_id": "sb_1", "paused": True, "runtime_generation": 7, "operation_id": "idem-" + "a" * 64}
        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            return httpx.Response(200, json={"success": True, "data": data})
        with Client(token="test-token", base_url="https://example.test") as client:
            client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
            for generation in (0, -1, 1.5, True, "7", 9007199254740992):
                with self.assertRaises(ValueError):
                    client.sandboxes.pause_memory_for_operation("sb_1", expected_runtime_generation=generation, idempotency_key="pause-7")
            for key in ("", " pause-7", "pause/7", "x" * 256):
                with self.assertRaises(ValueError):
                    client.sandboxes.pause_memory_for_operation("sb_1", expected_runtime_generation=7, idempotency_key=key)
            self.assertEqual(calls, [])
            for field, value in (("operation_id", None), ("operation_id", "other"), ("runtime_generation", None), ("runtime_generation", 8), ("sandbox_id", "other"), ("paused", "true")):
                original = data[field]
                if value is None:
                    del data[field]
                else:
                    data[field] = value
                with self.assertRaises(ValueError):
                    client.sandboxes.pause_memory_for_operation("sb_1", expected_runtime_generation=7, idempotency_key="pause-7")
                data[field] = original
            self.assertEqual(len(calls), 6)
