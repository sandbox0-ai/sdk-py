from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.claim_mount_request import ClaimMountRequest
from sandbox0.apispec.models.claim_response import ClaimResponse
from sandbox0.apispec.models.mount_status import MountStatus
from sandbox0.apispec.models.mount_status_state import MountStatusState
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.success_claim_response import SuccessClaimResponse
from sandbox0.apispec.types import Response
from sandbox0.resources import Sandboxes
from sandbox0.sandbox import Sandbox


class TestSandboxes(TestCase):
    def test_claim_builds_request_with_bootstrap_mounts(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        captured = {}

        def fake_sync_detailed(*, client, body):
            captured["body"] = body
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessClaimResponse(
                    success=True,
                    data=ClaimResponse(
                        sandbox_id="sb_123",
                        template="default",
                        pod_name="pod-a",
                        status="running",
                        cluster_id="cluster-a",
                        bootstrap_mounts=[
                            MountStatus(
                                sandboxvolume_id="vol_1",
                                mount_point="/workspace/data",
                                state=MountStatusState.MOUNTED,
                            )
                        ],
                    ),
                ),
            )

        with patch("sandbox0.resources.post_api_v1_sandboxes.sync_detailed", side_effect=fake_sync_detailed):
            sandbox = client.sandboxes.claim(
                "default",
                config=SandboxConfig(ttl=300),
                mounts=[ClaimMountRequest(sandboxvolume_id="vol_1", mount_point="/workspace/data")],
                wait_for_mounts=True,
                mount_wait_timeout_ms=45000,
            )

        request = captured["body"]
        self.assertEqual(request.template, "default")
        self.assertEqual(request.config.ttl, 300)
        self.assertEqual(len(request.mounts), 1)
        self.assertEqual(request.mounts[0].sandboxvolume_id, "vol_1")
        self.assertEqual(request.wait_for_mounts, True)
        self.assertEqual(request.mount_wait_timeout_ms, 45000)
        self.assertEqual(sandbox.id, "sb_123")
        self.assertEqual(sandbox.cluster_id, "cluster-a")
        self.assertEqual(len(sandbox.bootstrap_mounts), 1)
        self.assertEqual(sandbox.bootstrap_mounts[0].state, MountStatusState.MOUNTED)

    def test_open_forwards_bootstrap_mount_options(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        sandbox = Sandbox(id="sb_456", client=client)
        sandboxes = Sandboxes(client)

        with patch.object(Sandboxes, "claim", return_value=sandbox) as claim_mock:
            session = sandboxes.open(
                "default",
                config=SandboxConfig(ttl=120),
                mounts=[ClaimMountRequest(sandboxvolume_id="vol_2", mount_point="/workspace/cache")],
                wait_for_mounts=True,
                mount_wait_timeout_ms=12000,
            )

        claim_mock.assert_called_once_with(
            "default",
            config=SandboxConfig(ttl=120),
            mounts=[ClaimMountRequest(sandboxvolume_id="vol_2", mount_point="/workspace/cache")],
            wait_for_mounts=True,
            mount_wait_timeout_ms=12000,
        )
        self.assertIs(session.sandbox, sandbox)
