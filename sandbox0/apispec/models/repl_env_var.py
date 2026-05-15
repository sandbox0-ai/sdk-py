from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="REPLEnvVar")


@_attrs_define
class REPLEnvVar:
    """
    Attributes:
        name (str):
        value (Union[Unset, str]):
        value_from (Union[Unset, str]):
    """

    name: str
    value: Union[Unset, str] = UNSET
    value_from: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        value_from = self.value_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if value_from is not UNSET:
            field_dict["value_from"] = value_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value", UNSET)

        value_from = d.pop("value_from", UNSET)

        repl_env_var = cls(
            name=name,
            value=value,
            value_from=value_from,
        )

        repl_env_var.additional_properties = d
        return repl_env_var

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
