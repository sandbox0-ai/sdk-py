from __future__ import annotations

from typing import TYPE_CHECKING

from sandbox0.apispec.api.sandbox_volumes import delete_api_v1_sandboxvolumes_id
from sandbox0.apispec.api.sandbox_volumes import get_api_v1_sandboxvolumes
from sandbox0.apispec.api.sandbox_volumes import get_api_v1_sandboxvolumes_id
from sandbox0.apispec.api.sandbox_volumes import post_api_v1_sandboxvolumes
from sandbox0.apispec.api.snapshots import delete_api_v1_sandboxvolumes_id_snapshots_snapshot_id
from sandbox0.apispec.api.snapshots import get_api_v1_sandboxvolumes_id_snapshots
from sandbox0.apispec.api.snapshots import get_api_v1_sandboxvolumes_id_snapshots_snapshot_id
from sandbox0.apispec.api.snapshots import post_api_v1_sandboxvolumes_id_snapshots
from sandbox0.apispec.api.snapshots import post_api_v1_sandboxvolumes_id_snapshots_snapshot_id_restore
from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest
from sandbox0.apispec.models.create_snapshot_request import CreateSnapshotRequest
from sandbox0.apispec.models.sandbox_volume import SandboxVolume
from sandbox0.apispec.models.snapshot import Snapshot
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_restore_response import SuccessRestoreResponse
from sandbox0.apispec.models.success_sandbox_volume_list_response import SuccessSandboxVolumeListResponse
from sandbox0.apispec.models.success_sandbox_volume_response import SuccessSandboxVolumeResponse
from sandbox0.apispec.models.success_snapshot_list_response import SuccessSnapshotListResponse
from sandbox0.apispec.models.success_snapshot_response import SuccessSnapshotResponse
from sandbox0.response import ensure_data, ensure_model

if TYPE_CHECKING:
    from sandbox0.client import Client


class ClientVolumesMixin:
    _api: any

    def create_volume(self: "Client", request: CreateSandboxVolumeRequest) -> SandboxVolume:
        resp = post_api_v1_sandboxvolumes.sync_detailed(client=self._api, body=request)
        return ensure_data(resp, SuccessSandboxVolumeResponse)

    def list_volumes(self: "Client") -> list[SandboxVolume]:
        resp = get_api_v1_sandboxvolumes.sync_detailed(client=self._api)
        data = ensure_data(resp, SuccessSandboxVolumeListResponse)
        return data

    # Backward-compatible alias.
    def list_volume(self: "Client") -> list[SandboxVolume]:
        return self.list_volumes()

    def get_volume(self: "Client", volume_id: str) -> SandboxVolume:
        resp = get_api_v1_sandboxvolumes_id.sync_detailed(id=volume_id, client=self._api)
        return ensure_data(resp, SuccessSandboxVolumeResponse)

    def delete_volume(self: "Client", volume_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandboxvolumes_id.sync_detailed(id=volume_id, client=self._api)
        return ensure_model(resp, SuccessDeletedResponse)

    def create_volume_snapshot(self: "Client", volume_id: str, request: CreateSnapshotRequest) -> Snapshot:
        resp = post_api_v1_sandboxvolumes_id_snapshots.sync_detailed(id=volume_id, client=self._api, body=request)
        return ensure_data(resp, SuccessSnapshotResponse)

    def list_volume_snapshots(self: "Client", volume_id: str) -> list[Snapshot]:
        resp = get_api_v1_sandboxvolumes_id_snapshots.sync_detailed(id=volume_id, client=self._api)
        data = ensure_data(resp, SuccessSnapshotListResponse)
        return data

    def get_volume_snapshot(self: "Client", volume_id: str, snapshot_id: str) -> Snapshot:
        resp = get_api_v1_sandboxvolumes_id_snapshots_snapshot_id.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._api,
        )
        return ensure_data(resp, SuccessSnapshotResponse)

    def delete_volume_snapshot(self: "Client", volume_id: str, snapshot_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandboxvolumes_id_snapshots_snapshot_id.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._api,
        )
        return ensure_model(resp, SuccessDeletedResponse)

    def restore_volume_snapshot(self: "Client", volume_id: str, snapshot_id: str) -> SuccessRestoreResponse:
        resp = post_api_v1_sandboxvolumes_id_snapshots_snapshot_id_restore.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._api,
        )
        return ensure_model(resp, SuccessRestoreResponse)
