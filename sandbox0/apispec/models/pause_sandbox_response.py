from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_resource_usage import SandboxResourceUsage


T = TypeVar("T", bound="PauseSandboxResponse")


@_attrs_define
class PauseSandboxResponse:
    """
    Attributes:
        sandbox_id (str):
        paused (bool):
        resource_usage (Union[Unset, SandboxResourceUsage]):
        updated_memory (Union[Unset, str]):
        updated_cpu (Union[Unset, str]):
    """

    sandbox_id: str
    paused: bool
    resource_usage: Union[Unset, "SandboxResourceUsage"] = UNSET
    updated_memory: Union[Unset, str] = UNSET
    updated_cpu: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        paused = self.paused

        resource_usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resource_usage, Unset):
            resource_usage = self.resource_usage.to_dict()

        updated_memory = self.updated_memory

        updated_cpu = self.updated_cpu

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "paused": paused,
            }
        )
        if resource_usage is not UNSET:
            field_dict["resource_usage"] = resource_usage
        if updated_memory is not UNSET:
            field_dict["updated_memory"] = updated_memory
        if updated_cpu is not UNSET:
            field_dict["updated_cpu"] = updated_cpu

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_resource_usage import SandboxResourceUsage

        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        paused = d.pop("paused")

        _resource_usage = d.pop("resource_usage", UNSET)
        resource_usage: Union[Unset, SandboxResourceUsage]
        if isinstance(_resource_usage, Unset):
            resource_usage = UNSET
        else:
            resource_usage = SandboxResourceUsage.from_dict(_resource_usage)

        updated_memory = d.pop("updated_memory", UNSET)

        updated_cpu = d.pop("updated_cpu", UNSET)

        pause_sandbox_response = cls(
            sandbox_id=sandbox_id,
            paused=paused,
            resource_usage=resource_usage,
            updated_memory=updated_memory,
            updated_cpu=updated_cpu,
        )

        pause_sandbox_response.additional_properties = d
        return pause_sandbox_response

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
