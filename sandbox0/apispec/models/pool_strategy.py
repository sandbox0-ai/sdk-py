from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PoolStrategy")


@_attrs_define
class PoolStrategy:
    """
    Attributes:
        min_idle (int):
        max_idle (int):
        auto_scale (bool):
    """

    min_idle: int
    max_idle: int
    auto_scale: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_idle = self.min_idle

        max_idle = self.max_idle

        auto_scale = self.auto_scale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "minIdle": min_idle,
                "maxIdle": max_idle,
                "autoScale": auto_scale,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_idle = d.pop("minIdle")

        max_idle = d.pop("maxIdle")

        auto_scale = d.pop("autoScale")

        pool_strategy = cls(
            min_idle=min_idle,
            max_idle=max_idle,
            auto_scale=auto_scale,
        )

        pool_strategy.additional_properties = d
        return pool_strategy

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
