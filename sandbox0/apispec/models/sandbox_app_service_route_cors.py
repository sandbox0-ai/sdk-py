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

T = TypeVar("T", bound="SandboxAppServiceRouteCORS")


@_attrs_define
class SandboxAppServiceRouteCORS:
    """
    Attributes:
        allowed_origins (Union[Unset, list[str]]):
        allowed_methods (Union[Unset, list[str]]):
        allowed_headers (Union[Unset, list[str]]):
        expose_headers (Union[Unset, list[str]]):
        allow_credentials (Union[Unset, bool]):
        max_age_seconds (Union[Unset, int]):
    """

    allowed_origins: Union[Unset, list[str]] = UNSET
    allowed_methods: Union[Unset, list[str]] = UNSET
    allowed_headers: Union[Unset, list[str]] = UNSET
    expose_headers: Union[Unset, list[str]] = UNSET
    allow_credentials: Union[Unset, bool] = UNSET
    max_age_seconds: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_origins: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_origins, Unset):
            allowed_origins = self.allowed_origins

        allowed_methods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_methods, Unset):
            allowed_methods = self.allowed_methods

        allowed_headers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_headers, Unset):
            allowed_headers = self.allowed_headers

        expose_headers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.expose_headers, Unset):
            expose_headers = self.expose_headers

        allow_credentials = self.allow_credentials

        max_age_seconds = self.max_age_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_origins is not UNSET:
            field_dict["allowed_origins"] = allowed_origins
        if allowed_methods is not UNSET:
            field_dict["allowed_methods"] = allowed_methods
        if allowed_headers is not UNSET:
            field_dict["allowed_headers"] = allowed_headers
        if expose_headers is not UNSET:
            field_dict["expose_headers"] = expose_headers
        if allow_credentials is not UNSET:
            field_dict["allow_credentials"] = allow_credentials
        if max_age_seconds is not UNSET:
            field_dict["max_age_seconds"] = max_age_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_origins = cast(list[str], d.pop("allowed_origins", UNSET))

        allowed_methods = cast(list[str], d.pop("allowed_methods", UNSET))

        allowed_headers = cast(list[str], d.pop("allowed_headers", UNSET))

        expose_headers = cast(list[str], d.pop("expose_headers", UNSET))

        allow_credentials = d.pop("allow_credentials", UNSET)

        max_age_seconds = d.pop("max_age_seconds", UNSET)

        sandbox_app_service_route_cors = cls(
            allowed_origins=allowed_origins,
            allowed_methods=allowed_methods,
            allowed_headers=allowed_headers,
            expose_headers=expose_headers,
            allow_credentials=allow_credentials,
            max_age_seconds=max_age_seconds,
        )

        sandbox_app_service_route_cors.additional_properties = d
        return sandbox_app_service_route_cors

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
