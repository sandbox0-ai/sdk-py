from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.team_quota_key import TeamQuotaKey
from ..models.team_quota_kind import TeamQuotaKind
from ..models.team_quota_unit import TeamQuotaUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamQuotaPolicy")


@_attrs_define
class TeamQuotaPolicy:
    """Capacity and concurrency policies use limit. Rate policies use tokens, interval_ms, and burst.

    Attributes:
        team_id (str):
        key (TeamQuotaKey):
        kind (TeamQuotaKind):
        unit (TeamQuotaUnit):
        revision (Union[Unset, int]):
        limit (Union[Unset, int]):
        tokens (Union[Unset, int]):
        interval_ms (Union[Unset, int]):
        burst (Union[Unset, int]):
    """

    team_id: str
    key: TeamQuotaKey
    kind: TeamQuotaKind
    unit: TeamQuotaUnit
    revision: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    tokens: Union[Unset, int] = UNSET
    interval_ms: Union[Unset, int] = UNSET
    burst: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        key = self.key.value

        kind = self.kind.value

        unit = self.unit.value

        revision = self.revision

        limit = self.limit

        tokens = self.tokens

        interval_ms = self.interval_ms

        burst = self.burst

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "key": key,
                "kind": kind,
                "unit": unit,
            }
        )
        if revision is not UNSET:
            field_dict["revision"] = revision
        if limit is not UNSET:
            field_dict["limit"] = limit
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if interval_ms is not UNSET:
            field_dict["interval_ms"] = interval_ms
        if burst is not UNSET:
            field_dict["burst"] = burst

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        key = TeamQuotaKey(d.pop("key"))

        kind = TeamQuotaKind(d.pop("kind"))

        unit = TeamQuotaUnit(d.pop("unit"))

        revision = d.pop("revision", UNSET)

        limit = d.pop("limit", UNSET)

        tokens = d.pop("tokens", UNSET)

        interval_ms = d.pop("interval_ms", UNSET)

        burst = d.pop("burst", UNSET)

        team_quota_policy = cls(
            team_id=team_id,
            key=key,
            kind=kind,
            unit=unit,
            revision=revision,
            limit=limit,
            tokens=tokens,
            interval_ms=interval_ms,
            burst=burst,
        )

        team_quota_policy.additional_properties = d
        return team_quota_policy

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
