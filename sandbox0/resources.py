from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from sandbox0.apispec.api.sandboxes import delete_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_status
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_pause
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_refresh
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_resume
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id
from sandbox0.apispec.api.sandbox_volumes import delete_api_v1_sandboxvolumes_id
from sandbox0.apispec.api.sandbox_volumes import get_api_v1_sandboxvolumes
from sandbox0.apispec.api.sandbox_volumes import get_api_v1_sandboxvolumes_id
from sandbox0.apispec.api.sandbox_volumes import post_api_v1_sandboxvolumes
from sandbox0.apispec.api.snapshots import delete_api_v1_sandboxvolumes_id_snapshots_snapshot_id
from sandbox0.apispec.api.snapshots import get_api_v1_sandboxvolumes_id_snapshots
from sandbox0.apispec.api.snapshots import get_api_v1_sandboxvolumes_id_snapshots_snapshot_id
from sandbox0.apispec.api.snapshots import post_api_v1_sandboxvolumes_id_snapshots
from sandbox0.apispec.api.snapshots import post_api_v1_sandboxvolumes_id_snapshots_snapshot_id_restore
from sandbox0.apispec.models.claim_request import ClaimRequest
from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest
from sandbox0.apispec.models.create_snapshot_request import CreateSnapshotRequest
from sandbox0.apispec.models.pause_sandbox_response import PauseSandboxResponse
from sandbox0.apispec.models.refresh_request import RefreshRequest
from sandbox0.apispec.models.refresh_response import RefreshResponse
from sandbox0.apispec.models.resume_sandbox_response import ResumeSandboxResponse
from sandbox0.apispec.models.sandbox import Sandbox as APISandbox
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_status import SandboxStatus
from sandbox0.apispec.models.sandbox_update_request import SandboxUpdateRequest
from sandbox0.apispec.models.sandbox_volume import SandboxVolume
from sandbox0.apispec.models.snapshot import Snapshot
from sandbox0.apispec.models.success_claim_response import SuccessClaimResponse
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_pause_sandbox_response import SuccessPauseSandboxResponse
from sandbox0.apispec.models.success_refresh_response import SuccessRefreshResponse
from sandbox0.apispec.models.success_resume_sandbox_response import SuccessResumeSandboxResponse
from sandbox0.apispec.models.success_restore_response import SuccessRestoreResponse
from sandbox0.apispec.models.success_sandbox_response import SuccessSandboxResponse
from sandbox0.apispec.models.success_sandbox_status_response import SuccessSandboxStatusResponse
from sandbox0.apispec.models.success_sandbox_volume_list_response import SuccessSandboxVolumeListResponse
from sandbox0.apispec.models.success_sandbox_volume_response import SuccessSandboxVolumeResponse
from sandbox0.apispec.models.success_snapshot_list_response import SuccessSnapshotListResponse
from sandbox0.apispec.models.success_snapshot_response import SuccessSnapshotResponse
from sandbox0.response import ensure_data, ensure_model
from sandbox0.sessions import SandboxSession, VolumeSession

if TYPE_CHECKING:
    from sandbox0.client import Client
    from sandbox0.sandbox import Sandbox


