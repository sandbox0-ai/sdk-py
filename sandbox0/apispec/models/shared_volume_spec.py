from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedVolumeSpec")


@_attrs_define
class SharedVolumeSpec:
    """
    Attributes:
        name (str):
        sandbox_volume_id (str):
        mount_path (str):
        cache_size (Union[Unset, str]):
        prefetch (Union[Unset, int]):
        buffer_size (Union[Unset, str]):
        writeback (Union[Unset, bool]):
    """

    name: str
    sandbox_volume_id: str
    mount_path: str
    cache_size: Union[Unset, str] = UNSET
    prefetch: Union[Unset, int] = UNSET
    buffer_size: Union[Unset, str] = UNSET
    writeback: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sandbox_volume_id = self.sandbox_volume_id

        mount_path = self.mount_path

        cache_size = self.cache_size

        prefetch = self.prefetch

        buffer_size = self.buffer_size

        writeback = self.writeback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "sandboxVolumeId": sandbox_volume_id,
                "mountPath": mount_path,
            }
        )
        if cache_size is not UNSET:
            field_dict["cacheSize"] = cache_size
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch
        if buffer_size is not UNSET:
            field_dict["bufferSize"] = buffer_size
        if writeback is not UNSET:
            field_dict["writeback"] = writeback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        sandbox_volume_id = d.pop("sandboxVolumeId")

        mount_path = d.pop("mountPath")

        cache_size = d.pop("cacheSize", UNSET)

        prefetch = d.pop("prefetch", UNSET)

        buffer_size = d.pop("bufferSize", UNSET)

        writeback = d.pop("writeback", UNSET)

        shared_volume_spec = cls(
            name=name,
            sandbox_volume_id=sandbox_volume_id,
            mount_path=mount_path,
            cache_size=cache_size,
            prefetch=prefetch,
            buffer_size=buffer_size,
            writeback=writeback,
        )

        shared_volume_spec.additional_properties = d
        return shared_volume_spec

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
