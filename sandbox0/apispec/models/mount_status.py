from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MountStatus")


@_attrs_define
class MountStatus:
    """
    Attributes:
        sandboxvolume_id (Union[Unset, str]):
        mount_point (Union[Unset, str]):
        mounted_at (Union[Unset, str]):
        mounted_duration_sec (Union[Unset, int]):
    """

    sandboxvolume_id: Union[Unset, str] = UNSET
    mount_point: Union[Unset, str] = UNSET
    mounted_at: Union[Unset, str] = UNSET
    mounted_duration_sec: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandboxvolume_id = self.sandboxvolume_id

        mount_point = self.mount_point

        mounted_at = self.mounted_at

        mounted_duration_sec = self.mounted_duration_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandboxvolume_id is not UNSET:
            field_dict["sandboxvolume_id"] = sandboxvolume_id
        if mount_point is not UNSET:
            field_dict["mount_point"] = mount_point
        if mounted_at is not UNSET:
            field_dict["mounted_at"] = mounted_at
        if mounted_duration_sec is not UNSET:
            field_dict["mounted_duration_sec"] = mounted_duration_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandboxvolume_id = d.pop("sandboxvolume_id", UNSET)

        mount_point = d.pop("mount_point", UNSET)

        mounted_at = d.pop("mounted_at", UNSET)

        mounted_duration_sec = d.pop("mounted_duration_sec", UNSET)

        mount_status = cls(
            sandboxvolume_id=sandboxvolume_id,
            mount_point=mount_point,
            mounted_at=mounted_at,
            mounted_duration_sec=mounted_duration_sec,
        )

        mount_status.additional_properties = d
        return mount_status

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
