import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (str):
        email (str):
        name (str):
        email_verified (bool):
        is_admin (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        avatar_url (Union[None, Unset, str]):
        default_team_id (Union[None, Unset, str]):
    """

    id: str
    email: str
    name: str
    email_verified: bool
    is_admin: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    avatar_url: Union[None, Unset, str] = UNSET
    default_team_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name = self.name

        email_verified = self.email_verified

        is_admin = self.is_admin

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        avatar_url: Union[None, Unset, str]
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        default_team_id: Union[None, Unset, str]
        if isinstance(self.default_team_id, Unset):
            default_team_id = UNSET
        else:
            default_team_id = self.default_team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "name": name,
                "email_verified": email_verified,
                "is_admin": is_admin,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if default_team_id is not UNSET:
            field_dict["default_team_id"] = default_team_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        email_verified = d.pop("email_verified")

        is_admin = d.pop("is_admin")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_avatar_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        def _parse_default_team_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_team_id = _parse_default_team_id(d.pop("default_team_id", UNSET))

        user = cls(
            id=id,
            email=email,
            name=name,
            email_verified=email_verified,
            is_admin=is_admin,
            created_at=created_at,
            updated_at=updated_at,
            avatar_url=avatar_url,
            default_team_id=default_team_id,
        )

        user.additional_properties = d
        return user

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
