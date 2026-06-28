from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmptyDirMountSpec")


@_attrs_define
class EmptyDirMountSpec:
    """
    Attributes:
        mount_path (str):
        size_limit (Union[Unset, str]): Optional size limit for the Kubernetes emptyDir volume.
    """

    mount_path: str
    size_limit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mount_path = self.mount_path

        size_limit = self.size_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mountPath": mount_path,
            }
        )
        if size_limit is not UNSET:
            field_dict["sizeLimit"] = size_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mount_path = d.pop("mountPath")

        size_limit = d.pop("sizeLimit", UNSET)

        empty_dir_mount_spec = cls(
            mount_path=mount_path,
            size_limit=size_limit,
        )

        empty_dir_mount_spec.additional_properties = d
        return empty_dir_mount_spec

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
