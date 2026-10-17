from unittest import TestCase
import httpx
from sandbox0 import Client
from sandbox0.errors import APIError

OPERATION = "idem-" + "b" * 64
BASE = dict(sandbox_id="sb_1", action="pause", operation_id=OPERATION, checkpoint_id=OPERATION,
            from_runtime_generation=7, lifecycle_epoch=3, state="canceled", reason="before_capture", current=True)
INPUT = dict(action="pause", expected_runtime_generation=7, idempotency_key="pause-7", expected_operation_id=OPERATION)


class TestMemoryOperation(TestCase):
    def test_read_only_exact_requests_and_terminal_states(self):
        for resource in (True, False):
            for action in ("pause", "resume"):
                for state in ("pending", "completed", "canceled", "failed"):
                    for current in (False, True):
                        if current and (state == "pending" or (action == "pause" and state == "failed")):
                            continue
                        data = dict(BASE, action=action, state=state, current=current)
                        data.pop("reason")
                        if action == "resume":
                            data["checkpoint_id"] = "capture-7"
                        if state == "canceled":
                            data["reason"] = "before_capture" if action == "pause" else "before_restore"
                        if state == "failed":
                            data["reason"] = "capture_failed" if action == "pause" else "restore_failed"
                        if action == "resume" and state in ("completed", "failed"):
                            data["result_runtime_generation"] = 8
                        calls = []
                        def handler(request):
                            calls.append(request)
                            self.assertEqual(request.method, "GET")
                            self.assertEqual(request.content, b"")
                            self.assertEqual(request.url.path, "/api/v1/sandboxes/sb_1/memory-operations/lookup")
                            self.assertEqual(request.headers["Idempotency-Key"], "pause-7")
                            self.assertEqual(dict(request.url.params), dict(action=action, expected_runtime_generation="7", **({"checkpoint_id": "capture-7"} if action == "resume" else {})))
                            return httpx.Response(200, json={"success": True, "data": data})
                        with Client(token="test-token", base_url="https://example.test") as client:
                            client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                            method = client.sandboxes.lookup_memory_operation if resource else client.lookup_sandbox_memory_operation
                            result = method("sb_1", **dict(INPUT, action=action, checkpoint_id="capture-7" if action == "resume" else None))
                            self.assertEqual(result.state, state)
                            self.assertEqual(result.current, current)
                            self.assertEqual(len(calls), 1)

    def test_unbound_or_contradictory_evidence(self):
        changes = [dict(sandbox_id="other"), dict(action="resume"), dict(operation_id="idem-" + "c" * 64), dict(checkpoint_id="other"),
                   dict(from_runtime_generation=8), dict(from_runtime_generation=True), dict(lifecycle_epoch=0), dict(lifecycle_epoch=True),
                   dict(current="true"), dict(reason="before_restore"), dict(reason=None), dict(result_runtime_generation=None),
                   dict(result_runtime_generation=8), dict(state="pending"), dict(state="completed"), dict(state="failed", reason="capture_failed")]
        for change in changes:
            calls = []
            def handler(request):
                calls.append(request)
                return httpx.Response(200, json={"success": True, "data": dict(BASE, **change)})
            with Client(token="test-token", base_url="https://example.test") as client:
                client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                with self.assertRaises(ValueError):
                    client.sandboxes.lookup_memory_operation("sb_1", **INPUT)
                self.assertEqual(len(calls), 1)

    def test_invalid_input_and_errors_never_dispatch(self):
        calls = []
        status = 404
        def handler(request):
            calls.append(request)
            return httpx.Response(status, json={"success": False, "error": {"code": "unavailable", "message": "no proof"}})
        with Client(token="test-token", base_url="https://example.test") as client:
            client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
            for change in [dict(action="other"), dict(expected_runtime_generation=True), dict(expected_runtime_generation=0),
                           dict(expected_runtime_generation=1.5), dict(idempotency_key="bad/key"), dict(checkpoint_id="forbidden"),
                           dict(expected_operation_id="bad"), dict(action="resume"), dict(action="resume", checkpoint_id="capture", expected_runtime_generation=9007199254740991)]:
                with self.assertRaises(ValueError):
                    client.sandboxes.lookup_memory_operation("sb_1", **dict(INPUT, **change))
            self.assertEqual(calls, [])
            for status in (404, 409, 503):
                with self.assertRaises(APIError):
                    client.sandboxes.lookup_memory_operation("sb_1", **INPUT)
            self.assertEqual(len(calls), 3)
