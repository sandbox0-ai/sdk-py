from __future__ import annotations

from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox
    from sandbox0.apispec.models.sandbox_volume import SandboxVolume


class SandboxSession:
    def __init__(self, sandbox: "Sandbox", closer: Callable[[], None]) -> None:
        self._sandbox = sandbox
        self._closer = closer
        self._closed = False

    @property
    def sandbox(self) -> "Sandbox":
        return self._sandbox

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._closer()

    def __enter__(self) -> "Sandbox":
        return self._sandbox

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.close()
        return False


class VolumeSession:
    def __init__(self, volume: "SandboxVolume", closer: Callable[[], None]) -> None:
        self._volume = volume
        self._closer = closer
        self._closed = False

    @property
    def volume(self) -> "SandboxVolume":
        return self._volume

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._closer()

    def __enter__(self) -> "SandboxVolume":
        return self._volume

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.close()
        return False


class MountSession:
    def __init__(
        self,
        *,
        volume_id: str,
        mount_point: str,
        mount_session_id: str,
        unmount: Callable[[], None],
    ) -> None:
        self.volume_id = volume_id
        self.mount_point = mount_point
        self.mount_session_id = mount_session_id
        self._unmount = unmount
        self._closed = False

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._unmount()

    def __enter__(self) -> "MountSession":
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.close()
        return False
