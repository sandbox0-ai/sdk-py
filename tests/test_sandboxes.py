from http import HTTPStatus
from contextlib import ExitStack
from datetime import datetime, timezone
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.claim_mount_request import ClaimMountRequest
from sandbox0.apispec.models.claim_response import ClaimResponse
from sandbox0.apispec.models.fork_sandbox_response import ForkSandboxResponse
from sandbox0.apispec.models.mount_status import MountStatus
from sandbox0.apispec.models.mount_status_state import MountStatusState
from sandbox0.apispec.models.restore_sandbox_root_fs_response import RestoreSandboxRootFSResponse
from sandbox0.apispec.models.restore_sandbox_root_fs_request import RestoreSandboxRootFSRequest
from sandbox0.apispec.models.sandbox import Sandbox as APISandbox
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_lifecycle_status import SandboxLifecycleStatus
from sandbox0.apispec.models.sandbox_root_fs_snapshot import SandboxRootFSSnapshot
from sandbox0.apispec.models.sandbox_root_fs_snapshot_list import SandboxRootFSSnapshotList
from sandbox0.apispec.models.success_claim_response import SuccessClaimResponse
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_fork_sandbox_response import SuccessForkSandboxResponse
from sandbox0.apispec.models.success_restore_sandbox_root_fs_response import SuccessRestoreSandboxRootFSResponse
from sandbox0.apispec.models.success_sandbox_response import SuccessSandboxResponse
from sandbox0.apispec.models.success_sandbox_root_fs_snapshot_list_response import SuccessSandboxRootFSSnapshotListResponse
from sandbox0.apispec.models.success_sandbox_root_fs_snapshot_response import SuccessSandboxRootFSSnapshotResponse
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
                memory="512Mi",
                mounts=[ClaimMountRequest(sandboxvolume_id="vol_1", mount_point="/workspace/data")],
                snapshot_id="snap_123",
            )

        request = captured["body"]
        self.assertEqual(request.template, "default")
        self.assertEqual(request.config.ttl, 300)
        self.assertEqual(request.config.resources.memory, "512Mi")
        self.assertEqual(len(request.mounts), 1)
        self.assertEqual(request.mounts[0].sandboxvolume_id, "vol_1")
        self.assertEqual(request.snapshot_id, "snap_123")
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
                snapshot_id="snap_456",
                memory="1Gi",
            )

        claim_mock.assert_called_once_with(
            "default",
            config=SandboxConfig(ttl=120),
            mounts=[ClaimMountRequest(sandboxvolume_id="vol_2", mount_point="/workspace/cache")],
            snapshot_id="snap_456",
            memory="1Gi",
        )
        self.assertIs(session.sandbox, sandbox)

    def test_update_memory_builds_request(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        now = datetime.now(timezone.utc)
        updated = APISandbox(
            id="sb_123",
            template_id="default",
            team_id="team_1",
            status=SandboxLifecycleStatus.RUNNING,
            paused=False,
            auto_resume=True,
            pod_name="pod-a",
            runtime_generation=1,
            expires_at=now,
            hard_expires_at=now,
            claimed_at=now,
            created_at=now,
            updated_at=now,
        )
        captured = {}

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessSandboxResponse(success=True, data=updated),
            )

        with patch("sandbox0.resources.put_api_v1_sandboxes_id.sync_detailed", side_effect=fake_sync_detailed):
            result = client.sandboxes.update_memory("sb_123", "2Gi")

        self.assertIs(result, updated)
        self.assertEqual(captured["id"], "sb_123")
        body = captured["body"]
        self.assertEqual(body.config.resources.memory, "2Gi")

    def test_rootfs_operations_use_generated_api(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        now = datetime.now(timezone.utc)
        snapshot = SandboxRootFSSnapshot(
            id="snap_1",
            sandbox_id="sb_1",
            created_at=now,
            name="snap",
        )
        fork_sandbox = APISandbox(
            id="sb_fork",
            template_id="default",
            team_id="team_1",
            status=SandboxLifecycleStatus.PAUSED,
            paused=True,
            auto_resume=False,
            pod_name="",
            runtime_generation=0,
            expires_at=now,
            hard_expires_at=now,
            claimed_at=now,
            created_at=now,
            updated_at=now,
        )

        captured = {}

        def response(parsed):
            return Response(status_code=HTTPStatus.OK, content=b"{}", headers={}, parsed=parsed)

        def capture_response(name, parsed):
            def fake(**kwargs):
                captured[name] = kwargs
                return response(parsed)

            return fake

        with ExitStack() as stack:
            stack.enter_context(
                patch(
                    "sandbox0.resources.post_api_v1_sandboxes_id_snapshots.sync_detailed",
                    side_effect=capture_response("create", SuccessSandboxRootFSSnapshotResponse(success=True, data=snapshot)),
                )
            )
            stack.enter_context(
                patch(
                    "sandbox0.resources.get_api_v1_sandboxes_id_snapshots.sync_detailed",
                    side_effect=capture_response(
                        "list",
                        SuccessSandboxRootFSSnapshotListResponse(
                            success=True,
                            data=SandboxRootFSSnapshotList(snapshots=[snapshot], count=1),
                        ),
                    ),
                )
            )
            stack.enter_context(
                patch(
                    "sandbox0.resources.get_api_v1_sandbox_rootfs_snapshots_snapshot_id.sync_detailed",
                    side_effect=capture_response("get", SuccessSandboxRootFSSnapshotResponse(success=True, data=snapshot)),
                )
            )
            stack.enter_context(
                patch(
                    "sandbox0.resources.delete_api_v1_sandbox_rootfs_snapshots_snapshot_id.sync_detailed",
                    side_effect=capture_response("delete", SuccessDeletedResponse(success=True)),
                )
            )
            stack.enter_context(
                patch(
                    "sandbox0.resources.post_api_v1_sandboxes_id_rootfs_restore.sync_detailed",
                    side_effect=capture_response(
                        "restore",
                        SuccessRestoreSandboxRootFSResponse(
                            success=True,
                            data=RestoreSandboxRootFSResponse(
                                sandbox_id="sb_1",
                                snapshot_id="snap_1",
                                status=SandboxLifecycleStatus.PAUSED,
                            ),
                        ),
                    ),
                )
            )
            stack.enter_context(
                patch(
                    "sandbox0.resources.post_api_v1_sandboxes_id_fork.sync_detailed",
                    side_effect=capture_response(
                        "fork",
                        SuccessForkSandboxResponse(
                            success=True,
                            data=ForkSandboxResponse(source_sandbox_id="sb_1", sandbox=fork_sandbox),
                        ),
                    ),
                )
            )
            created = client.sandboxes.create_rootfs_snapshot("sb_1")
            listed = client.sandboxes.list_rootfs_snapshots("sb_1")
            fetched = client.sandboxes.get_rootfs_snapshot("snap_1")
            deleted = client.sandboxes.delete_rootfs_snapshot("snap_1")
            restored = client.sandboxes.restore_rootfs("sb_1", request=RestoreSandboxRootFSRequest(snapshot_id="snap_1"))
            forked = client.sandboxes.fork("sb_1")

        self.assertEqual(created.id, "snap_1")
        self.assertEqual(listed[0].id, "snap_1")
        self.assertEqual(fetched.id, "snap_1")
        self.assertTrue(deleted.success)
        self.assertEqual(restored.snapshot_id, "snap_1")
        self.assertEqual(forked.sandbox.id, "sb_fork")
        self.assertEqual(captured["create"]["id"], "sb_1")
        self.assertEqual(captured["list"]["id"], "sb_1")
        self.assertEqual(captured["get"]["snapshot_id"], "snap_1")
        self.assertEqual(captured["delete"]["snapshot_id"], "snap_1")
        self.assertEqual(captured["restore"]["id"], "sb_1")
        self.assertEqual(captured["fork"]["id"], "sb_1")
