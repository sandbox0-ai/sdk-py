import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.volume_access_mode import VolumeAccessMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxVolume")


@_attrs_define
class SandboxVolume:
    """
    Attributes:
        id (str):
        team_id (str):
        user_id (str):
        cache_size (str):
        buffer_size (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        prefetch (Union[Unset, int]):
        writeback (Union[Unset, bool]):
        access_mode (Union[Unset, VolumeAccessMode]): Access mode for sandbox volumes. Enforcement is scoped to storage-
            proxy instances. RWO allows read-write mounts on a single instance; ROX allows read-only mounts across
            instances; RWX allows read-write mounts across instances.
    """

    id: str
    team_id: str
    user_id: str
    cache_size: str
    buffer_size: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    prefetch: Union[Unset, int] = UNSET
    writeback: Union[Unset, bool] = UNSET
    access_mode: Union[Unset, VolumeAccessMode] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        user_id = self.user_id

        cache_size = self.cache_size

        buffer_size = self.buffer_size

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        prefetch = self.prefetch

        writeback = self.writeback

        access_mode: Union[Unset, str] = UNSET
        if not isinstance(self.access_mode, Unset):
            access_mode = self.access_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "team_id": team_id,
                "user_id": user_id,
                "cache_size": cache_size,
                "buffer_size": buffer_size,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if prefetch is not UNSET:
            field_dict["prefetch"] = prefetch
        if writeback is not UNSET:
            field_dict["writeback"] = writeback
        if access_mode is not UNSET:
            field_dict["access_mode"] = access_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        user_id = d.pop("user_id")

        cache_size = d.pop("cache_size")

        buffer_size = d.pop("buffer_size")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        prefetch = d.pop("prefetch", UNSET)

        writeback = d.pop("writeback", UNSET)

        _access_mode = d.pop("access_mode", UNSET)
        access_mode: Union[Unset, VolumeAccessMode]
        if isinstance(_access_mode, Unset):
            access_mode = UNSET
        else:
            access_mode = VolumeAccessMode(_access_mode)

        sandbox_volume = cls(
            id=id,
            team_id=team_id,
            user_id=user_id,
            cache_size=cache_size,
            buffer_size=buffer_size,
            created_at=created_at,
            updated_at=updated_at,
            prefetch=prefetch,
            writeback=writeback,
            access_mode=access_mode,
        )

        sandbox_volume.additional_properties = d
        return sandbox_volume

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
