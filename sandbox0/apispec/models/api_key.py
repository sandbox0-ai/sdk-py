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

T = TypeVar("T", bound="APIKey")


@_attrs_define
class APIKey:
    """
    Attributes:
        id (str):
        team_id (str):
        created_by (str):
        name (str):
        type_ (str):
        roles (list[str]):
        is_active (bool):
        expires_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        key_value (Union[Unset, str]):
        user_id (Union[None, Unset, str]):
        last_used_at (Union[Unset, datetime.datetime]):
        usage_count (Union[Unset, int]):
    """

    id: str
    team_id: str
    created_by: str
    name: str
    type_: str
    roles: list[str]
    is_active: bool
    expires_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    key_value: Union[Unset, str] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    last_used_at: Union[Unset, datetime.datetime] = UNSET
    usage_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        created_by = self.created_by

        name = self.name

        type_ = self.type_

        roles = self.roles

        is_active = self.is_active

        expires_at = self.expires_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        key_value = self.key_value

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        last_used_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        usage_count = self.usage_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "team_id": team_id,
                "created_by": created_by,
                "name": name,
                "type": type_,
                "roles": roles,
                "is_active": is_active,
                "expires_at": expires_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if key_value is not UNSET:
            field_dict["key_value"] = key_value
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if usage_count is not UNSET:
            field_dict["usage_count"] = usage_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        created_by = d.pop("created_by")

        name = d.pop("name")

        type_ = d.pop("type")

        roles = cast(list[str], d.pop("roles"))

        is_active = d.pop("is_active")

        expires_at = isoparse(d.pop("expires_at"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        key_value = d.pop("key_value", UNSET)

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        _last_used_at = d.pop("last_used_at", UNSET)
        last_used_at: Union[Unset, datetime.datetime]
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = isoparse(_last_used_at)

        usage_count = d.pop("usage_count", UNSET)

        api_key = cls(
            id=id,
            team_id=team_id,
            created_by=created_by,
            name=name,
            type_=type_,
            roles=roles,
            is_active=is_active,
            expires_at=expires_at,
            created_at=created_at,
            updated_at=updated_at,
            key_value=key_value,
            user_id=user_id,
            last_used_at=last_used_at,
            usage_count=usage_count,
        )

        api_key.additional_properties = d
        return api_key

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
