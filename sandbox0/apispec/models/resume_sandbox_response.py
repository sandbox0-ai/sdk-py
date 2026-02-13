from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResumeSandboxResponse")


@_attrs_define
class ResumeSandboxResponse:
    """
    Attributes:
        sandbox_id (str):
        resumed (bool):
        restored_memory (Union[Unset, str]):
    """

    sandbox_id: str
    resumed: bool
    restored_memory: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        resumed = self.resumed

        restored_memory = self.restored_memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "resumed": resumed,
            }
        )
        if restored_memory is not UNSET:
            field_dict["restored_memory"] = restored_memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        resumed = d.pop("resumed")

        restored_memory = d.pop("restored_memory", UNSET)

        resume_sandbox_response = cls(
            sandbox_id=sandbox_id,
            resumed=resumed,
            restored_memory=restored_memory,
        )

        resume_sandbox_response.additional_properties = d
        return resume_sandbox_response

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