class Sandboxes:
    def __init__(self, client: "Client") -> None:
        self._client = client

    def claim(self, template: str, config: Optional[SandboxConfig] = None) -> "Sandbox":
        request = ClaimRequest(template=template, config=config) if config is not None else ClaimRequest(template=template)
        resp = post_api_v1_sandboxes.sync_detailed(client=self._client.api, body=request)
        data = ensure_data(resp, SuccessClaimResponse)
        from sandbox0.sandbox import Sandbox

        return Sandbox(
            id=data.sandbox_id,
            client=self._client,
            template=data.template,
            cluster_id=None if data.cluster_id.__class__.__name__ == "Unset" else data.cluster_id,
            pod_name=data.pod_name,
            status=data.status,
        )

    def open(self, template: str, config: Optional[SandboxConfig] = None) -> SandboxSession:
        sandbox = self.claim(template, config=config)
        return SandboxSession(sandbox, closer=lambda: None if self.delete(sandbox.id) else None)

    def get(self, sandbox_id: str) -> APISandbox:
        resp = get_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxResponse)

    def update(self, sandbox_id: str, request: SandboxUpdateRequest) -> APISandbox:
        resp = put_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api, body=request)
        return ensure_data(resp, SuccessSandboxResponse)

    def delete(self, sandbox_id: str) -> SuccessMessageResponse:
        resp = delete_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_model(resp, SuccessMessageResponse)

    def status(self, sandbox_id: str) -> SandboxStatus:
        resp = get_api_v1_sandboxes_id_status.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxStatusResponse)

    def pause(self, sandbox_id: str) -> PauseSandboxResponse:
        resp = post_api_v1_sandboxes_id_pause.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessPauseSandboxResponse)

    def resume(self, sandbox_id: str) -> ResumeSandboxResponse:
        resp = post_api_v1_sandboxes_id_resume.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessResumeSandboxResponse)

    def refresh(self, sandbox_id: str, request: Optional[RefreshRequest] = None) -> RefreshResponse:
        # For sandbox refresh, the body is optional but the generated API requires it.
        # Pass an empty refresh_token if no request is provided - the server ignores it for this endpoint.
        body = request if request is not None else RefreshRequest(refresh_token="")
        resp = post_api_v1_sandboxes_id_refresh.sync_detailed(id=sandbox_id, client=self._client.api, body=body)
        return ensure_data(resp, SuccessRefreshResponse)

    def sandbox(self, sandbox_id: str) -> "Sandbox":
        from sandbox0.sandbox import Sandbox

        return Sandbox(id=sandbox_id, client=self._client)


class Volumes:
    def __init__(self, client: "Client") -> None:
        self._client = client

    def create(self, request: CreateSandboxVolumeRequest) -> SandboxVolume:
        resp = post_api_v1_sandboxvolumes.sync_detailed(client=self._client.api, body=request)
        return ensure_data(resp, SuccessSandboxVolumeResponse)

    def open(self, request: CreateSandboxVolumeRequest) -> VolumeSession:
        volume = self.create(request)
        return VolumeSession(volume, closer=lambda: None if self.delete(volume.id) else None)

    def list(self) -> List[SandboxVolume]:
        resp = get_api_v1_sandboxvolumes.sync_detailed(client=self._client.api)
        data = ensure_data(resp, SuccessSandboxVolumeListResponse)
        return data

    def get(self, volume_id: str) -> SandboxVolume:
        resp = get_api_v1_sandboxvolumes_id.sync_detailed(id=volume_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxVolumeResponse)

    def delete(self, volume_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandboxvolumes_id.sync_detailed(id=volume_id, client=self._client.api)
        return ensure_model(resp, SuccessDeletedResponse)

    def create_snapshot(self, volume_id: str, request: CreateSnapshotRequest) -> Snapshot:
        resp = post_api_v1_sandboxvolumes_id_snapshots.sync_detailed(id=volume_id, client=self._client.api, body=request)
        return ensure_data(resp, SuccessSnapshotResponse)

    def list_snapshots(self, volume_id: str) -> List[Snapshot]:
        resp = get_api_v1_sandboxvolumes_id_snapshots.sync_detailed(id=volume_id, client=self._client.api)
        data = ensure_data(resp, SuccessSnapshotListResponse)
        return data

    def get_snapshot(self, volume_id: str, snapshot_id: str) -> Snapshot:
        resp = get_api_v1_sandboxvolumes_id_snapshots_snapshot_id.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_data(resp, SuccessSnapshotResponse)

    def delete_snapshot(self, volume_id: str, snapshot_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandboxvolumes_id_snapshots_snapshot_id.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_model(resp, SuccessDeletedResponse)

    def restore_snapshot(self, volume_id: str, snapshot_id: str) -> SuccessRestoreResponse:
        resp = post_api_v1_sandboxvolumes_id_snapshots_snapshot_id_restore.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_model(resp, SuccessRestoreResponse)
