import json
from unittest import TestCase

import httpx

from sandbox0 import Client, APIError
from sandbox0.apispec.models.credential_source_resolver_kind import CredentialSourceResolverKind
from sandbox0.apispec.models.credential_source_write_request import CredentialSourceWriteRequest
from sandbox0.apispec.models.credential_source_write_spec import CredentialSourceWriteSpec
from sandbox0.apispec.models.external_mount_binding import ExternalMountBinding
from sandbox0.apispec.models.external_mount_binding_access import ExternalMountBindingAccess
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.static_s3_source_spec import StaticS3SourceSpec


class TestExternalMounts(TestCase):
    def client(self, handler):
        client = Client(token="test", base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client

    def test_claim_and_paused_details_use_generated_binding(self):
        binding = ExternalMountBinding(source_ref="customer-data", mount_path="/data", prefix="runs/", access=ExternalMountBindingAccess.READ_WRITE)
        wire_binding = {"source_ref": "customer-data", "mount_path": "/data", "prefix": "runs/", "access": "read_write"}
        calls = []

        def handle(request):
            calls.append((request.method, request.url.path))
            if request.method == "POST":
                self.assertEqual(request.url.path, "/api/v1/sandboxes")
                self.assertEqual(json.loads(request.content), {"template": "default", "config": {"external_mounts": [wire_binding], "resources": {"memory": "1Gi"}, "auto_resume": True, "services": []}})
                return httpx.Response(201, json={"success": True, "data": {"sandbox_id": "sb_1", "template": "default", "runtime_id": "alloc", "status": "running"}})
            self.assertEqual(request.url.path, "/api/v1/sandboxes/sb_1")
            return httpx.Response(200, json={"success": True, "data": {
                "id": "sb_1", "template_id": "default", "team_id": "team", "status": "paused", "paused": True,
                "auto_resume": False, "runtime_id": "", "runtime_generation": 2, "external_mounts": [wire_binding],
                "claimed_at": "2026-10-20T00:00:00Z", "created_at": "2026-10-20T00:00:00Z", "updated_at": "2026-10-20T00:00:00Z",
            }})

        client = self.client(handle)
        config = SandboxConfig(external_mounts=[binding])
        sandbox = client.sandboxes.claim("default", config=config, memory="1Gi")
        self.assertEqual(sandbox.id, "sb_1")
        detail = client.sandboxes.get(sandbox.id)
        self.assertTrue(detail.paused)
        self.assertEqual(detail.external_mounts, [binding])
        self.assertEqual(calls, [("POST", "/api/v1/sandboxes"), ("GET", "/api/v1/sandboxes/sb_1")])
        self.assertEqual(ExternalMountBinding(source_ref="customer-data", mount_path="/data").access, ExternalMountBindingAccess.READ_ONLY)

    def test_s3_credentials_are_sent_to_source_endpoint(self):
        calls = []

        def handle(request):
            calls.append(request.url.path)
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.url.path, "/api/v1/credential-sources")
            self.assertEqual(json.loads(request.content), {
                "name": "customer-data", "resolverKind": "static_s3", "spec": {"staticS3": {
                    "bucket": "customer-bucket", "region": "us-east-1", "prefix": "agents/", "allowWrite": True,
                    "endpointUrl": "https://s3.example.test", "accessKey": "test-access", "secretKey": "test-secret", "sessionToken": "test-session",
                }},
            })
            return httpx.Response(201, json={"success": True, "data": {"name": "customer-data", "resolverKind": "static_s3", "currentVersion": 1, "status": "active"}})

        client = self.client(handle)
        metadata = client.create_credential_source(CredentialSourceWriteRequest(
            name="customer-data", resolver_kind=CredentialSourceResolverKind.STATIC_S3,
            spec=CredentialSourceWriteSpec(static_s3=StaticS3SourceSpec(
                bucket="customer-bucket", region="us-east-1", prefix="agents/", allow_write=True,
                endpoint_url="https://s3.example.test", access_key="test-access", secret_key="test-secret", session_token="test-session",
            )),
        ))
        self.assertEqual(metadata.resolver_kind, CredentialSourceResolverKind.STATIC_S3)
        self.assertNotIn("spec", metadata.to_dict())
        self.assertEqual(len(calls), 1)

    def test_claim_denial_has_no_retry_or_guest_fallback(self):
        calls = []

        def handle(request):
            calls.append(request.url.path)
            return httpx.Response(409, json={"success": False, "error": {"code": "conflict", "message": "mount unavailable"}})

        client = self.client(handle)
        with self.assertRaises(APIError):
            client.sandboxes.claim("default", config=SandboxConfig(external_mounts=[ExternalMountBinding(source_ref="customer-data", mount_path="/data")]))
        self.assertEqual(calls, ["/api/v1/sandboxes"])
