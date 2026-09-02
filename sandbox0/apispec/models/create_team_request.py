from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTeamRequest")


@_attrs_define
class CreateTeamRequest:
    """
    Attributes:
        name (str): Display name. Team names are not unique.
        home_region_id (str): Required when creating a team through the global gateway.
        slug (Union[Unset, str]): Human-readable alias. Team slugs are not unique.
    """

    name: str
    home_region_id: str
    slug: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        home_region_id = self.home_region_id

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "home_region_id": home_region_id,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        home_region_id = d.pop("home_region_id")

        slug = d.pop("slug", UNSET)

        create_team_request = cls(
            name=name,
            home_region_id=home_region_id,
            slug=slug,
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
