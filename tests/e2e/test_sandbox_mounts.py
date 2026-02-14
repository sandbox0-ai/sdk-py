import time
import unittest

from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest

from tests.e2e.helpers import claim_sandbox, new_client, require_config


class TestSandboxMounts(unittest.TestCase):
    def test_mount_lifecycle(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        sandbox = claim_sandbox(self, client, cfg)

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

        mount_point = f"/mnt/sdk-py-e2e-{time.time_ns()}"
        session = sandbox.mount(volume.id, mount_point)
        self.assertEqual(session.mount_point, mount_point)

        mounts = sandbox.mount_status()
        self.assertTrue(any(m.mount_point == mount_point for m in mounts))

        session.close()

        client.volumes.delete(volume.id)
        deleted = True
