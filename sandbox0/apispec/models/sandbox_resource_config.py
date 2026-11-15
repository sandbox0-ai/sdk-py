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
    """Instance-level sandbox resource override. CPU is derived from base memory; optional preauthorized memory burst does
    not increase CPU.

        Attributes:
            memory (Union[Unset, str]): Base sandbox memory. Must be at least 128Mi. Base memory plus any burst allowance
                must not exceed the platform sandbox maximum, which defaults to 16Gi. CPU is derived from this base.
            memory_burst_percent (Union[Unset, int]): Optional preauthorized memory allowance, as a percentage of base
                memory (0 disables it).
                With memory 4Gi and memory_burst_percent 50, the hard memory limit may grow from 4Gi
                to 6Gi under pressure and return to 4Gi when safe; CPU remains derived from 4Gi. This does not preallocate
                physical RAM or guarantee
                capacity under host pressure. Automatic burst transitions preserve processes and are billed at the applied
                memory limit.
                Explicitly changing the resource configuration uses the existing process-restarting resize.
    """

    memory: Union[Unset, str] = UNSET
    memory_burst_percent: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        memory_burst_percent = self.memory_burst_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memory is not UNSET:
            field_dict["memory"] = memory
        if memory_burst_percent is not UNSET:
            field_dict["memory_burst_percent"] = memory_burst_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memory = d.pop("memory", UNSET)

        memory_burst_percent = d.pop("memory_burst_percent", UNSET)

        sandbox_resource_config = cls(
            memory=memory,
            memory_burst_percent=memory_burst_percent,
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
