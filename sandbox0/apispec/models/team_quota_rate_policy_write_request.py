from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.team_quota_rate_policy_write_request_kind import (
    TeamQuotaRatePolicyWriteRequestKind,
)

T = TypeVar("T", bound="TeamQuotaRatePolicyWriteRequest")


@_attrs_define
class TeamQuotaRatePolicyWriteRequest:
    """
    Attributes:
        kind (TeamQuotaRatePolicyWriteRequestKind):
        tokens (int):
        interval_ms (int):
        burst (int):
    """

    kind: TeamQuotaRatePolicyWriteRequestKind
    tokens: int
    interval_ms: int
    burst: int

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        tokens = self.tokens

        interval_ms = self.interval_ms

        burst = self.burst

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "tokens": tokens,
                "interval_ms": interval_ms,
                "burst": burst,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = TeamQuotaRatePolicyWriteRequestKind(d.pop("kind"))

        tokens = d.pop("tokens")

        interval_ms = d.pop("interval_ms")

        burst = d.pop("burst")

        team_quota_rate_policy_write_request = cls(
            kind=kind,
            tokens=tokens,
            interval_ms=interval_ms,
            burst=burst,
        )

        return team_quota_rate_policy_write_request
