from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sandbox_app_service_route_auth_mode import SandboxAppServiceRouteAuthMode
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="SandboxAppServiceRouteAuth")



@_attrs_define
class SandboxAppServiceRouteAuth:
    """ 
        Attributes:
            mode (SandboxAppServiceRouteAuthMode):  Default: SandboxAppServiceRouteAuthMode.NONE.
            bearer_token_sha256 (Union[Unset, str]): Hex SHA-256 of the accepted bearer token. Required when mode is bearer.
            header_name (Union[Unset, str]): Required header name when mode is header.
            header_value_sha256 (Union[Unset, str]): Hex SHA-256 of the required header value when mode is header.
     """

    mode: SandboxAppServiceRouteAuthMode = SandboxAppServiceRouteAuthMode.NONE
    bearer_token_sha256: Union[Unset, str] = UNSET
    header_name: Union[Unset, str] = UNSET
    header_value_sha256: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        bearer_token_sha256 = self.bearer_token_sha256

        header_name = self.header_name

        header_value_sha256 = self.header_value_sha256


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mode": mode,
        })
        if bearer_token_sha256 is not UNSET:
            field_dict["bearer_token_sha256"] = bearer_token_sha256
        if header_name is not UNSET:
            field_dict["header_name"] = header_name
        if header_value_sha256 is not UNSET:
            field_dict["header_value_sha256"] = header_value_sha256

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = SandboxAppServiceRouteAuthMode(d.pop("mode"))




        bearer_token_sha256 = d.pop("bearer_token_sha256", UNSET)

        header_name = d.pop("header_name", UNSET)

        header_value_sha256 = d.pop("header_value_sha256", UNSET)

        sandbox_app_service_route_auth = cls(
            mode=mode,
            bearer_token_sha256=bearer_token_sha256,
            header_name=header_name,
            header_value_sha256=header_value_sha256,
        )


        sandbox_app_service_route_auth.additional_properties = d
        return sandbox_app_service_route_auth

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
