from unittest import TestCase
import httpx
from sandbox0 import Client, APIError

IDENTITY={"sandbox_id":"sandbox","runtime_generation":7,"lifecycle_epoch":8,"desired_state":"paused","managed_files_size_bytes":0,"filesystem_id":"filesystem","head_generation_id":"head","writer_epoch":9007199254740993,"base_artifact_digest":"sha256:base","source_oci_digest":"sha256:image","has_imported_filesystem":True,"active_lifecycle":False,"sandbox_created_at":"2026-10-15T00:00:00Z","filesystem_created_at":"2026-10-15T00:00:00Z","observed_at":"2026-10-15T00:00:01Z"}
class TestRootFSIdentity(TestCase):
    def client(self, handler):
        client=Client(token="test",base_url="https://example.test")
        client.api.get_httpx_client().close()
        client.api.set_httpx_client(httpx.Client(base_url="https://example.test",transport=httpx.MockTransport(handler)))
        self.addCleanup(client.close)
        return client
    def test_external_read_preserves_exact_coordinates(self):
        calls=[]
        def handler(request):
            calls.append(request)
            self.assertEqual(request.method,"GET")
            self.assertEqual(request.url.path,"/api/v1/sandboxes/sandbox/rootfs/identity")
            self.assertFalse(request.url.query)
            return httpx.Response(200,json={"success":True,"data":IDENTITY})
        result=self.client(handler).sandboxes.get_rootfs_identity("sandbox")
        self.assertEqual(result.writer_epoch,9007199254740993)
        self.assertTrue(result.has_imported_filesystem)
        self.assertEqual(len(calls),1)
    def test_malformed_identity_is_not_adopted(self):
        for change in ({"sandbox_id":"other"},{"writer_epoch":2**63},{"lifecycle_epoch":True},{"runtime_generation":0.5},{"has_imported_filesystem":"false"},{"filesystem_id":""}):
            with self.subTest(change=change):
                client=self.client(lambda request:httpx.Response(200,json={"success":True,"data":{**IDENTITY,**change}}))
                with self.assertRaises(ValueError):client.get_sandbox_rootfs_identity("sandbox")
    def test_errors_do_not_retry_or_fallback(self):
        for status in (404,409,503):
            calls=[]
            def handler(request):
                calls.append(request)
                return httpx.Response(status,json={"success":False,"error":{"code":"unavailable","message":"unavailable"}})
            with self.assertRaises(APIError):self.client(handler).get_sandbox_rootfs_identity("sandbox")
            self.assertEqual(len(calls),1)
    def test_optional_runtime_compatibility(self):
        digest="sha256:"+"a"*64
        for change,valid in (({},True),({"desired_state":"active","runtime_compatibility_digest":digest},True),
          ({"runtime_compatibility_digest":digest},False),({"desired_state":"active","runtime_compatibility_digest":"bad"},False),
          ({"desired_state":"active","runtime_compatibility_digest":digest,"active_lifecycle":True},False)):
            with self.subTest(change=change):
                client=self.client(lambda request:httpx.Response(200,json={"success":True,"data":{**IDENTITY,**change}}))
                if valid:
                    result=client.get_sandbox_rootfs_identity("sandbox")
                    if change:self.assertEqual(result.runtime_compatibility_digest,digest)
                else:
                    with self.assertRaises(ValueError):client.get_sandbox_rootfs_identity("sandbox")

    def test_retained_recovery_metadata_never_invents_live_authority(self):
        digest="sha256:"+"a"*64
        from sandbox0.apispec.types import UNSET
        for change in ({},{"retained_runtime_compatibility_digest":"bad"},{"desired_state":"paused"},{"active_lifecycle":True},{"runtime_generation":0}):
            with self.subTest(change=change):
                data={**IDENTITY,"desired_state":"active","retained_runtime_compatibility_digest":digest,**change}
                client=self.client(lambda request:httpx.Response(200,json={"success":True,"data":data}))
                if change:
                    with self.assertRaises(ValueError):client.get_sandbox_rootfs_identity("sandbox")
                else:
                    result=client.get_sandbox_rootfs_identity("sandbox")
                    self.assertEqual(result.retained_runtime_compatibility_digest,digest)
                    self.assertIs(result.runtime_compatibility_digest,UNSET)
