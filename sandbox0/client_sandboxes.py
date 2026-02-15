from __future__ import annotations

from typing import Any, Optional, TYPE_CHECKING

from sandbox0.apispec.api.sandboxes import delete_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_status
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_pause
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_refresh
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_resume
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id
from sandbox0.apispec.models.claim_request import ClaimRequest
from sandbox0.apispec.models.claim_response import ClaimResponse
from sandbox0.apispec.models.refresh_request import RefreshRequest
from sandbox0.apispec.models.refresh_response import RefreshResponse
from sandbox0.apispec.models.resume_sandbox_response import ResumeSandboxResponse
from sandbox0.apispec.models.pause_sandbox_response import PauseSandboxResponse
from sandbox0.apispec.models.sandbox import Sandbox as APISandbox
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_status import SandboxStatus
from sandbox0.apispec.models.sandbox_update_request import SandboxUpdateRequest
from sandbox0.apispec.models.success_claim_response import SuccessClaimResponse
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_pause_sandbox_response import SuccessPauseSandboxResponse
from sandbox0.apispec.models.success_refresh_response import SuccessRefreshResponse
from sandbox0.apispec.models.success_resume_sandbox_response import SuccessResumeSandboxResponse
from sandbox0.apispec.models.success_sandbox_response import SuccessSandboxResponse
from sandbox0.apispec.models.success_sandbox_status_response import SuccessSandboxStatusResponse
from sandbox0.response import ensure_data, ensure_model

if TYPE_CHECKING:
    from sandbox0.client import Client
    from sandbox0.sandbox import Sandbox


class ClientSandboxesMixin:
    _api: Any

    def claim_sandbox(self: "Client", template: str, config: Optional[SandboxConfig] = None) -> "Sandbox":  # type: ignore[misc]
        request = ClaimRequest(template=template, config=config) if config is not None else ClaimRequest(template=template)
        resp = post_api_v1_sandboxes.sync_detailed(client=self._api, body=request)
        data = ensure_data(resp, SuccessClaimResponse)
        from sandbox0.sandbox import Sandbox

        return Sandbox(
            id=data.sandbox_id,
            client=self,
            template=data.template,
            cluster_id=None if data.cluster_id.__class__.__name__ == "Unset" else data.cluster_id,
            pod_name=data.pod_name,
            status=data.status,
        )

    def get_sandbox(self: "Client", sandbox_id: str) -> APISandbox:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._api)
        return ensure_data(resp, SuccessSandboxResponse)

    def update_sandbox(self: "Client", sandbox_id: str, request: SandboxUpdateRequest) -> APISandbox:  # type: ignore[misc]
        resp = put_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._api, body=request)
        return ensure_data(resp, SuccessSandboxResponse)

    def delete_sandbox(self: "Client", sandbox_id: str) -> SuccessMessageResponse:  # type: ignore[misc]
        resp = delete_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._api)
        return ensure_model(resp, SuccessMessageResponse)

    def status_sandbox(self: "Client", sandbox_id: str) -> SandboxStatus:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_status.sync_detailed(id=sandbox_id, client=self._api)
        return ensure_data(resp, SuccessSandboxStatusResponse)

    def pause_sandbox(self: "Client", sandbox_id: str) -> PauseSandboxResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_pause.sync_detailed(id=sandbox_id, client=self._api)
        return ensure_data(resp, SuccessPauseSandboxResponse)

    def resume_sandbox(self: "Client", sandbox_id: str) -> ResumeSandboxResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_resume.sync_detailed(id=sandbox_id, client=self._api)
        return ensure_data(resp, SuccessResumeSandboxResponse)

    def refresh_sandbox(self: "Client", sandbox_id: str, request: Optional[RefreshRequest] = None) -> RefreshResponse:  # type: ignore[misc]
        body = request if request is not None else RefreshRequest(refresh_token="")
        resp = post_api_v1_sandboxes_id_refresh.sync_detailed(id=sandbox_id, client=self._api, body=body)
        return ensure_data(resp, SuccessRefreshResponse)
