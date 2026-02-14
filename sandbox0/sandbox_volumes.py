from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from sandbox0.apispec.api.sandbox_volumes import get_api_v1_sandboxes_id_sandboxvolumes_status
from sandbox0.apispec.api.sandbox_volumes import post_api_v1_sandboxes_id_sandboxvolumes_mount
from sandbox0.apispec.api.sandbox_volumes import post_api_v1_sandboxes_id_sandboxvolumes_unmount
from sandbox0.apispec.models.mount_request import MountRequest
from sandbox0.apispec.models.mount_response import MountResponse
from sandbox0.apispec.models.mount_status import MountStatus
from sandbox0.apispec.models.success_mount_response import SuccessMountResponse
from sandbox0.apispec.models.success_mount_status_response import SuccessMountStatusResponse
from sandbox0.apispec.models.success_unmounted_response import SuccessUnmountedResponse
from sandbox0.apispec.models.unmount_request import UnmountRequest
from sandbox0.apispec.models.volume_config import VolumeConfig
from sandbox0.apispec.types import UNSET
from sandbox0.response import ensure_data, ensure_model

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


class SandboxVolumesMixin:
    id: str
    _client: any

    def mount(self: "Sandbox", volume_id: str, mount_point: str, config: Optional[VolumeConfig] = None) -> MountResponse:
        request = MountRequest(
            sandboxvolume_id=volume_id,
            mount_point=mount_point,
            volume_config=config if config is not None else UNSET,
        )
        resp = post_api_v1_sandboxes_id_sandboxvolumes_mount.sync_detailed(
            id=self.id,
            client=self._client.api,
            body=request,
        )
        return ensure_data(resp, SuccessMountResponse)

    def unmount(self: "Sandbox", volume_id: str, mount_session_id: str) -> SuccessUnmountedResponse:
        resp = post_api_v1_sandboxes_id_sandboxvolumes_unmount.sync_detailed(
            id=self.id,
            client=self._client.api,
            body=UnmountRequest(sandboxvolume_id=volume_id, mount_session_id=mount_session_id),
        )
        return ensure_model(resp, SuccessUnmountedResponse)

    def mount_status(self: "Sandbox") -> list[MountStatus]:
        resp = get_api_v1_sandboxes_id_sandboxvolumes_status.sync_detailed(id=self.id, client=self._client.api)
        data = ensure_data(resp, SuccessMountStatusResponse)
        mounts = data.mounts
        if mounts.__class__.__name__ == "Unset":
            return []
        return mounts
