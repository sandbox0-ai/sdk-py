from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_public_gateway
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id_public_gateway
from sandbox0.apispec.models.public_gateway_config import PublicGatewayConfig
from sandbox0.apispec.models.success_public_gateway_response import SuccessPublicGatewayResponse
from sandbox0.models import PublicGatewayResponse
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


class SandboxPublicGatewayMixin:
    id: str
    _client: Any

    def get_public_gateway(self: "Sandbox") -> PublicGatewayResponse:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_public_gateway.sync_detailed(id=self.id, client=self._client.api)
        data = ensure_data(resp, SuccessPublicGatewayResponse)
        return _to_public_gateway_response(data)

    def update_public_gateway(self: "Sandbox", public_gateway: PublicGatewayConfig) -> PublicGatewayResponse:  # type: ignore[misc]
        resp = put_api_v1_sandboxes_id_public_gateway.sync_detailed(
            id=self.id,
            client=self._client.api,
            body=public_gateway,
        )
        data = ensure_data(resp, SuccessPublicGatewayResponse)
        return _to_public_gateway_response(data)

    def clear_public_gateway(self: "Sandbox") -> PublicGatewayResponse:  # type: ignore[misc]
        return self.update_public_gateway(PublicGatewayConfig(enabled=False))


def _to_public_gateway_response(data: Any) -> PublicGatewayResponse:
    domain = "" if data.exposure_domain.__class__.__name__ == "Unset" else str(data.exposure_domain)
    return PublicGatewayResponse(
        sandbox_id=data.sandbox_id,
        public_gateway=data.public_gateway,
        exposure_domain=domain,
    )
