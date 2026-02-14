import time
import unittest

from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest
from sandbox0.apispec.models.create_snapshot_request import CreateSnapshotRequest
from sandbox0.sessions import VolumeSession

from tests.e2e.helpers import new_client, require_config


class TestVolumes(unittest.TestCase):
    def test_volume_and_snapshot_lifecycle(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)

        volume = client.volumes.create(CreateSandboxVolumeRequest())
        self.assertTrue(volume.id)
        deleted = False

        def _cleanup() -> None:
            if deleted:
                return
            try:
                client.volumes.delete(volume.id)
            except Exception:
                pass

        self.addCleanup(_cleanup)

        volumes = client.volumes.list()
        self.assertTrue(any(v.id == volume.id for v in volumes))

        fetched = client.volumes.get(volume.id)
        self.assertEqual(fetched.id, volume.id)

        snapshot_name = f"sdk-py-e2e-snap-{time.time_ns()}"
        snapshot = client.volumes.create_snapshot(
            volume.id,
            CreateSnapshotRequest(name=snapshot_name, description="sdk py e2e snapshot"),
        )
        self.assertTrue(snapshot.id)

        snapshots = client.volumes.list_snapshots(volume.id)
        self.assertTrue(any(s.id == snapshot.id for s in snapshots))

        fetched_snapshot = client.volumes.get_snapshot(volume.id, snapshot.id)
        self.assertEqual(fetched_snapshot.id, snapshot.id)

        restore_resp = client.volumes.restore_snapshot(volume.id, snapshot.id)
        self.assertEqual(restore_resp.snapshot_id, snapshot.id)

        client.volumes.delete_snapshot(volume.id, snapshot.id)

        client.volumes.delete(volume.id)
        deleted = True

    def test_volume_open_session(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)

        with client.volumes.open(CreateSandboxVolumeRequest()) as volume:
            self.assertTrue(volume.id)

        session = client.volumes.open(CreateSandboxVolumeRequest())
        self.assertIsInstance(session, VolumeSession)
        volume = session.volume
        self.assertTrue(volume.id)
        session.close()
