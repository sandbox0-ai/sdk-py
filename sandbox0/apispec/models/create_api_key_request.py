from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAPIKeyRequest")


@_attrs_define
class CreateAPIKeyRequest:
    """
    Attributes:
        name (str):
        scope (Union[Unset, str]): API key scope: team or platform. Defaults to team. platform keys grant system admin
            access, require a system admin user session, and do not support roles.
        roles (Union[Unset, list[str]]): Requested API key roles. Supported roles: admin, developer, builder, viewer.
            The roles must not grant permissions outside the authenticated caller's permissions.
        expires_in (Union[Unset, str]): 30d, 90d, 180d, 365d, or never
    """

    name: str
    scope: Union[Unset, str] = UNSET
    roles: Union[Unset, list[str]] = UNSET
    expires_in: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scope = self.scope

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        expires_in = self.expires_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope
        if roles is not UNSET:
            field_dict["roles"] = roles
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        scope = d.pop("scope", UNSET)

        roles = cast(list[str], d.pop("roles", UNSET))

        expires_in = d.pop("expires_in", UNSET)

        create_api_key_request = cls(
            name=name,
            scope=scope,
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
