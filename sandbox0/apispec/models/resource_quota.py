from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ResourceQuota")



@_attrs_define
class ResourceQuota:
    """ 
        Attributes:
            cpu (Union[Unset, str]):
            memory (Union[Unset, str]):
            ephemeral_storage (Union[Unset, str]): Ephemeral storage limit for the sandbox writable layer and container
                logs. Defaults to 512Mi when omitted.
     """

    cpu: Union[Unset, str] = UNSET
    memory: Union[Unset, str] = UNSET
    ephemeral_storage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu

        memory = self.memory

        ephemeral_storage = self.ephemeral_storage


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if memory is not UNSET:
            field_dict["memory"] = memory
        if ephemeral_storage is not UNSET:
            field_dict["ephemeralStorage"] = ephemeral_storage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpu = d.pop("cpu", UNSET)

        memory = d.pop("memory", UNSET)

        ephemeral_storage = d.pop("ephemeralStorage", UNSET)

        resource_quota = cls(
            cpu=cpu,
            memory=memory,
            ephemeral_storage=ephemeral_storage,
        )


        resource_quota.additional_properties = d
        return resource_quota

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
