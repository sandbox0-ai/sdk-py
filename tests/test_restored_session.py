from unittest import TestCase
import httpx
from sandbox0 import Client
from tests.test_sandbox_sessions import _session_fixture


class TestRestoredSession(TestCase):
    def test_original_attempt_only_and_no_fallback(self):
        calls = []
        state = dict(status=200, origin=1, phase="running")
        def handler(request):
            calls.append(request)
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.url.params["runtime_generation"], "5")
            self.assertEqual(request.url.params["creation_runtime_generation"], "1")
            value = _session_fixture().to_dict()
            value.update(runtime_generation=5, phase=state["phase"], attempt=dict(id="original", number=1, runtime_generation=state["origin"]))
            return httpx.Response(state["status"], json={"success": True, "data": value} if state["status"] == 200 else {"success": False, "error": {"code": "unavailable", "message": "unavailable"}})
        client = Client(token="test", base_url="https://example.test")
        self.addCleanup(client.close)
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        sb = client.sandbox("sandbox")
        self.assertEqual(sb.find_restored_conditional_session("original", 5, 1).attempt.id, "original")
        state["origin"] = 5
        with self.assertRaises(ValueError): sb.find_restored_conditional_session("original", 5, 1)
        state.update(origin=1, phase="stopped")
        with self.assertRaises(ValueError): sb.find_restored_conditional_session("original", 5, 1)
        for code in (404, 405, 409, 503):
            state["status"] = code
            with self.assertRaises(Exception): sb.find_restored_conditional_session("original", 5, 1)
        for origin in (0, -1, True, 5, 6, 1.5):
            with self.assertRaises(ValueError): sb.find_restored_conditional_session("original", 5, origin)
        self.assertEqual(len(calls), 7)
