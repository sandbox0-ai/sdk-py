from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_journal_entry import SyncJournalEntry


T = TypeVar("T", bound="ListVolumeSyncChangesResponse")


@_attrs_define
class ListVolumeSyncChangesResponse:
    """
    Attributes:
        head_seq (int):
        retained_after_seq (int):
        changes (list['SyncJournalEntry']):
    """

    head_seq: int
    retained_after_seq: int
    changes: list["SyncJournalEntry"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        head_seq = self.head_seq

        retained_after_seq = self.retained_after_seq

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "head_seq": head_seq,
                "retained_after_seq": retained_after_seq,
                "changes": changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_journal_entry import SyncJournalEntry

        d = dict(src_dict)
        head_seq = d.pop("head_seq")

        retained_after_seq = d.pop("retained_after_seq")

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = SyncJournalEntry.from_dict(changes_item_data)

            changes.append(changes_item)

        list_volume_sync_changes_response = cls(
            head_seq=head_seq,
            retained_after_seq=retained_after_seq,
            changes=changes,
        )

        list_volume_sync_changes_response.additional_properties = d
        return list_volume_sync_changes_response

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
