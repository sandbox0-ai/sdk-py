import json
from unittest import TestCase

import httpx

from sandbox0 import APIError, Client


STATE = {"runtime_generation": 7, "mutation_sequence": "9007199254740993", "size_bytes": 8 << 20, "guest_path": "/run/sandbox0/credentials"}


class TestManagedFiles(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_exact_routes_binary_content_and_uint64_sequence(self):
        for namespace in (None, "codex"):
            with self.subTest(namespace=namespace):
                calls = []

                def handler(request):
                    calls.append(request)
                    self.assertEqual(request.url.params["runtime_generation"], "7")
                    return httpx.Response(200, json={"success": True, "data": {**STATE, "content": "AP+ACg=="}})

                files = self.client(handler).sandbox("sb_123").managed_files(runtime_generation=7, namespace=namespace)
                state = files.inspect()
                files.write("auth.json", b"\x00\xff\x80\x0a", expected_mutation_sequence=state.mutation_sequence)
                result = files.read("auth.json")
                self.assertEqual(result.content, b"\x00\xff\x80\x0a")
                self.assertEqual(result.state.mutation_sequence, "9007199254740993")
                self.assertNotIn("content", result.state.additional_properties)
                files.delete("auth.json", expected_mutation_sequence="18446744073709551615")
                root = "/api/v1/sandboxes/sb_123/managed-files"
                path = f"/api/v1/sandboxes/sb_123/managed-file-namespaces/{namespace}/auth.json" if namespace else root + "/auth.json"
                self.assertEqual([(r.method, r.url.path) for r in calls], [("GET", root), ("PUT", path), ("GET", path), ("DELETE", path)])
                self.assertEqual(json.loads(calls[1].content), {"content": "AP+ACg==", "expected_mutation_sequence": "9007199254740993"})
                self.assertEqual(calls[3].url.params["expected_mutation_sequence"], "18446744073709551615")

    def test_ambiguous_mutations_never_retry_resume_or_fall_back(self):
        for status in (404, 409, 503):
            with self.subTest(status=status):
                calls = []

                def handler(request):
                    calls.append(request)
                    self.assertEqual(request.method, "PUT")
                    self.assertIn("managed-file-namespaces/codex/auth.json", request.url.path)
                    self.assertEqual(json.loads(request.content)["content"], "")
                    return httpx.Response(status, json={"success": False, "error": {"code": "unavailable", "message": "unavailable"}})

                files = self.client(handler).sandbox("sb_123").managed_files(runtime_generation=7, namespace="codex")
                with self.assertRaises(APIError) as raised:
                    files.write("auth.json", b"", expected_mutation_sequence="0")
                self.assertEqual(raised.exception.status_code, status)
                self.assertEqual(len(calls), 1)

    def test_invalid_inputs_do_not_reach_transport(self):
        def handler(request):
            self.fail("invalid request reached transport")

        sandbox = self.client(handler).sandbox("sb_123")
        for generation in (0, -1, True, 1.5, 1 << 63):
            with self.assertRaises(ValueError):
                sandbox.managed_files(runtime_generation=generation)
        files = sandbox.managed_files(runtime_generation=7)
        for name in ("", "../auth", "a/b", "auth?x", ".", "..", ".s0-write-hidden", "é"):
            with self.assertRaises(ValueError):
                sandbox.managed_files(runtime_generation=7, namespace=name)
            with self.assertRaises(ValueError):
                files.read(name)
        for sequence in ("01", "-1", "18446744073709551616", 1):
            with self.assertRaises(ValueError):
                files.write("auth.json", b"", expected_mutation_sequence=sequence)
        with self.assertRaises(ValueError):
            files.write("auth.json", bytes((4 << 20) + 1), expected_mutation_sequence="0")

    def test_invalid_response_is_rejected_without_disclosing_content(self):
        for data in ({**STATE, "runtime_generation": 8, "content": ""}, {**STATE, "content": "private-invalid-base64"}):
            files = self.client(lambda _: httpx.Response(200, json={"success": True, "data": data})).sandbox("sb_123").managed_files(runtime_generation=7)
            with self.assertRaises(ValueError) as raised:
                files.read("auth.json")
            self.assertNotIn("private-invalid-base64", str(raised.exception))
