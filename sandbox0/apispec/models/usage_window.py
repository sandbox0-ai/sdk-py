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

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageWindow")


@_attrs_define
class UsageWindow:
    """
    Attributes:
        window_id (str):
        window_type (str):
        subject_type (str):
        subject_id (str):
        window_start (datetime.datetime):
        window_end (datetime.datetime):
        value (int):
        unit (str):
        recorded_at (datetime.datetime):
        region_id (Union[Unset, str]):
        cluster_id (Union[Unset, str]):
        sandbox_id (Union[Unset, str]):
    """

    window_id: str
    window_type: str
    subject_type: str
    subject_id: str
    window_start: datetime.datetime
    window_end: datetime.datetime
    value: int
    unit: str
    recorded_at: datetime.datetime
    region_id: Union[Unset, str] = UNSET
    cluster_id: Union[Unset, str] = UNSET
    sandbox_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window_id = self.window_id

        window_type = self.window_type

        subject_type = self.subject_type

        subject_id = self.subject_id

        window_start = self.window_start.isoformat()

        window_end = self.window_end.isoformat()

        value = self.value

        unit = self.unit

        recorded_at = self.recorded_at.isoformat()

        region_id = self.region_id

        cluster_id = self.cluster_id

        sandbox_id = self.sandbox_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window_id": window_id,
                "window_type": window_type,
                "subject_type": subject_type,
                "subject_id": subject_id,
                "window_start": window_start,
                "window_end": window_end,
                "value": value,
                "unit": unit,
                "recorded_at": recorded_at,
            }
        )
        if region_id is not UNSET:
            field_dict["region_id"] = region_id
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        window_id = d.pop("window_id")

        window_type = d.pop("window_type")

        subject_type = d.pop("subject_type")

        subject_id = d.pop("subject_id")

        window_start = isoparse(d.pop("window_start"))

        window_end = isoparse(d.pop("window_end"))

        value = d.pop("value")

        unit = d.pop("unit")

        recorded_at = isoparse(d.pop("recorded_at"))

        region_id = d.pop("region_id", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        sandbox_id = d.pop("sandbox_id", UNSET)

        usage_window = cls(
            window_id=window_id,
            window_type=window_type,
            subject_type=subject_type,
            subject_id=subject_id,
            window_start=window_start,
            window_end=window_end,
            value=value,
            unit=unit,
            recorded_at=recorded_at,
            region_id=region_id,
            cluster_id=cluster_id,
            sandbox_id=sandbox_id,
        )

        usage_window.additional_properties = d
        return usage_window

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
