import json
from unittest import TestCase

import httpx

from sandbox0 import Client
from sandbox0.errors import APIError


class TestConditionalMemoryResume(TestCase):
    def test_exact_intent_on_retry_and_completed_replay(self) -> None:
        for resource in (True, False):
            for generation in (0, 7):
                calls = []
                operation = "idem-" + "b" * 64
                def handler(request: httpx.Request) -> httpx.Response:
                    calls.append(request)
                    self.assertEqual(request.method, "POST")
                    self.assertEqual(request.url.path, "/api/v1/sandboxes/sb_1/resume")
                    self.assertEqual(request.headers["Idempotency-Key"], "resume-7")
                    self.assertEqual(json.loads(request.content), {"memory": True, "expected_runtime_generation": generation, "checkpoint_id": "capture-7"})
                    if len(calls) == 1:
                        return httpx.Response(503, json={"success": False, "error": {"code": "unavailable", "message": "restore reply uncertain"}})
                    return httpx.Response(200, json={"success": True, "data": {"sandbox_id": "sb_1", "resumed": True, "operation_id": operation,
                        "checkpoint_id": "capture-7", "from_runtime_generation": generation, "runtime_generation": generation + 1}})
                with Client(token="test-token", base_url="https://example.test") as client:
                    client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                    method = client.sandboxes.resume_memory_for_operation if resource else client.resume_sandbox_memory_for_operation
                    with self.assertRaises(APIError):
                        method("sb_1", expected_runtime_generation=generation, checkpoint_id="capture-7", idempotency_key="resume-7")
                    self.assertEqual(len(calls), 1)
                    result = method("sb_1", expected_runtime_generation=generation, checkpoint_id="capture-7", idempotency_key="resume-7")
                    self.assertTrue(result.resumed)
                    self.assertEqual(result.operation_id, operation)
                    self.assertEqual(result.from_runtime_generation, generation)
                    self.assertEqual(result.runtime_generation, generation + 1)
                    replay = method("sb_1", expected_runtime_generation=generation, checkpoint_id="capture-7", idempotency_key="resume-7")
                    self.assertEqual(result, replay)
                    self.assertEqual(len(calls), 3)

    def test_invalid_input_and_unbound_responses(self) -> None:
        calls = []
        data = {"sandbox_id": "sb_1", "resumed": True, "operation_id": "idem-" + "b" * 64, "checkpoint_id": "capture-7", "from_runtime_generation": 7, "runtime_generation": 8}
        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            return httpx.Response(200, json={"success": True, "data": data})
        with Client(token="test-token", base_url="https://example.test") as client:
            client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
            for generation in (-1, 1.5, True, "7", 9007199254740991):
                with self.assertRaises(ValueError):
                    client.sandboxes.resume_memory_for_operation("sb_1", expected_runtime_generation=generation, checkpoint_id="capture-7", idempotency_key="resume-7")
            for checkpoint in ("", " padded", "line\nbreak", "🙂", "x" * 257):
                with self.assertRaises(ValueError):
                    client.sandboxes.resume_memory_for_operation("sb_1", expected_runtime_generation=7, checkpoint_id=checkpoint, idempotency_key="resume-7")
            for key in ("", " padded", "resume/7", "x" * 256):
                with self.assertRaises(ValueError):
                    client.sandboxes.resume_memory_for_operation("sb_1", expected_runtime_generation=7, checkpoint_id="capture-7", idempotency_key=key)
            self.assertEqual(calls, [])
            for field, value in (("operation_id", None), ("operation_id", "other"), ("checkpoint_id", None), ("checkpoint_id", "other"),
                    ("from_runtime_generation", None), ("from_runtime_generation", 8), ("runtime_generation", None), ("runtime_generation", 9), ("sandbox_id", "other"), ("resumed", False), ("resumed", "true")):
                original = data[field]
                if value is None:
                    del data[field]
                else:
                    data[field] = value
                with self.assertRaises(ValueError):
                    client.sandboxes.resume_memory_for_operation("sb_1", expected_runtime_generation=7, checkpoint_id="capture-7", idempotency_key="resume-7")
                data[field] = original
            self.assertEqual(len(calls), 11)
