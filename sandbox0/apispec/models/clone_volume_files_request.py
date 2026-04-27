from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clone_volume_files_request_mode import CloneVolumeFilesRequestMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clone_volume_file_entry import CloneVolumeFileEntry


T = TypeVar("T", bound="CloneVolumeFilesRequest")


@_attrs_define
class CloneVolumeFilesRequest:
    """
    Attributes:
        entries (list['CloneVolumeFileEntry']):
        mode (Union[Unset, CloneVolumeFilesRequestMode]): Clone strategy. cow_or_copy prefers copy-on-write and falls
            back to server-side copy. Default: CloneVolumeFilesRequestMode.COW_OR_COPY.
        atomic (Union[Unset, bool]): Batch atomicity flag. Only true is currently supported. Default: True.
    """

    entries: list["CloneVolumeFileEntry"]
    mode: Union[Unset, CloneVolumeFilesRequestMode] = (
        CloneVolumeFilesRequestMode.COW_OR_COPY
    )
    atomic: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        atomic = self.atomic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if atomic is not UNSET:
            field_dict["atomic"] = atomic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clone_volume_file_entry import CloneVolumeFileEntry

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = CloneVolumeFileEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, CloneVolumeFilesRequestMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CloneVolumeFilesRequestMode(_mode)

        atomic = d.pop("atomic", UNSET)

        clone_volume_files_request = cls(
            entries=entries,
            mode=mode,
            atomic=atomic,
        )

        clone_volume_files_request.additional_properties = d
        return clone_volume_files_request

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
