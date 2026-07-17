from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxResourceConfig")


@_attrs_define
class SandboxResourceConfig:
    """Instance-level sandbox resource override. Sandbox0 exposes memory only and derives CPU from the platform memory-per-
    CPU ratio, with a minimum CPU limit of 150m.

        Attributes:
            memory (Union[Unset, str]): Sandbox memory limit. Must be at least 128Mi and no more than the platform sandbox
                maximum, which defaults to 32Gi.
    """

    memory: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memory = d.pop("memory", UNSET)

        sandbox_resource_config = cls(
            memory=memory,
        )

        sandbox_resource_config.additional_properties = d
        return sandbox_resource_config

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
