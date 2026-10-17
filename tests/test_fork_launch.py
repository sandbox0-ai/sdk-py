from unittest import TestCase
import json
import httpx
from sandbox0 import Client, APIError

OPTIONS = dict(fork_operation_id="fork", filesystem_id="child", head_generation_id="head", writer_epoch=7, idempotency_key="original", expected_operation_id="launch")
FIXTURE = dict(operation_id="launch", sandbox_id="child", fork_operation_id="fork", filesystem_id="child", head_generation_id="head", writer_epoch=7, lifecycle_epoch=1, runtime_generation=0, state="pending", current=True)
COMPLETED = dict(FIXTURE, runtime_generation=1, state="completed", current=False, launch_digest="a" * 64, completed_at="2026-10-17T00:00:00Z")
METHODS = ("launch_rootfs_fork", "get_rootfs_fork_launch")


class TestForkLaunch(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_original_conditions_and_outcomes(self):
        for method in METHODS:
            for status in (200, 202, 404, 409, 429, 503):
                if method == "get_rootfs_fork_launch" and status == 202:
                    continue
                with self.subTest(method=method, status=status):
                    calls = []
                    def handler(request):
                        calls.append(request)
                        self.assertEqual(request.url.path, "/api/v1/sandboxes/child/fork-launch")
                        self.assertEqual(request.headers["Idempotency-Key"], "original")
                        conditions = dict(fork_operation_id="fork", filesystem_id="child", head_generation_id="head", writer_epoch=7)
                        if method == "launch_rootfs_fork":
                            self.assertEqual(request.method, "POST")
                            self.assertEqual(json.loads(request.content), conditions)
                            self.assertEqual(request.url.query, b"")
                        else:
                            self.assertEqual(request.method, "GET")
                            self.assertEqual(request.content, b"")
                            self.assertEqual(dict(request.url.params), dict(conditions, writer_epoch="7"))
                        return httpx.Response(status, json={"success": False, "error": {"code": "retained", "message": "retain original"}} if status >= 400 else {"success": True, "data": FIXTURE if status == 202 else COMPLETED})
                    client = self.client(handler)
                    if status >= 400:
                        with self.assertRaises(APIError) as error:
                            getattr(client.sandboxes, method)("child", **OPTIONS)
                        self.assertEqual(error.exception.status_code, status)
                    else:
                        result = getattr(client.sandboxes, method)("child", **OPTIONS)
                        self.assertEqual(result.state, "pending" if status == 202 else "completed")
                        self.assertEqual(result.current, status == 202)
                    self.assertEqual(len(calls), 1)

    def test_reject_invalid_inputs_without_network(self):
        calls = []
        def handler(request):
            calls.append(request)
            return httpx.Response(200, json={"success": True, "data": FIXTURE})
        client = self.client(handler)
        for method in METHODS:
            for change in [dict(writer_epoch=0), dict(writer_epoch=True), dict(writer_epoch=1.5), dict(writer_epoch=9007199254740992), dict(fork_operation_id=""), dict(filesystem_id="bad id"), dict(head_generation_id="a" * 513), dict(idempotency_key=""), dict(idempotency_key="bad key"), dict(expected_operation_id="bad id")]:
                with self.subTest(method=method, change=change), self.assertRaises(ValueError):
                    getattr(client.sandboxes, method)("child", **dict(OPTIONS, **change))
        self.assertEqual(len(calls), 0)

    def test_reject_foreign_and_inconsistent_receipts(self):
        calls = []
        data = FIXTURE
        def handler(request):
            calls.append(request)
            return httpx.Response(200, json={"success": True, "data": data})
        client = self.client(handler)
        for method in METHODS:
            changes = [dict(sandbox_id="foreign"), dict(fork_operation_id="foreign"), dict(filesystem_id="foreign"), dict(head_generation_id="foreign"), dict(writer_epoch=8), dict(operation_id="different"), dict(lifecycle_epoch=2), dict(lifecycle_epoch=True), dict(lifecycle_epoch=1.0), dict(runtime_generation=False), dict(runtime_generation=0.0), dict(runtime_generation=1), dict(current="true"), dict(current=None), dict(state="unknown"), dict(state="aborted"), dict(launch_digest="a" * 64), dict(launch_digest=None), dict(completed_at=None), dict(completed_at="2026-10-17T00:00:00Z")]
            for change in changes:
                data = dict(FIXTURE, **change)
                with self.subTest(method=method, change=change), self.assertRaises((ValueError, TypeError)):
                    getattr(client.sandboxes, method)("child", **OPTIONS)
            for change in [dict(runtime_generation=0), dict(launch_digest=None), dict(launch_digest="bad"), dict(completed_at=None), dict(completed_at=1792195200000), dict(completed_at="2026-10-17"), dict(completed_at="invalid")]:
                data = dict(COMPLETED, **change)
                with self.subTest(method=method, change=change), self.assertRaises((ValueError, TypeError)):
                    getattr(client.sandboxes, method)("child", **OPTIONS)
            data = dict(FIXTURE, state="aborted", current=False)
            self.assertEqual(getattr(client.sandboxes, method)("child", **OPTIONS).state, "aborted")
            data = dict(FIXTURE, current=False)
            self.assertFalse(getattr(client.sandboxes, method)("child", **OPTIONS).current)
        self.assertEqual(len(calls), 58)

    def test_lost_reply_then_original_lookup(self):
        calls = []
        def handler(request):
            calls.append(request)
            if len(calls) == 1:
                self.assertEqual(request.method, "POST")
                raise httpx.ReadTimeout("lost reply", request=request)
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.url.params["writer_epoch"], "7")
            return httpx.Response(200, json={"success": True, "data": COMPLETED})
        client = self.client(handler)
        with self.assertRaises(httpx.ReadTimeout):
            client.sandboxes.launch_rootfs_fork("child", **OPTIONS)
        self.assertEqual(len(calls), 1)
        self.assertFalse(client.sandboxes.get_rootfs_fork_launch("child", **OPTIONS).current)
        self.assertEqual(len(calls), 2)

    def test_accepted_terminal_rejected(self):
        client = self.client(lambda request: httpx.Response(202, json={"success": True, "data": COMPLETED}))
        with self.assertRaises(ValueError):
            client.sandboxes.launch_rootfs_fork("child", **OPTIONS)
