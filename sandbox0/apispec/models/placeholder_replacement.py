from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.placeholder_substitution_location import PlaceholderSubstitutionLocation

T = TypeVar("T", bound="PlaceholderReplacement")


@_attrs_define
class PlaceholderReplacement:
    """
    Attributes:
        placeholder (str): Opaque sandbox-visible value to replace.
        value_template (str): Template rendered against the resolved credential source payload.
        locations (list[PlaceholderSubstitutionLocation]): HTTP request locations where this placeholder can be
            replaced.
    """

    placeholder: str
    value_template: str
    locations: list[PlaceholderSubstitutionLocation]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        placeholder = self.placeholder

        value_template = self.value_template

        locations = []
        for locations_item_data in self.locations:
            locations_item = locations_item_data.value
            locations.append(locations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "placeholder": placeholder,
                "valueTemplate": value_template,
                "locations": locations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        placeholder = d.pop("placeholder")

        value_template = d.pop("valueTemplate")

        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = PlaceholderSubstitutionLocation(locations_item_data)

            locations.append(locations_item)

        placeholder_replacement = cls(
            placeholder=placeholder,
            value_template=value_template,
            locations=locations,
        )

        placeholder_replacement.additional_properties = d
        return placeholder_replacement

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
