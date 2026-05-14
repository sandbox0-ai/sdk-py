from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="HTTPValueMatch")



@_attrs_define
class HTTPValueMatch:
    """ 
        Attributes:
            name (str): Header or query parameter name.
            values (Union[Unset, list[str]]): Accepted values. Empty with present=true requires only presence.
            present (Union[Unset, bool]): When true and values is empty, only parameter/header presence is required.
     """

    name: str
    values: Union[Unset, list[str]] = UNSET
    present: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values



        present = self.present


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if values is not UNSET:
            field_dict["values"] = values
        if present is not UNSET:
            field_dict["present"] = present

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        values = cast(list[str], d.pop("values", UNSET))


        present = d.pop("present", UNSET)

        http_value_match = cls(
            name=name,
            values=values,
            present=present,
        )


        http_value_match.additional_properties = d
        return http_value_match

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
