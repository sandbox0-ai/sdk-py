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

T = TypeVar("T", bound="UpdateUserRequest")


@_attrs_define
class UpdateUserRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        avatar_url (Union[Unset, str]):
        default_team_id (Union[None, Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    default_team_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        avatar_url = self.avatar_url

        default_team_id: Union[None, Unset, str]
        if isinstance(self.default_team_id, Unset):
            default_team_id = UNSET
        else:
            default_team_id = self.default_team_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if default_team_id is not UNSET:
            field_dict["default_team_id"] = default_team_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        def _parse_default_team_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_team_id = _parse_default_team_id(d.pop("default_team_id", UNSET))

        update_user_request = cls(
            name=name,
            avatar_url=avatar_url,
            default_team_id=default_team_id,
        )

        update_user_request.additional_properties = d
        return update_user_request

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
