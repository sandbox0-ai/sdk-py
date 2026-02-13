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

T = TypeVar("T", bound="CreateAPIKeyResponse")


@_attrs_define
class CreateAPIKeyResponse:
    """
    Attributes:
        id (str):
        name (str):
        type_ (str):
        roles (list[str]):
        team_id (str):
        expires_at (datetime.datetime):
        created_at (datetime.datetime):
        key (Union[Unset, str]):
    """

    id: str
    name: str
    type_: str
    roles: list[str]
    team_id: str
    expires_at: datetime.datetime
    created_at: datetime.datetime
    key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        roles = self.roles

        team_id = self.team_id

        expires_at = self.expires_at.isoformat()

        created_at = self.created_at.isoformat()

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "roles": roles,
                "team_id": team_id,
                "expires_at": expires_at,
                "created_at": created_at,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        roles = cast(list[str], d.pop("roles"))

        team_id = d.pop("team_id")

        expires_at = isoparse(d.pop("expires_at"))

        created_at = isoparse(d.pop("created_at"))

        key = d.pop("key", UNSET)

        create_api_key_response = cls(
            id=id,
            name=name,
            type_=type_,
            roles=roles,
            team_id=team_id,
            expires_at=expires_at,
            created_at=created_at,
            key=key,
        )

        create_api_key_response.additional_properties = d
        return create_api_key_response

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
