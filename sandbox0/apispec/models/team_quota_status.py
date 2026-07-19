from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.team_quota_key import TeamQuotaKey
from ..models.team_quota_kind import TeamQuotaKind
from ..models.team_quota_policy_source import TeamQuotaPolicySource
from ..models.team_quota_unit import TeamQuotaUnit

if TYPE_CHECKING:
    from ..models.team_quota_policy import TeamQuotaPolicy


T = TypeVar("T", bound="TeamQuotaStatus")


@_attrs_define
class TeamQuotaStatus:
    """Capacity rows expose durable committed and reserved usage. Concurrency rows expose live lease usage. Rate rows
    expose policy but not distributed Redis token balance, so committed, reserved, and used are zero and remaining is
    null.

        Attributes:
            team_id (str):
            key (TeamQuotaKey):
            kind (TeamQuotaKind):
            unit (TeamQuotaUnit):
            source (TeamQuotaPolicySource): Identifies whether the effective policy is inherited from the region default or
                defined by an explicit team override.
            policy (TeamQuotaPolicy): Capacity and concurrency policies use limit. Rate policies use tokens, interval_ms,
                and burst.
            committed (int): Durable committed capacity usage; zero for concurrency and rate policies.
            reserved (int): Durable in-flight capacity reservation; zero for concurrency and rate policies.
            used (int): Committed plus reserved capacity usage, or current live concurrency usage; zero for rate policies.
            remaining (Union[None, int]): Remaining capacity or concurrency headroom; null for rate policies because token
                balance is not exposed.
    """

    team_id: str
    key: TeamQuotaKey
    kind: TeamQuotaKind
    unit: TeamQuotaUnit
    source: TeamQuotaPolicySource
    policy: "TeamQuotaPolicy"
    committed: int
    reserved: int
    used: int
    remaining: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        key = self.key.value

        kind = self.kind.value

        unit = self.unit.value

        source = self.source.value

        policy = self.policy.to_dict()

        committed = self.committed

        reserved = self.reserved

        used = self.used

        remaining: Union[None, int]
        remaining = self.remaining

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "key": key,
                "kind": kind,
                "unit": unit,
                "source": source,
                "policy": policy,
                "committed": committed,
                "reserved": reserved,
                "used": used,
                "remaining": remaining,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_quota_policy import TeamQuotaPolicy

        d = dict(src_dict)
        team_id = d.pop("team_id")

        key = TeamQuotaKey(d.pop("key"))

        kind = TeamQuotaKind(d.pop("kind"))

        unit = TeamQuotaUnit(d.pop("unit"))

        source = TeamQuotaPolicySource(d.pop("source"))

        policy = TeamQuotaPolicy.from_dict(d.pop("policy"))

        committed = d.pop("committed")

        reserved = d.pop("reserved")

        used = d.pop("used")

        def _parse_remaining(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        remaining = _parse_remaining(d.pop("remaining"))

        team_quota_status = cls(
            team_id=team_id,
            key=key,
            kind=kind,
            unit=unit,
            source=source,
            policy=policy,
            committed=committed,
            reserved=reserved,
            used=used,
            remaining=remaining,
        )

        team_quota_status.additional_properties = d
        return team_quota_status

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
