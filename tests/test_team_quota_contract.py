import unittest

from sandbox0.apispec.api.quotas.put_api_v1_teams_team_id_quotas_key import (
    _get_kwargs,
)
from sandbox0.apispec.models.team_quota_capacity_policy_write_request import (
    TeamQuotaCapacityPolicyWriteRequest,
)
from sandbox0.apispec.models.team_quota_capacity_policy_write_request_kind import (
    TeamQuotaCapacityPolicyWriteRequestKind,
)
from sandbox0.apispec.models.team_quota_concurrency_policy_write_request import (
    TeamQuotaConcurrencyPolicyWriteRequest,
)
from sandbox0.apispec.models.team_quota_concurrency_policy_write_request_kind import (
    TeamQuotaConcurrencyPolicyWriteRequestKind,
)
from sandbox0.apispec.models.team_quota_key import TeamQuotaKey
from sandbox0.apispec.models.team_quota_rate_policy_write_request import (
    TeamQuotaRatePolicyWriteRequest,
)
from sandbox0.apispec.models.team_quota_rate_policy_write_request_kind import (
    TeamQuotaRatePolicyWriteRequestKind,
)


class TeamQuotaContractTests(unittest.TestCase):
    def test_write_policy_variants_serialize_without_sibling_fields(self) -> None:
        cases = [
            (
                TeamQuotaKey.SANDBOX_RUNTIME_COUNT,
                TeamQuotaCapacityPolicyWriteRequest(
                    kind=TeamQuotaCapacityPolicyWriteRequestKind.CAPACITY,
                    limit=100,
                ),
                {"kind": "capacity", "limit": 100},
            ),
            (
                TeamQuotaKey.ACTIVE_REQUEST_COUNT,
                TeamQuotaConcurrencyPolicyWriteRequest(
                    kind=TeamQuotaConcurrencyPolicyWriteRequestKind.CONCURRENCY,
                    limit=25,
                ),
                {"kind": "concurrency", "limit": 25},
            ),
            (
                TeamQuotaKey.API_REQUESTS,
                TeamQuotaRatePolicyWriteRequest(
                    kind=TeamQuotaRatePolicyWriteRequestKind.RATE,
                    tokens=20,
                    interval_ms=1000,
                    burst=40,
                ),
                {
                    "kind": "rate",
                    "tokens": 20,
                    "interval_ms": 1000,
                    "burst": 40,
                },
            ),
        ]

        for key, policy, expected in cases:
            with self.subTest(kind=expected["kind"]):
                request = _get_kwargs("team-1", key, body=policy)
                self.assertEqual(request["json"], expected)


if __name__ == "__main__":
    unittest.main()
