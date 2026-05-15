import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistryCredentials")


@_attrs_define
class RegistryCredentials:
    """
    Attributes:
        provider (str):
        push_registry (str):
        pull_registry (str):
        username (str):
        password (str):
        expires_at (Union[Unset, datetime.datetime]):
    """

    provider: str
    push_registry: str
    pull_registry: str
    username: str
    password: str
    expires_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        push_registry = self.push_registry

        pull_registry = self.pull_registry

        username = self.username

        password = self.password

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "pushRegistry": push_registry,
                "pullRegistry": pull_registry,
                "username": username,
                "password": password,
            }
        )
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider")

        push_registry = d.pop("pushRegistry")

        pull_registry = d.pop("pullRegistry")

        username = d.pop("username")

        password = d.pop("password")

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        registry_credentials = cls(
            provider=provider,
            push_registry=push_registry,
            pull_registry=pull_registry,
            username=username,
            password=password,
            expires_at=expires_at,
        )

        registry_credentials.additional_properties = d
        return registry_credentials

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
