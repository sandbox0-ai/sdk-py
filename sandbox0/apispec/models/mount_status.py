from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mount_status_state import MountStatusState
from ..types import UNSET, Unset

T = TypeVar("T", bound="MountStatus")


@_attrs_define
class MountStatus:
    """
    Attributes:
        sandboxvolume_id (str):
        mount_point (str):
        state (MountStatusState):
        mounted_at (Union[Unset, str]):
        mounted_duration_sec (Union[Unset, int]):
        mount_session_id (Union[Unset, str]):
        error_code (Union[Unset, str]):
        error_message (Union[Unset, str]):
    """

    sandboxvolume_id: str
    mount_point: str
    state: MountStatusState
    mounted_at: Union[Unset, str] = UNSET
    mounted_duration_sec: Union[Unset, int] = UNSET
    mount_session_id: Union[Unset, str] = UNSET
    error_code: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandboxvolume_id = self.sandboxvolume_id

        mount_point = self.mount_point

        state = self.state.value

        mounted_at = self.mounted_at

        mounted_duration_sec = self.mounted_duration_sec

        mount_session_id = self.mount_session_id

        error_code = self.error_code

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandboxvolume_id": sandboxvolume_id,
                "mount_point": mount_point,
                "state": state,
            }
        )
        if mounted_at is not UNSET:
            field_dict["mounted_at"] = mounted_at
        if mounted_duration_sec is not UNSET:
            field_dict["mounted_duration_sec"] = mounted_duration_sec
        if mount_session_id is not UNSET:
            field_dict["mount_session_id"] = mount_session_id
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandboxvolume_id = d.pop("sandboxvolume_id")

        mount_point = d.pop("mount_point")

        state = MountStatusState(d.pop("state"))

        mounted_at = d.pop("mounted_at", UNSET)

        mounted_duration_sec = d.pop("mounted_duration_sec", UNSET)

        mount_session_id = d.pop("mount_session_id", UNSET)

        error_code = d.pop("error_code", UNSET)

        error_message = d.pop("error_message", UNSET)

        mount_status = cls(
            sandboxvolume_id=sandboxvolume_id,
            mount_point=mount_point,
            state=state,
            mounted_at=mounted_at,
            mounted_duration_sec=mounted_duration_sec,
            mount_session_id=mount_session_id,
            error_code=error_code,
            error_message=error_message,
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
