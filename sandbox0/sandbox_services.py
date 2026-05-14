from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_services
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id_services
from sandbox0.apispec.models.sandbox_app_service import SandboxAppService
from sandbox0.apispec.models.sandbox_services_update_request import SandboxServicesUpdateRequest
from sandbox0.apispec.models.success_sandbox_services_response import SuccessSandboxServicesResponse
from sandbox0.models import SandboxServicesResponse
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


class SandboxServicesMixin:
    id: str
    _client: Any

    def get_services(self: "Sandbox") -> SandboxServicesResponse:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_services.sync_detailed(id=self.id, client=self._client.api)
        data = ensure_data(resp, SuccessSandboxServicesResponse)
        return _to_services_response(data)

    def update_services(self: "Sandbox", services: list[SandboxAppService]) -> SandboxServicesResponse:  # type: ignore[misc]
        resp = put_api_v1_sandboxes_id_services.sync_detailed(
            id=self.id,
            client=self._client.api,
            body=SandboxServicesUpdateRequest(services=services or []),
        )
        data = ensure_data(resp, SuccessSandboxServicesResponse)
        return _to_services_response(data)

    def clear_services(self: "Sandbox") -> SandboxServicesResponse:  # type: ignore[misc]
        return self.update_services([])


def _to_services_response(data: Any) -> SandboxServicesResponse:
    return SandboxServicesResponse(
        sandbox_id=data.sandbox_id,
        services=list(data.services or []),
    )

