from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.app_armor_profile_type import AppArmorProfileType
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="AppArmorProfile")



@_attrs_define
class AppArmorProfile:
    """ 
        Attributes:
            type_ (AppArmorProfileType):
            localhost_profile (Union[Unset, str]):
     """

    type_: AppArmorProfileType
    localhost_profile: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        localhost_profile = self.localhost_profile


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if localhost_profile is not UNSET:
            field_dict["localhostProfile"] = localhost_profile

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AppArmorProfileType(d.pop("type"))




        localhost_profile = d.pop("localhostProfile", UNSET)

        app_armor_profile = cls(
            type_=type_,
            localhost_profile=localhost_profile,
        )


        app_armor_profile.additional_properties = d
        return app_armor_profile

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
