from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.volume_access_mode import VolumeAccessMode
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="SandboxVolume")



@_attrs_define
class SandboxVolume:
    """ 
        Attributes:
            id (str):
            team_id (str):
            user_id (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            source_volume_id (Union[None, Unset, str]):
            default_posix_uid (Union[None, Unset, int]):
            default_posix_gid (Union[None, Unset, int]):
            access_mode (Union[Unset, VolumeAccessMode]): Access mode for sandbox volumes. Enforcement is scoped to storage-
                proxy instances. RWO allows read-write mounts on a single instance; ROX allows read-only mounts across
                instances; RWX allows read-write mounts across instances.
     """

    id: str
    team_id: str
    user_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    source_volume_id: Union[None, Unset, str] = UNSET
    default_posix_uid: Union[None, Unset, int] = UNSET
    default_posix_gid: Union[None, Unset, int] = UNSET
    access_mode: Union[Unset, VolumeAccessMode] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        user_id = self.user_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        source_volume_id: Union[None, Unset, str]
        if isinstance(self.source_volume_id, Unset):
            source_volume_id = UNSET
        else:
            source_volume_id = self.source_volume_id

        default_posix_uid: Union[None, Unset, int]
        if isinstance(self.default_posix_uid, Unset):
            default_posix_uid = UNSET
        else:
            default_posix_uid = self.default_posix_uid

        default_posix_gid: Union[None, Unset, int]
        if isinstance(self.default_posix_gid, Unset):
            default_posix_gid = UNSET
        else:
            default_posix_gid = self.default_posix_gid

        access_mode: Union[Unset, str] = UNSET
        if not isinstance(self.access_mode, Unset):
            access_mode = self.access_mode.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "team_id": team_id,
            "user_id": user_id,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if source_volume_id is not UNSET:
            field_dict["source_volume_id"] = source_volume_id
        if default_posix_uid is not UNSET:
            field_dict["default_posix_uid"] = default_posix_uid
        if default_posix_gid is not UNSET:
            field_dict["default_posix_gid"] = default_posix_gid
        if access_mode is not UNSET:
            field_dict["access_mode"] = access_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        user_id = d.pop("user_id")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        def _parse_source_volume_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_volume_id = _parse_source_volume_id(d.pop("source_volume_id", UNSET))


        def _parse_default_posix_uid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_posix_uid = _parse_default_posix_uid(d.pop("default_posix_uid", UNSET))


        def _parse_default_posix_gid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_posix_gid = _parse_default_posix_gid(d.pop("default_posix_gid", UNSET))


        _access_mode = d.pop("access_mode", UNSET)
        access_mode: Union[Unset, VolumeAccessMode]
        if isinstance(_access_mode,  Unset):
            access_mode = UNSET
        else:
            access_mode = VolumeAccessMode(_access_mode)




        sandbox_volume = cls(
            id=id,
            team_id=team_id,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            source_volume_id=source_volume_id,
            default_posix_uid=default_posix_uid,
            default_posix_gid=default_posix_gid,
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
