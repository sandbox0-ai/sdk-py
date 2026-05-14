from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="VolumeMountSpec")



@_attrs_define
class VolumeMountSpec:
    """ 
        Attributes:
            name (str):
            mount_path (str):
            read_only (Union[Unset, bool]):
     """

    name: str
    mount_path: str
    read_only: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mount_path = self.mount_path

        read_only = self.read_only


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "mountPath": mount_path,
        })
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        mount_path = d.pop("mountPath")

        read_only = d.pop("readOnly", UNSET)

        volume_mount_spec = cls(
            name=name,
            mount_path=mount_path,
            read_only=read_only,
        )


        volume_mount_spec.additional_properties = d
        return volume_mount_spec

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
