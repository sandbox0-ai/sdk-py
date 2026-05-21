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

T = TypeVar("T", bound="CreateTeamRequest")


@_attrs_define
class CreateTeamRequest:
    """
    Attributes:
        name (str):
        slug (Union[Unset, str]):
        home_region_id (Union[None, Unset, str]):
    """

    name: str
    slug: Union[Unset, str] = UNSET
    home_region_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        home_region_id: Union[None, Unset, str]
        if isinstance(self.home_region_id, Unset):
            home_region_id = UNSET
        else:
            home_region_id = self.home_region_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if home_region_id is not UNSET:
            field_dict["home_region_id"] = home_region_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug", UNSET)

        def _parse_home_region_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        home_region_id = _parse_home_region_id(d.pop("home_region_id", UNSET))

        create_team_request = cls(
            name=name,
            slug=slug,
            home_region_id=home_region_id,
        )

        create_team_request.additional_properties = d
        return create_team_request

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
