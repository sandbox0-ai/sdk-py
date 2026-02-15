from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sandbox0.apispec.api.sandboxes import delete_api_v1_sandboxes_id_exposed_ports
from sandbox0.apispec.api.sandboxes import delete_api_v1_sandboxes_id_exposed_ports_port
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_exposed_ports
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id_exposed_ports
from sandbox0.apispec.models.exposed_port_config import ExposedPortConfig
from sandbox0.apispec.models.success_exposed_ports_response import SuccessExposedPortsResponse
from sandbox0.apispec.models.update_exposed_ports_request import UpdateExposedPortsRequest
from sandbox0.models import ExposedPort, ExposedPortsResponse
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


class SandboxExposedPortsMixin:
    id: str
    _client: Any

    def get_exposed_ports(self: "Sandbox") -> ExposedPortsResponse:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_exposed_ports.sync_detailed(id=self.id, client=self._client.api)
        data = ensure_data(resp, SuccessExposedPortsResponse)
        return _to_exposed_ports_response(data)

    def update_exposed_ports(self: "Sandbox", ports: list[ExposedPort]) -> ExposedPortsResponse:  # type: ignore[misc]
        request = UpdateExposedPortsRequest(
            ports=[ExposedPortConfig(port=p.port, resume=p.resume) for p in ports]
        )
        resp = put_api_v1_sandboxes_id_exposed_ports.sync_detailed(id=self.id, client=self._client.api, body=request)
        data = ensure_data(resp, SuccessExposedPortsResponse)
        return _to_exposed_ports_response(data)

    def expose_port(self: "Sandbox", port: int, resume: bool) -> ExposedPortsResponse:  # type: ignore[misc]
        current = self.get_exposed_ports()
        ports = list(current.ports)
        updated = False
        for index, existing in enumerate(ports):
            if existing.port == port:
                ports[index] = ExposedPort(port=port, resume=resume, public_url=existing.public_url)
                updated = True
                break
        if not updated:
            ports.append(ExposedPort(port=port, resume=resume))
        return self.update_exposed_ports(ports)

    def unexpose_port(self: "Sandbox", port: int) -> ExposedPortsResponse:  # type: ignore[misc]
        resp = delete_api_v1_sandboxes_id_exposed_ports_port.sync_detailed(
            id=self.id,
            port=port,
            client=self._client.api,
        )
        data = ensure_data(resp, SuccessExposedPortsResponse)
        return _to_exposed_ports_response(data)

    def clear_exposed_ports(self: "Sandbox") -> None:  # type: ignore[misc]
        delete_api_v1_sandboxes_id_exposed_ports.sync_detailed(id=self.id, client=self._client.api)


def _to_exposed_ports_response(data: Any) -> ExposedPortsResponse:
    ports: list[ExposedPort] = []
    for item in data.exposed_ports:
        public_url = "" if item.public_url.__class__.__name__ == "Unset" else str(item.public_url)
        ports.append(ExposedPort(port=item.port, resume=item.resume, public_url=public_url))
    domain = "" if data.exposure_domain.__class__.__name__ == "Unset" else str(data.exposure_domain)
    return ExposedPortsResponse(ports=ports, exposure_domain=domain)
