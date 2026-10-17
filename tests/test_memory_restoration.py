from unittest import TestCase

import httpx
from sandbox0 import Client, APIError


def step(source, target):
    return dict(operation_id=f"restore-{target}", capture_operation_id=f"capture-{source}", from_runtime_generation=source, to_runtime_generation=target, restore_id="a" * 64, managed_files_size_bytes=8388608)


def data():
    return dict(sandbox_id="sandbox", runtime_generation=5, filesystem_id="filesystem", runtime_compatibility_digest="sha256:" + "b" * 64, steps=[step(1, 3), step(3, 5)], observed_at="2026-10-15T00:00:00Z")


class TestMemoryRestoration(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_exact_read_preserves_skipped_generations_and_legacy_projection(self):
        for size in (0, 8388608):
            calls = []
            value = data()
            for entry in value["steps"]:
                entry["managed_files_size_bytes"] = size
            def handler(request):
                calls.append(request)
                self.assertEqual(request.method, "GET")
                self.assertEqual(request.url.path, "/api/v1/sandboxes/sandbox/memory-restoration")
                self.assertEqual(request.url.query, b"runtime_generation=5")
                return httpx.Response(200, json={"success": True, "data": value})
            result = self.client(handler).sandboxes.get_memory_restoration("sandbox", 5)
            self.assertEqual([(s.from_runtime_generation, s.to_runtime_generation) for s in result.steps], [(1, 3), (3, 5)])
            self.assertEqual(result.steps[0].managed_files_size_bytes, size)
            self.assertEqual(len(calls), 1)

    def test_malformed_authority(self):
        changes = [dict(sandbox_id="foreign"), dict(runtime_generation=True), dict(runtime_generation=4), dict(filesystem_id=""),
                   dict(runtime_compatibility_digest="bad"), dict(observed_at="2026-10-15T00:00:00"), dict(steps=[]),
                   dict(steps=[step(1, 3), step(4, 5)]), dict(steps=[step(1, 3)]), dict(steps=[step(5, 5)]), dict(steps=[step(0, 5)]),
                   dict(steps=[step(1, 5)] * 65)]
        changes += [dict(steps=[{**step(1, 5), **change}]) for change in (dict(restore_id="bad"), dict(operation_id=""),
                    dict(capture_operation_id=""), dict(from_runtime_generation=True), dict(to_runtime_generation=2**63),
                    dict(managed_files_size_bytes=-1), dict(managed_files_size_bytes=67108865))]
        for change in changes:
            with self.subTest(change=change):
                client = self.client(lambda request: httpx.Response(200, json={"success": True, "data": {**data(), **change}}))
                with self.assertRaises(ValueError):
                    client.get_sandbox_memory_restoration("sandbox", 5)

    def test_input_validation_and_no_retry(self):
        def unexpected(request):
            self.fail("unexpected I/O")
        client = self.client(unexpected)
        for generation in (0, -1, True, 1.5, 2**63):
            with self.assertRaises(ValueError):
                client.get_sandbox_memory_restoration("sandbox", generation)
        for sandbox in ("", "..", "a/b", "a?b"):
            with self.assertRaises(ValueError):
                client.get_sandbox_memory_restoration(sandbox, 5)
        for status in (404, 409, 503):
            calls = []
            def handler(request):
                calls.append(request)
                return httpx.Response(status, json={"success": False, "error": {"code": "unavailable", "message": "unavailable"}})
            with self.assertRaises(APIError):
                self.client(handler).get_sandbox_memory_restoration("sandbox", 5)
            self.assertEqual(len(calls), 1)
