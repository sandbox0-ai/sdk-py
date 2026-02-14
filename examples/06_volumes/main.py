from __future__ import annotations

import time

from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest
from sandbox0.apispec.models.create_snapshot_request import CreateSnapshotRequest
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.volume_access_mode import VolumeAccessMode

from examples.common import create_client


def main() -> None:
    client = create_client()
    with client.sandboxes.open("default", config=SandboxConfig(hard_ttl=300)) as sandbox:
        with client.volumes.open(CreateSandboxVolumeRequest(access_mode=VolumeAccessMode.RWX)) as volume:
            volume_id = volume.id
            print(f"volume created: {volume_id}")

            with sandbox.mount(volume_id, "/mnt/data"):
                print(f"volume mounted: {volume_id}")
                sandbox.write_file("/mnt/data/hello.txt", b"hello volume\n")
                print("file written: /mnt/data/hello.txt")

                snapshot_name = f"snap-{int(time.time())}"
                snapshot = client.volumes.create_snapshot(volume_id, CreateSnapshotRequest(name=snapshot_name))
                print(f"snapshot created: {snapshot.id}")

                sandbox.write_file("/mnt/data/hello.txt", b"hello volume\nsecond line\n")
                print("file updated: /mnt/data/hello.txt")
                print("file content:\n" + sandbox.read_file("/mnt/data/hello.txt").decode("utf-8"), end="")

                client.volumes.restore_snapshot(volume_id, snapshot.id)
                print(f"snapshot restored: {snapshot.id}")
                print("file content:\n" + sandbox.read_file("/mnt/data/hello.txt").decode("utf-8"), end="")

                with client.sandboxes.open("default") as sandbox2:
                    print(f"new sandbox created: {sandbox2.id}")
                    with sandbox2.mount(volume_id, "/mnt/data"):
                        print("sandbox2 file content:\n" + sandbox2.read_file("/mnt/data/hello.txt").decode("utf-8"), end="")


if __name__ == "__main__":
    main()
