from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MountResponse")


@_attrs_define
class MountResponse:
    """
    Attributes:
        sandboxvolume_id (str):
        mount_point (str):
        mounted_at (str):
    """

    sandboxvolume_id: str
    mount_point: str
    mounted_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandboxvolume_id = self.sandboxvolume_id

        mount_point = self.mount_point

        mounted_at = self.mounted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandboxvolume_id": sandboxvolume_id,
                "mount_point": mount_point,
                "mounted_at": mounted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandboxvolume_id = d.pop("sandboxvolume_id")

        mount_point = d.pop("mount_point")

        mounted_at = d.pop("mounted_at")

        mount_response = cls(
            sandboxvolume_id=sandboxvolume_id,
            mount_point=mount_point,
            mounted_at=mounted_at,
        )

        mount_response.additional_properties = d
        return mount_response

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
