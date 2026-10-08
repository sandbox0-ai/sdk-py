from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0 import QuotaDimension
from sandbox0 import TeamQuota
from sandbox0 import TeamQuotaKind
from sandbox0 import TeamQuotaSource
from sandbox0 import TeamQuotaUnit
from sandbox0.apispec.models.get_api_v1_quotas_response_200 import (
    GetApiV1QuotasResponse200,
)
from sandbox0.apispec.models.success_team_quota_response import (
    SuccessTeamQuotaResponse,
)
from sandbox0.apispec.types import Response


def rate_quota() -> TeamQuota:
    return TeamQuota(
        team_id="team-1",
        dimension=QuotaDimension.API_REQUESTS,
        kind=TeamQuotaKind.RATE,
        limit_value=100,
        interval_ms=1000,
        burst_value=200,
        current=None,
        remaining=None,
        unlimited=False,
        unit=TeamQuotaUnit.REQUESTS,
        source=TeamQuotaSource.REGION_DEFAULT,
    )


class TestQuotas(TestCase):
    def setUp(self) -> None:
        self.client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(self.client.close)

    def test_decodes_paused_capacity_wire_response(self) -> None:
        quota = TeamQuota.from_dict({
            "team_id": "team-1", "dimension": "paused_sandboxes",
            "kind": "capacity", "limit_value": 2000, "interval_ms": None,
            "burst_value": None, "current": 2001, "remaining": 0,
            "unlimited": False, "unit": "count", "source": "region_default",
        })
        self.assertEqual(quota.dimension, QuotaDimension.PAUSED_SANDBOXES)
        self.assertEqual(quota.current, 2001)
        self.assertEqual(quota.remaining, 0)

    def test_list_team_quotas(self) -> None:
        quota = rate_quota()
        response = Response(
            status_code=HTTPStatus.OK,
            content=b"{}",
            headers={},
            parsed=GetApiV1QuotasResponse200(success=True, data=[quota]),
        )

        with patch(
            "sandbox0.client_quotas.get_api_v1_quotas.sync_detailed",
            return_value=response,
        ) as request:
            quotas = self.client.list_team_quotas()

        request.assert_called_once_with(client=self.client.api)
        self.assertEqual(quotas, [quota])
        self.assertIsNone(quotas[0].current)
        self.assertIsNone(quotas[0].remaining)

    def test_get_team_quota(self) -> None:
        quota = rate_quota()
        response = Response(
            status_code=HTTPStatus.OK,
            content=b"{}",
            headers={},
            parsed=SuccessTeamQuotaResponse(success=True, data=quota),
        )

        with patch(
            "sandbox0.client_quotas.get_api_v1_quotas_dimension.sync_detailed",
            return_value=response,
        ) as request:
            result = self.client.get_team_quota(QuotaDimension.API_REQUESTS)

        request.assert_called_once_with(
            dimension=QuotaDimension.API_REQUESTS,
            client=self.client.api,
        )
        self.assertIs(result, quota)
