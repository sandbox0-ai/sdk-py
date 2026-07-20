from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quota_dimension import QuotaDimension
from ..models.team_quota_kind import TeamQuotaKind
from ..models.team_quota_source import TeamQuotaSource
from ..models.team_quota_unit import TeamQuotaUnit

T = TypeVar("T", bound="TeamQuota")


@_attrs_define
class TeamQuota:
    """
    Attributes:
        team_id (str):
        dimension (QuotaDimension):
        kind (TeamQuotaKind):
        limit_value (Union[None, int]):
        interval_ms (Union[None, int]):
        burst_value (Union[None, int]):
        current (Union[None, int]):
        remaining (Union[None, int]):
        unlimited (bool):
        unit (TeamQuotaUnit):
        source (TeamQuotaSource):
    """

    team_id: str
    dimension: QuotaDimension
    kind: TeamQuotaKind
    limit_value: Union[None, int]
    interval_ms: Union[None, int]
    burst_value: Union[None, int]
    current: Union[None, int]
    remaining: Union[None, int]
    unlimited: bool
    unit: TeamQuotaUnit
    source: TeamQuotaSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        dimension = self.dimension.value

        kind = self.kind.value

        limit_value: Union[None, int]
        limit_value = self.limit_value

        interval_ms: Union[None, int]
        interval_ms = self.interval_ms

        burst_value: Union[None, int]
        burst_value = self.burst_value

        current: Union[None, int]
        current = self.current

        remaining: Union[None, int]
        remaining = self.remaining

        unlimited = self.unlimited

        unit = self.unit.value

        source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "dimension": dimension,
                "kind": kind,
                "limit_value": limit_value,
                "interval_ms": interval_ms,
                "burst_value": burst_value,
                "current": current,
                "remaining": remaining,
                "unlimited": unlimited,
                "unit": unit,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        dimension = QuotaDimension(d.pop("dimension"))

        kind = TeamQuotaKind(d.pop("kind"))

        def _parse_limit_value(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        limit_value = _parse_limit_value(d.pop("limit_value"))

        def _parse_interval_ms(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        interval_ms = _parse_interval_ms(d.pop("interval_ms"))

        def _parse_burst_value(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        burst_value = _parse_burst_value(d.pop("burst_value"))

        def _parse_current(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        current = _parse_current(d.pop("current"))

        def _parse_remaining(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        remaining = _parse_remaining(d.pop("remaining"))

        unlimited = d.pop("unlimited")

        unit = TeamQuotaUnit(d.pop("unit"))

        source = TeamQuotaSource(d.pop("source"))

        team_quota = cls(
            team_id=team_id,
            dimension=dimension,
            kind=kind,
            limit_value=limit_value,
            interval_ms=interval_ms,
            burst_value=burst_value,
            current=current,
            remaining=remaining,
            unlimited=unlimited,
            unit=unit,
            source=source,
        )

        team_quota.additional_properties = d
        return team_quota

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
