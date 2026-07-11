from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionEventRetentionSpec")


@_attrs_define
class ExecutionSessionEventRetentionSpec:
    """
    Attributes:
        max_bytes (Union[Unset, int]):  Default: 67108864.
        max_age_seconds (Union[Unset, int]):  Default: 86400.
    """

    max_bytes: Union[Unset, int] = 67108864
    max_age_seconds: Union[Unset, int] = 86400
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_bytes = self.max_bytes

        max_age_seconds = self.max_age_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_bytes is not UNSET:
            field_dict["max_bytes"] = max_bytes
        if max_age_seconds is not UNSET:
            field_dict["max_age_seconds"] = max_age_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_bytes = d.pop("max_bytes", UNSET)

        max_age_seconds = d.pop("max_age_seconds", UNSET)

        execution_session_event_retention_spec = cls(
            max_bytes=max_bytes,
            max_age_seconds=max_age_seconds,
        )

        execution_session_event_retention_spec.additional_properties = d
        return execution_session_event_retention_spec

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
