import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sandbox_runtime_metric_freshness_status import (
    SandboxRuntimeMetricFreshnessStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxRuntimeMetricFreshness")


@_attrs_define
class SandboxRuntimeMetricFreshness:
    """Freshness is measured relative to the requested end_time, including for historical queries.

    Attributes:
        status (SandboxRuntimeMetricFreshnessStatus):
        newest_observed_at (Union[Unset, datetime.datetime]):
        age_seconds (Union[Unset, float]):
    """

    status: SandboxRuntimeMetricFreshnessStatus
    newest_observed_at: Union[Unset, datetime.datetime] = UNSET
    age_seconds: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        newest_observed_at: Union[Unset, str] = UNSET
        if not isinstance(self.newest_observed_at, Unset):
            newest_observed_at = self.newest_observed_at.isoformat()

        age_seconds = self.age_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if newest_observed_at is not UNSET:
            field_dict["newest_observed_at"] = newest_observed_at
        if age_seconds is not UNSET:
            field_dict["age_seconds"] = age_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = SandboxRuntimeMetricFreshnessStatus(d.pop("status"))

        _newest_observed_at = d.pop("newest_observed_at", UNSET)
        newest_observed_at: Union[Unset, datetime.datetime]
        if isinstance(_newest_observed_at, Unset):
            newest_observed_at = UNSET
        else:
            newest_observed_at = isoparse(_newest_observed_at)

        age_seconds = d.pop("age_seconds", UNSET)

        sandbox_runtime_metric_freshness = cls(
            status=status,
            newest_observed_at=newest_observed_at,
            age_seconds=age_seconds,
        )

        sandbox_runtime_metric_freshness.additional_properties = d
        return sandbox_runtime_metric_freshness

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
