import unittest

from sandbox0.apispec.models.claim_mount_request import ClaimMountRequest
from sandbox0.apispec.models.create_sandbox_root_fs_snapshot_request import CreateSandboxRootFSSnapshotRequest
from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest
from sandbox0.apispec.models.mount_status_state import MountStatusState
from sandbox0.apispec.models.restore_sandbox_root_fs_request import RestoreSandboxRootFSRequest
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_config_env_vars import SandboxConfigEnvVars
from sandbox0.apispec.models.sandbox_lifecycle_status import SandboxLifecycleStatus
from sandbox0.apispec.models.sandbox_update_config import SandboxUpdateConfig
from sandbox0.apispec.models.sandbox_update_request import SandboxUpdateRequest
from sandbox0.apispec.models.sandbox_network_policy import SandboxNetworkPolicy
from sandbox0.apispec.models.sandbox_network_policy_mode import SandboxNetworkPolicyMode
from sandbox0.apispec.models.webhook_config import WebhookConfig
from sandbox0.sessions import SandboxSession

from tests.e2e.helpers import claim_sandbox, close_client, new_client, require_config


class TestSandboxes(unittest.TestCase):
    def test_sandbox_lifecycle(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        env_vars = SandboxConfigEnvVars()
        env_vars.additional_properties["SDK_PY_E2E"] = "true"
        config = SandboxConfig(
            env_vars=env_vars,
            ttl=300,
            hard_ttl=600,
            auto_resume=True,
            network=SandboxNetworkPolicy(mode=SandboxNetworkPolicyMode.ALLOW_ALL),
            webhook=WebhookConfig(url="https://example.com/webhook", secret="secret", watch_dir="/workspace"),
        )

        sandbox = claim_sandbox(self, client, cfg, config=config)

        fetched = client.sandboxes.get(sandbox.id)
        self.assertEqual(fetched.id, sandbox.id)

        status = client.sandboxes.status(sandbox.id)
        self.assertEqual(status.sandbox_id, sandbox.id)

        updated = client.sandboxes.update(
            sandbox.id,
            SandboxUpdateRequest(config=SandboxUpdateConfig(auto_resume=False)),
        )
        self.assertFalse(updated.auto_resume)

        paused = client.sandboxes.pause(sandbox.id)
        self.assertTrue(paused.paused)

        resumed = client.sandboxes.resume(sandbox.id)
        self.assertTrue(resumed.resumed)

        refresh = client.sandboxes.refresh(sandbox.id)
        self.assertEqual(refresh.sandbox_id, sandbox.id)
        self.assertEqual(client.sandboxes.sandbox("sandbox-id").id, "sandbox-id")

    def test_sandbox_open_session(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        with client.sandboxes.open(cfg.template) as sandbox:
            self.assertTrue(sandbox.id)

        session = client.sandboxes.open(cfg.template)
        self.assertIsInstance(session, SandboxSession)
        sandbox = session.sandbox
        self.assertTrue(sandbox.id)
        session.close()

    def test_claim_sandbox_with_bootstrap_mounts(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        volume = client.volumes.create(CreateSandboxVolumeRequest())
        self.addCleanup(lambda: self._delete_volume(client, volume.id))
        client.volumes.write_file(volume.id, "/claim-bootstrap/hello.txt", b"hello bootstrap claim mount")

        sandbox = client.sandboxes.claim(
            cfg.template,
            mounts=[ClaimMountRequest(sandboxvolume_id=volume.id, mount_point="/workspace/bootstrap-data")],
        )
        self.addCleanup(lambda: self._delete_sandbox(client, sandbox.id))

        self.assertTrue(sandbox.bootstrap_mounts)
        self.assertEqual(sandbox.bootstrap_mounts[0].state, MountStatusState.MOUNTED)

        content = sandbox.read_file("/workspace/bootstrap-data/claim-bootstrap/hello.txt")
        self.assertEqual(content, b"hello bootstrap claim mount")

    def test_list_sandboxes(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        # Create a sandbox to ensure there's at least one
        sandbox = claim_sandbox(self, client, cfg)

        # Test list via client method
        sandboxes = client.list_sandboxes(
            status=SandboxLifecycleStatus.RUNNING,
            limit=10,
        )
        self.assertIsInstance(sandboxes, list)
        self.assertGreater(len(sandboxes), 0)
        found = any(sb.id == sandbox.id for sb in sandboxes)
        self.assertTrue(found, f"Sandbox {sandbox.id} not found in list")

        # Test list via sandboxes resource
        sandboxes2 = client.sandboxes.list(
            status="running",
            template_id=cfg.template,
            limit=10,
        )
        self.assertIsInstance(sandboxes2, list)
        self.assertGreater(len(sandboxes2), 0)
        found2 = any(sb.id == sandbox.id for sb in sandboxes2)
        self.assertTrue(found2, f"Sandbox {sandbox.id} not found in resource list")

        # Test with paused filter (should not include running sandbox)
        sandboxes3 = client.list_sandboxes(paused=True, limit=10)
        self.assertIsInstance(sandboxes3, list)
        found3 = any(sb.id == sandbox.id for sb in sandboxes3)
        self.assertFalse(found3, f"Running sandbox {sandbox.id} should not be in paused list")

    def test_sandbox_rootfs_snapshot_restore_fork(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        source = client.sandboxes.claim(cfg.template)
        self.addCleanup(lambda: self._delete_sandbox(client, source.id))

        snapshot_id = ""
        fork_id = ""

        def _cleanup_snapshot() -> None:
            if snapshot_id:
                try:
                    client.sandboxes.delete_rootfs_snapshot(snapshot_id)
                except Exception:
                    pass

        def _cleanup_fork() -> None:
            if fork_id:
                self._delete_sandbox(client, fork_id)

        self.addCleanup(_cleanup_snapshot)
        self.addCleanup(_cleanup_fork)

        marker_path = "/tmp/sdk-py-rootfs-marker.txt"
        source.write_file(marker_path, b"rootfs-v1\n")
        paused = client.sandboxes.pause(source.id)
        self.assertTrue(paused.paused)

        snapshot = client.sandboxes.create_rootfs_snapshot(
            source.id,
            CreateSandboxRootFSSnapshotRequest(name="sdk-py-e2e-rootfs"),
        )
        snapshot_id = snapshot.id
        self.assertTrue(snapshot.id)

        snapshots = client.sandboxes.list_rootfs_snapshots(source.id)
        self.assertTrue(any(item.id == snapshot.id for item in snapshots))

        fetched_snapshot = client.sandboxes.get_rootfs_snapshot(snapshot.id)
        self.assertEqual(fetched_snapshot.id, snapshot.id)

        client.sandboxes.resume(source.id)
        source.write_file(marker_path, b"rootfs-v2\n")
        client.sandboxes.pause(source.id)

        restored = client.sandboxes.restore_rootfs(source.id, RestoreSandboxRootFSRequest(snapshot_id=snapshot.id))
        self.assertEqual(restored.snapshot_id, snapshot.id)

        forked = client.sandboxes.fork(source.id)
        fork_id = forked.sandbox.id
        self.assertEqual(forked.source_sandbox_id, source.id)
        self.assertTrue(fork_id)

        client.sandboxes.delete_rootfs_snapshot(snapshot.id)
        snapshot_id = ""

        client.sandboxes.resume(source.id)
        client.sandboxes.resume(fork_id)

        self.assertEqual(source.read_file(marker_path), b"rootfs-v1\n")
        self.assertEqual(client.sandbox(fork_id).read_file(marker_path), b"rootfs-v1\n")

    @staticmethod
    def _delete_sandbox(client, sandbox_id: str) -> None:
        try:
            client.sandboxes.delete(sandbox_id)
        except Exception:
            pass

    @staticmethod
    def _delete_volume(client, volume_id: str) -> None:
        try:
            client.volumes.delete(volume_id)
        except Exception:
            pass
