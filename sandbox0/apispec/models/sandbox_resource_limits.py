from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxResourceLimits")


@_attrs_define
class SandboxResourceLimits:
    """
    Attributes:
        memory (str): Memory limit used by default when a sandbox claim does not provide a memory override. Sandbox0
            derives the internal CPU limit from platform configuration.
        ephemeral_storage (Union[Unset, str]): Ephemeral storage limit for the sandbox writable layer and container
            logs. Defaults to 8Gi when omitted.
    """

    memory: str
    ephemeral_storage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        ephemeral_storage = self.ephemeral_storage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memory": memory,
            }
        )
        if ephemeral_storage is not UNSET:
            field_dict["ephemeralStorage"] = ephemeral_storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memory = d.pop("memory")

        ephemeral_storage = d.pop("ephemeralStorage", UNSET)

        sandbox_resource_limits = cls(
            memory=memory,
            ephemeral_storage=ephemeral_storage,
        )

        sandbox_resource_limits.additional_properties = d
        return sandbox_resource_limits

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
