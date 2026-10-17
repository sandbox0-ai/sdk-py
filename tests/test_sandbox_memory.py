import json
from unittest import TestCase

import httpx

from sandbox0 import Client
from sandbox0.errors import APIError
from sandbox0.apispec.models.fork_sandbox_request import ForkSandboxRequest
from sandbox0.apispec.models.fork_sandbox_config import ForkSandboxConfig
from sandbox0.apispec.types import UNSET


class TestMemoryLifecycle(TestCase):
    def test_conditional_fork_keeps_zero_generation_and_rejects_invalid_input(self) -> None:
        requests=[]
        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            self.assertEqual(json.loads(request.content), {"memory":False,"expected_runtime_generation":0})
            self.assertEqual(request.headers["Idempotency-Key"],"fork-generation-zero")
            return httpx.Response(503,json={"success":False,"error":{"code":"unavailable","message":"pending"}})
        with Client(token="test-token",base_url="https://example.test") as client:
            client.api.set_httpx_client(httpx.Client(base_url="https://example.test",transport=httpx.MockTransport(handler)))
            with self.assertRaises(ValueError): client.sandboxes.fork("source",ForkSandboxRequest(expected_runtime_generation=0))
            for generation in (-1,1.5,True,None,9007199254740992):
                with self.assertRaises(ValueError): client.sandboxes.fork("source",ForkSandboxRequest(expected_runtime_generation=generation),idempotency_key="key")
            with self.assertRaises(ValueError): client.sandboxes.fork("source",ForkSandboxRequest(memory=True,expected_runtime_generation=9007199254740991),idempotency_key="key")
            self.assertEqual(len(requests),0)
            for _ in range(2):
                with self.assertRaises(APIError): client.sandboxes.fork("source",ForkSandboxRequest(expected_runtime_generation=0),idempotency_key="fork-generation-zero")
        self.assertEqual(len(requests),2)

    def test_fork_wake_override_uses_generated_wire_contract(self) -> None:
        for auto_resume in (UNSET, False, True):
            with self.subTest(auto_resume=auto_resume):
                requests = []
                def handler(request: httpx.Request) -> httpx.Response:
                    requests.append(request)
                    self.assertEqual(json.loads(request.content), {"memory": False, "config": {} if auto_resume is UNSET else {"auto_resume": auto_resume}})
                    self.assertEqual(request.headers["Idempotency-Key"], "fork-wake-policy")
                    return httpx.Response(409, json={"success": False, "error": {"code": "conflict", "message": "fixture stops after request serialization"}})
                with Client(token="test-token", base_url="https://example.test") as client:
                    client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                    with self.assertRaises(APIError):
                        client.sandboxes.fork("sb_1", ForkSandboxRequest(config=ForkSandboxConfig(auto_resume=auto_resume)), idempotency_key="fork-wake-policy")
                self.assertEqual(len(requests), 1)

    def test_explicit_memory_and_defaults_use_generated_wire_contract(self) -> None:
        for action in ("pause", "resume"):
            for memory in (False, True):
                for resource in (False, True):
                    with self.subTest(action=action, memory=memory, resource=resource):
                        requests = []
                        def handler(request: httpx.Request) -> httpx.Response:
                            requests.append(request)
                            self.assertEqual(json.loads(request.content), {"memory": memory})
                            self.assertEqual(request.url.path, f"/api/v1/sandboxes/sb_1/{action}")
                            return httpx.Response(200, json={"success": True, "data": {"sandbox_id": "sb_1", "paused": True, "status": "paused", "resumed": True}})
                        with Client(token="test-token", base_url="https://example.test") as client:
                            client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                            method = getattr(client.sandboxes, action) if resource else getattr(client, action + "_sandbox")
                            if memory:
                                method("sb_1", memory=True)
                            else:
                                method("sb_1")
                        self.assertEqual(len(requests), 1)

    def test_memory_failure_never_retries_filesystem_mode(self) -> None:
        for action in ("pause", "resume"):
            calls = []
            def handler(request: httpx.Request) -> httpx.Response:
                calls.append(json.loads(request.content))
                return httpx.Response(503, json={"success": False, "error": {"code": "unavailable", "message": "memory unavailable"}})
            with Client(token="test-token", base_url="https://example.test") as client:
                client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                with self.assertRaises(APIError) as error:
                    getattr(client.sandboxes, action)("sb_1", memory=True)
                self.assertEqual(error.exception.status_code, 503)
            self.assertEqual(calls, [{"memory": True}])

    def test_memory_fork_requires_stable_key_for_caller_retry(self) -> None:
        calls = []
        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            self.assertEqual(request.headers["Idempotency-Key"], "fork-one")
            self.assertEqual(json.loads(request.content), {"memory": True})
            return httpx.Response(503, json={"success": False, "error": {"code": "unavailable", "message": "capture pending"}})
        with Client(token="test-token", base_url="https://example.test") as client:
            client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
            request = ForkSandboxRequest(memory=True)
            with self.assertRaises(ValueError):
                client.sandboxes.fork("sb_1", request)
            self.assertEqual(calls, [])
            for _ in range(2):
                with self.assertRaises(APIError):
                    client.sandboxes.fork("sb_1", request, idempotency_key="fork-one")
        self.assertEqual(len(calls), 2)
