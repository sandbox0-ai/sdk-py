from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_network
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id_network
from sandbox0.apispec.models.success_sandbox_network_policy_response import SuccessSandboxNetworkPolicyResponse
from sandbox0.apispec.models.tpl_sandbox_network_policy import TplSandboxNetworkPolicy
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


class SandboxNetworkMixin:
    id: str
    _client: Any

    def get_network_policy(self: "Sandbox") -> TplSandboxNetworkPolicy:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_network.sync_detailed(id=self.id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxNetworkPolicyResponse)

    def update_network_policy(self: "Sandbox", policy: TplSandboxNetworkPolicy) -> TplSandboxNetworkPolicy:  # type: ignore[misc]
        resp = put_api_v1_sandboxes_id_network.sync_detailed(id=self.id, client=self._client.api, body=policy)
        return ensure_data(resp, SuccessSandboxNetworkPolicyResponse)
