from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resolve_volume_sync_conflict_request_status import (
    ResolveVolumeSyncConflictRequestStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolveVolumeSyncConflictRequest")


@_attrs_define
class ResolveVolumeSyncConflictRequest:
    """
    Attributes:
        status (ResolveVolumeSyncConflictRequestStatus):
        resolution (Union[Unset, str]):
        note (Union[Unset, str]):
    """

    status: ResolveVolumeSyncConflictRequestStatus
    resolution: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        resolution = self.resolution

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ResolveVolumeSyncConflictRequestStatus(d.pop("status"))

        resolution = d.pop("resolution", UNSET)

        note = d.pop("note", UNSET)

        resolve_volume_sync_conflict_request = cls(
            status=status,
            resolution=resolution,
            note=note,
        )

        resolve_volume_sync_conflict_request.additional_properties = d
        return resolve_volume_sync_conflict_request

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
