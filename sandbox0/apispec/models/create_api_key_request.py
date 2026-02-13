from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_api_key_request_type import CreateAPIKeyRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAPIKeyRequest")


@_attrs_define
class CreateAPIKeyRequest:
    """
    Attributes:
        name (str):
        type_ (CreateAPIKeyRequestType):
        roles (Union[Unset, list[str]]):
        expires_in (Union[Unset, str]): 30d, 90d, 180d, 365d, or never
    """

    name: str
    type_: CreateAPIKeyRequestType
    roles: Union[Unset, list[str]] = UNSET
    expires_in: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if roles is not UNSET:
            field_dict["roles"] = roles
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = CreateAPIKeyRequestType(d.pop("type"))

        roles = cast(list[str], d.pop("roles", UNSET))

        expires_in = d.pop("expires_in", UNSET)

        create_api_key_request = cls(
            name=name,
            type_=type_,
            roles=roles,
            expires_in=expires_in,
        )

        create_api_key_request.additional_properties = d
        return create_api_key_request

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
