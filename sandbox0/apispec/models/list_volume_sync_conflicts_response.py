from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_conflict import SyncConflict


T = TypeVar("T", bound="ListVolumeSyncConflictsResponse")


@_attrs_define
class ListVolumeSyncConflictsResponse:
    """
    Attributes:
        conflicts (list['SyncConflict']):
    """

    conflicts: list["SyncConflict"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conflicts = []
        for conflicts_item_data in self.conflicts:
            conflicts_item = conflicts_item_data.to_dict()
            conflicts.append(conflicts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conflicts": conflicts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_conflict import SyncConflict

        d = dict(src_dict)
        conflicts = []
        _conflicts = d.pop("conflicts")
        for conflicts_item_data in _conflicts:
            conflicts_item = SyncConflict.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        list_volume_sync_conflicts_response = cls(
            conflicts=conflicts,
        )

        list_volume_sync_conflicts_response.additional_properties = d
        return list_volume_sync_conflicts_response

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
