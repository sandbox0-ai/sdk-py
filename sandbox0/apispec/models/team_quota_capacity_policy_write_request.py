from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.team_quota_capacity_policy_write_request_kind import (
    TeamQuotaCapacityPolicyWriteRequestKind,
)

T = TypeVar("T", bound="TeamQuotaCapacityPolicyWriteRequest")


@_attrs_define
class TeamQuotaCapacityPolicyWriteRequest:
    """
    Attributes:
        kind (TeamQuotaCapacityPolicyWriteRequestKind):
        limit (int):
    """

    kind: TeamQuotaCapacityPolicyWriteRequestKind
    limit: int

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = TeamQuotaCapacityPolicyWriteRequestKind(d.pop("kind"))

        limit = d.pop("limit")

        team_quota_capacity_policy_write_request = cls(
            kind=kind,
            limit=limit,
        )

        return team_quota_capacity_policy_write_request
