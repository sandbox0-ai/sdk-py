import json
from unittest import TestCase
import httpx
from sandbox0 import Client, APIError

OP = "40ea02de-5ef4-4710-a742-c9854cdfb6ce"
CAP = "a" * 64
STATUS = dict(operation_id=OP, sandbox_id="sandbox", from_runtime_generation=7, state="stopped", capture_id=CAP, stopped_at="2026-10-15T00:00:00Z")
FILE = dict(operation_id=OP, capture_id=CAP, runtime_generation=7, mutation_sequence="18446744073709551615", size_bytes=8388608, found=True, content="eA==")
PREFIX = f"/api/v1/sandboxes/sandbox/snapshot-restore-operations/{OP}/final-capture"


class TestSnapshotRestoreFinalCapture(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_identity_routes_and_receipt_replay(self):
        calls = []
        def handler(request):
            calls.append((request.method, request.url.path))
            data = STATUS
            if request.url.path.endswith("/auth.json"):
                self.assertEqual(request.url.params["capture_id"], CAP)
                data = FILE
            elif request.method == "POST":
                self.assertEqual(json.loads(request.content), dict(capture_id=CAP, receipt_id="receipt-1"))
                data = {**STATUS, "state": "acknowledged", "receipt_id": "receipt-1"}
            return httpx.Response(200, json=dict(success=True, data=data))
        client = self.client(handler)
        self.assertEqual(client.sandboxes.get_snapshot_restore_final_capture("sandbox", OP).state, "stopped")
        result = client.sandboxes.read_snapshot_restore_final_capture_file("sandbox", OP, CAP, "native", "auth.json")
        self.assertEqual(result.content, b"x")
        self.assertNotIn("content=", repr(result))
        for _ in range(2):
            self.assertEqual(client.sandboxes.acknowledge_snapshot_restore_final_capture("sandbox", OP, CAP, "receipt-1").receipt_id, "receipt-1")
        self.assertEqual(calls, [("GET", PREFIX), ("GET", PREFIX + "/namespaces/native/auth.json"), ("POST", PREFIX + "/acknowledgement"), ("POST", PREFIX + "/acknowledgement")])

    def test_empty_file_is_distinct_from_absence(self):
        for found in (True, False):
            client = self.client(lambda _: httpx.Response(200, json=dict(success=True, data={**FILE, "found": found, "content": ""})))
            result = client.read_sandbox_snapshot_restore_final_capture_file("sandbox", OP, CAP, "native", "auth.json")
            self.assertIs(result.found, found)
            self.assertEqual(result.content, b"")

    def test_errors_never_retry_or_imply_logout(self):
        for status in (404, 409, 503):
            calls = []
            def handler(request):
                calls.append(request)
                return httpx.Response(status, json=dict(success=False, error=dict(code="unavailable", message="unavailable")))
            client = self.client(handler)
            with self.assertRaises(APIError):
                client.read_sandbox_snapshot_restore_final_capture_file("sandbox", OP, CAP, "native", "auth.json")
            with self.assertRaises(APIError):
                client.acknowledge_sandbox_snapshot_restore_final_capture("sandbox", OP, CAP, "receipt-1")
            self.assertEqual(len(calls), 2)

    def test_invalid_responses_fail_closed(self):
        for change in ({"capture_id": "b"*64}, {"operation_id": "foreign"}, {"runtime_generation": True}, {"runtime_generation": 0}, {"mutation_sequence": "18446744073709551616"}, {"size_bytes": 0}, {"found": "false"}, {"found": False}, {"content": "eB=="}, {"content": "private-invalid"}):
            client = self.client(lambda _: httpx.Response(200, json=dict(success=True, data={**FILE, **change})))
            with self.assertRaises(ValueError) as error:
                client.read_sandbox_snapshot_restore_final_capture_file("sandbox", OP, CAP, "native", "auth.json")
            self.assertNotIn("private-invalid", str(error.exception))
        for change in ({"sandbox_id": "foreign"}, {"state": "pending"}, {"capture_id": None}, {"stopped_at": "2026-10-15T00:00:00"}, {"state": "acknowledged"}, {"receipt_id": "premature"}):
            client = self.client(lambda _: httpx.Response(200, json=dict(success=True, data={**STATUS, **change})))
            with self.assertRaises(ValueError):
                client.get_sandbox_snapshot_restore_final_capture("sandbox", OP)
        client = self.client(lambda _: httpx.Response(200, json=dict(success=True, data={**STATUS, "state": "acknowledged", "receipt_id": "changed"})))
        with self.assertRaises(ValueError):
            client.acknowledge_sandbox_snapshot_restore_final_capture("sandbox", OP, CAP, "receipt-1")

    def test_invalid_inputs_never_dispatch(self):
        client = self.client(lambda _: self.fail("invalid input reached transport"))
        for capture in (None, "", "A"*64):
            with self.assertRaises(ValueError):
                client.read_sandbox_snapshot_restore_final_capture_file("sandbox", OP, capture, "native", "auth.json")
            with self.assertRaises(ValueError):
                client.acknowledge_sandbox_snapshot_restore_final_capture("sandbox", OP, capture, "receipt-1")
        for namespace in ("..", "a/b", ".s0-write-secret", ""):
            with self.assertRaises(ValueError):
                client.read_sandbox_snapshot_restore_final_capture_file("sandbox", OP, CAP, namespace, "auth.json")
        with self.assertRaises(ValueError):
            client.get_sandbox_snapshot_restore_final_capture("..", OP)
        with self.assertRaises(ValueError):
            client.acknowledge_sandbox_snapshot_restore_final_capture("sandbox", OP, CAP, "")
