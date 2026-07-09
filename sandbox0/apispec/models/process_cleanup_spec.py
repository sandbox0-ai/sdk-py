from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessCleanupSpec")


@_attrs_define
class ProcessCleanupSpec:
    """
    Attributes:
        idle_timeout_sec (Union[Unset, int]):
        ttl_sec (Union[Unset, int]):
    """

    idle_timeout_sec: Union[Unset, int] = UNSET
    ttl_sec: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idle_timeout_sec = self.idle_timeout_sec

        ttl_sec = self.ttl_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idle_timeout_sec is not UNSET:
            field_dict["idle_timeout_sec"] = idle_timeout_sec
        if ttl_sec is not UNSET:
            field_dict["ttl_sec"] = ttl_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idle_timeout_sec = d.pop("idle_timeout_sec", UNSET)

        ttl_sec = d.pop("ttl_sec", UNSET)

        process_cleanup_spec = cls(
            idle_timeout_sec=idle_timeout_sec,
            ttl_sec=ttl_sec,
        )

        process_cleanup_spec.additional_properties = d
        return process_cleanup_spec

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
