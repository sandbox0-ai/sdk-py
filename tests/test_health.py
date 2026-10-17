from copy import deepcopy
from unittest import TestCase

import httpx

from sandbox0 import APIError, Client


def observation(state, reason, source):
    return {"state": state, "reason": reason, "source": source,
            "observed_at": None if source == "none" else "2026-10-15T00:00:01Z"}


HEALTH = {
    "sandbox_id": "sandbox", "runtime_generation": 9007199254740993, "lifecycle_epoch": 8,
    "desired_state": "active", "active_lifecycle": False, "observed_at": "2026-10-15T00:00:02Z",
    "runtime": {"launch_authority": observation("available", "external_launch_authority_present", "regional_authority"),
                "liveness": observation("available", "runsc_running", "node_runtime")},
    "execution": observation("unavailable", "command_start_failed", "guest_diagnostic"),
    "terminal": observation("unknown", "guest_diagnostics_unavailable", "none"),
    "storage": {"identity": observation("available", "rootfs_identity_present", "regional_authority"),
                "writer_authority": observation("available", "current_writer_lease_present", "regional_authority"),
                "io": observation("unknown", "storage_io_unobserved", "none")},
}


class TestSandboxHealth(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_independent_observations_preserve_exact_generation(self):
        calls = []
        def handler(request):
            calls.append(request)
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.url.path, "/api/v1/sandboxes/sandbox/health")
            self.assertFalse(request.url.query)
            self.assertFalse(request.content)
            return httpx.Response(200, json={"success": True, "data": HEALTH})
        health = self.client(handler).sandboxes.get_health("sandbox")
        self.assertEqual(health.runtime_generation, 9007199254740993)
        self.assertEqual(health.runtime.liveness.state, "available")
        self.assertEqual(health.execution.state, "unavailable")
        self.assertEqual(health.terminal.state, "unknown")
        self.assertIsNone(health.terminal.observed_at)
        self.assertEqual(health.storage.io.state, "unknown")
        self.assertNotEqual(health.execution.observed_at, health.observed_at)
        self.assertEqual(len(calls), 1)

    def test_invalid_observations_are_rejected(self):
        changes = [("sandbox_id", "foreign"), ("runtime_generation", 2**63),
                   ("runtime_generation", True), ("lifecycle_epoch", 0.5), ("active_lifecycle", "false"),
                   ("desired_state", "ready"), ("observed_at", None), ("observed_at", "2026-10-15"),
                   ("execution.state", "healthy"), ("execution.reason", "private backend error"),
                   ("execution.source", "guest"), ("execution.observed_at", None),
                   ("execution.observed_at", 0), ("execution.observed_at", "invalid"),
                   ("execution.observed_at", "2026-10-15T00:00:01"),
                   ("terminal.observed_at", "2026-10-15T00:00:01Z"), ("terminal.state", "available")]
        for path, value in changes:
            with self.subTest(path=path, value=value):
                data = deepcopy(HEALTH)
                target = data
                parts = path.split(".")
                for part in parts[:-1]: target = target[part]
                target[parts[-1]] = value
                client = self.client(lambda request: httpx.Response(200, json={"success": True, "data": data}))
                with self.assertRaises((ValueError, TypeError, KeyError)):
                    client.get_sandbox_health("sandbox")
        data = deepcopy(HEALTH)
        del data["terminal"]["observed_at"]
        client = self.client(lambda request: httpx.Response(200, json={"success": True, "data": data}))
        with self.assertRaises(KeyError): client.get_sandbox_health("sandbox")

    def test_no_retry_or_lifecycle_fallback(self):
        for status in (401, 403, 404, 503):
            calls = []
            def handler(request):
                calls.append(request)
                return httpx.Response(status, json={"success": False, "error": {"code": "unavailable", "message": "unavailable"}})
            client = self.client(handler)
            with self.assertRaises(APIError): client.get_sandbox_health("sandbox")
            for invalid in ("", " sandbox", "sandbox "):
                with self.assertRaises(ValueError): client.get_sandbox_health(invalid)
            self.assertEqual(len(calls), 1)
