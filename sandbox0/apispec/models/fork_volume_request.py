from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volume_access_mode import VolumeAccessMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ForkVolumeRequest")


@_attrs_define
class ForkVolumeRequest:
    """
    Attributes:
        cache_size (Union[Unset, str]):
        prefetch (Union[Unset, int]):
        buffer_size (Union[Unset, str]):
        writeback (Union[Unset, bool]):
        access_mode (Union[Unset, VolumeAccessMode]): Access mode for sandbox volumes. Enforcement is scoped to storage-
            proxy instances. RWO allows read-write mounts on a single instance; ROX allows read-only mounts across
            instances; RWX allows read-write mounts across instances.
    """

    cache_size: Union[Unset, str] = UNSET
    prefetch: Union[Unset, int] = UNSET
    buffer_size: Union[Unset, str] = UNSET
    writeback: Union[Unset, bool] = UNSET
    access_mode: Union[Unset, VolumeAccessMode] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache_size = self.cache_size

        prefetch = self.prefetch

        buffer_size = self.buffer_size

        writeback = self.writeback

        access_mode: Union[Unset, str] = UNSET
        if not isinstance(self.access_mode, Unset):
            access_mode = self.access_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cache_size is not UNSET:
            field_dict["cache_size"] = cache_size
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch
        if buffer_size is not UNSET:
            field_dict["buffer_size"] = buffer_size
        if writeback is not UNSET:
            field_dict["writeback"] = writeback
        if access_mode is not UNSET:
            field_dict["access_mode"] = access_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cache_size = d.pop("cache_size", UNSET)

        prefetch = d.pop("prefetch", UNSET)

        buffer_size = d.pop("buffer_size", UNSET)

        writeback = d.pop("writeback", UNSET)

        _access_mode = d.pop("access_mode", UNSET)
        access_mode: Union[Unset, VolumeAccessMode]
        if isinstance(_access_mode, Unset):
            access_mode = UNSET
        else:
            access_mode = VolumeAccessMode(_access_mode)

        fork_volume_request = cls(
            cache_size=cache_size,
            prefetch=prefetch,
            buffer_size=buffer_size,
            writeback=writeback,
            access_mode=access_mode,
        )

        fork_volume_request.additional_properties = d
        return fork_volume_request

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
