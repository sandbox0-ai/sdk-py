from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Toleration")


@_attrs_define
class Toleration:
    """
    Attributes:
        key (Union[Unset, str]):
        operator (Union[Unset, str]):
        value (Union[Unset, str]):
        effect (Union[Unset, str]):
    """

    key: Union[Unset, str] = UNSET
    operator: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    effect: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        operator = self.operator

        value = self.value

        effect = self.effect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value
        if effect is not UNSET:
            field_dict["effect"] = effect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        operator = d.pop("operator", UNSET)

        value = d.pop("value", UNSET)

        effect = d.pop("effect", UNSET)

        toleration = cls(
            key=key,
            operator=operator,
            value=value,
            effect=effect,
        )

        toleration.additional_properties = d
        return toleration

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
