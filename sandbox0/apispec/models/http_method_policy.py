from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="HTTPMethodPolicy")



@_attrs_define
class HTTPMethodPolicy:
    """ HTTP method allow and deny lists.

        Attributes:
            allowed (Union[Unset, list[str]]): When non-empty, only listed HTTP methods are allowed.
            denied (Union[Unset, list[str]]): HTTP methods that are always denied before allowed is evaluated.
     """

    allowed: Union[Unset, list[str]] = UNSET
    denied: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allowed: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = self.allowed



        denied: Union[Unset, list[str]] = UNSET
        if not isinstance(self.denied, Unset):
            denied = self.denied




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if denied is not UNSET:
            field_dict["denied"] = denied

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed = cast(list[str], d.pop("allowed", UNSET))


        denied = cast(list[str], d.pop("denied", UNSET))


        http_method_policy = cls(
            allowed=allowed,
            denied=denied,
        )


        http_method_policy.additional_properties = d
        return http_method_policy

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
