from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.volume_access_mode import VolumeAccessMode
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ForkVolumeRequest")



@_attrs_define
class ForkVolumeRequest:
    """ 
        Attributes:
            default_posix_uid (Union[Unset, int]): Override the default POSIX UID for external volume access paths. Inherits
                from the source volume when omitted.
            default_posix_gid (Union[Unset, int]): Override the default POSIX GID for external volume access paths. Inherits
                from the source volume when omitted.
            access_mode (Union[Unset, VolumeAccessMode]): Access mode for sandbox volumes. Enforcement is scoped to storage-
                proxy instances. RWO allows read-write mounts on a single instance; ROX allows read-only mounts across
                instances; RWX allows read-write mounts across instances.
     """

    default_posix_uid: Union[Unset, int] = UNSET
    default_posix_gid: Union[Unset, int] = UNSET
    access_mode: Union[Unset, VolumeAccessMode] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        default_posix_uid = self.default_posix_uid

        default_posix_gid = self.default_posix_gid

        access_mode: Union[Unset, str] = UNSET
        if not isinstance(self.access_mode, Unset):
            access_mode = self.access_mode.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        default_posix_uid = d.pop("default_posix_uid", UNSET)

        default_posix_gid = d.pop("default_posix_gid", UNSET)

        _access_mode = d.pop("access_mode", UNSET)
        access_mode: Union[Unset, VolumeAccessMode]
        if isinstance(_access_mode,  Unset):
            access_mode = UNSET
        else:
            access_mode = VolumeAccessMode(_access_mode)




        fork_volume_request = cls(
            default_posix_uid=default_posix_uid,
            default_posix_gid=default_posix_gid,
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
