import time
import unittest

from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest
from sandbox0.apispec.models.create_snapshot_request import CreateSnapshotRequest
from sandbox0.apispec.models.clone_volume_file_entry import CloneVolumeFileEntry
from sandbox0.apispec.models.clone_volume_files_request import CloneVolumeFilesRequest
from sandbox0.sessions import VolumeSession

from tests.e2e.helpers import claim_sandbox, close_client, new_client, require_config, wait_for_watch_event


class TestVolumes(unittest.TestCase):
    def test_volume_and_snapshot_lifecycle(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

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
        self.assertTrue(restore_resp.success)

        client.volumes.delete_snapshot(volume.id, snapshot.id)

        client.volumes.delete(volume.id)
        deleted = True

    def test_volume_open_session(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        with client.volumes.open(CreateSandboxVolumeRequest()) as volume:
            self.assertTrue(volume.id)

        session = client.volumes.open(CreateSandboxVolumeRequest())
        self.assertIsInstance(session, VolumeSession)
        volume = session.volume
        self.assertTrue(volume.id)
        session.close()

    def test_direct_volume_file_operations(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

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

        base_dir = f"/sdk-py-volume-{time.time_ns()}"
        file_path = f"{base_dir}/hello.txt"
        moved_path = f"{base_dir}/moved.txt"

        client.volumes.mkdir(volume.id, base_dir, recursive=True)
        client.volumes.write_file(volume.id, file_path, b"hello volume")
        client.volumes.stat_file(volume.id, file_path)
        self.assertEqual(client.volumes.read_file(volume.id, file_path), b"hello volume")
        entries = client.volumes.list_files(volume.id, base_dir)
        self.assertTrue(any(entry.name == "hello.txt" for entry in entries))
        client.volumes.move_file(volume.id, file_path, moved_path)
        cloned_path = f"{base_dir}/cloned.txt"
        clone_results = client.volumes.clone_files(
            volume.id,
            CloneVolumeFilesRequest(
                entries=[
                    CloneVolumeFileEntry(
                        source_volume_id=volume.id,
                        source_path=moved_path,
                        target_path=cloned_path,
                        create_parents=True,
                    )
                ]
            ),
        )
        self.assertEqual(len(clone_results), 1)
        self.assertEqual(clone_results[0].target_path, cloned_path)
        self.assertEqual(client.volumes.read_file(volume.id, cloned_path), b"hello volume")

        watch = client.volumes.watch_files(volume.id, base_dir, recursive=True)

        def _cleanup_watch() -> None:
            try:
                watch.unsubscribe()
            except Exception:
                pass

        self.addCleanup(_cleanup_watch)

        client.volumes.write_file(volume.id, f"{base_dir}/watch.txt", b"watch")
        event = wait_for_watch_event(watch, timeout_sec=10)
        self.assertIsNotNone(event, "timed out waiting for volume watch event")
        self.assertTrue(event.path)

        client.volumes.delete_file(volume.id, moved_path)
        client.volumes.delete_file(volume.id, base_dir)
        client.volumes.delete(volume.id)
        deleted = True

    def test_fork_volume_isolation(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)
        sandbox = claim_sandbox(self, client, cfg)

        source = client.volumes.create(CreateSandboxVolumeRequest())
        self.assertTrue(source.id)
        source_deleted = False
        fork_deleted = False

        def _cleanup_source() -> None:
            if source_deleted:
                return
            try:
                client.volumes.delete(source.id)
            except Exception:
                pass

        self.addCleanup(_cleanup_source)

        client.volumes.write_file(source.id, "/hello.txt", b"source-original\n")

        forked = client.volumes.fork(source.id)
        self.assertTrue(forked.id)
        self.assertEqual(getattr(forked, "source_volume_id", None), source.id)

        def _cleanup_fork() -> None:
            if fork_deleted:
                return
            try:
                client.volumes.delete(forked.id)
            except Exception:
                pass

        self.addCleanup(_cleanup_fork)

        client.volumes.write_file(forked.id, "/hello.txt", b"fork-updated\n")
        source_content = client.volumes.read_file(source.id, "/hello.txt")
        self.assertEqual(source_content, b"source-original\n")

        client.volumes.delete(forked.id)
        fork_deleted = True
        client.volumes.delete(source.id)
        source_deleted = True
