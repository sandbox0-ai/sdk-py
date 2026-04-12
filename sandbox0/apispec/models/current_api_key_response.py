import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CurrentAPIKeyResponse")


@_attrs_define
class CurrentAPIKeyResponse:
    """
    Attributes:
        id (str):
        team_id (str):
        created_by (str):
        roles (list[str]):
        permissions (list[str]):
        is_active (bool):
        expires_at (datetime.datetime):
    """

    id: str
    team_id: str
    created_by: str
    roles: list[str]
    permissions: list[str]
    is_active: bool
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        created_by = self.created_by

        roles = self.roles

        permissions = self.permissions

        is_active = self.is_active

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "team_id": team_id,
                "created_by": created_by,
                "roles": roles,
                "permissions": permissions,
                "is_active": is_active,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        created_by = d.pop("created_by")

        roles = cast(list[str], d.pop("roles"))

        permissions = cast(list[str], d.pop("permissions"))

        is_active = d.pop("is_active")

        expires_at = isoparse(d.pop("expires_at"))

        current_api_key_response = cls(
            id=id,
            team_id=team_id,
            created_by=created_by,
            roles=roles,
            permissions=permissions,
            is_active=is_active,
            expires_at=expires_at,
        )

        current_api_key_response.additional_properties = d
        return current_api_key_response

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
