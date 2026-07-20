from __future__ import annotations

from typing import Any, TYPE_CHECKING

from sandbox0.apispec.api.quotas import get_api_v1_quotas
from sandbox0.apispec.api.quotas import get_api_v1_quotas_dimension
from sandbox0.apispec.models.get_api_v1_quotas_response_200 import (
    GetApiV1QuotasResponse200,
)
from sandbox0.apispec.models.quota_dimension import QuotaDimension
from sandbox0.apispec.models.success_team_quota_response import (
    SuccessTeamQuotaResponse,
)
from sandbox0.apispec.models.team_quota import TeamQuota
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.client import Client


class ClientQuotasMixin:
    _api: Any

    def list_team_quotas(self: "Client") -> list[TeamQuota]:  # type: ignore[misc]
        response = get_api_v1_quotas.sync_detailed(client=self._api)
        return ensure_data(response, GetApiV1QuotasResponse200)

    def get_team_quota(  # type: ignore[misc]
        self: "Client",
        dimension: QuotaDimension,
    ) -> TeamQuota:
        response = get_api_v1_quotas_dimension.sync_detailed(
            dimension=dimension,
            client=self._api,
        )
        return ensure_data(response, SuccessTeamQuotaResponse)
