import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team import Team


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
        default_team (Union['Team', None, Unset]):
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
    default_team: Union["Team", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.team import Team

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

        default_team: Union[None, Unset, dict[str, Any]]
        if isinstance(self.default_team, Unset):
            default_team = UNSET
        elif isinstance(self.default_team, Team):
            default_team = self.default_team.to_dict()
        else:
            default_team = self.default_team

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
        if default_team is not UNSET:
            field_dict["default_team"] = default_team

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team import Team

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

        def _parse_default_team(data: object) -> Union["Team", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_team_type_1 = Team.from_dict(data)

                return default_team_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Team", None, Unset], data)

        default_team = _parse_default_team(d.pop("default_team", UNSET))

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
            default_team=default_team,
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
