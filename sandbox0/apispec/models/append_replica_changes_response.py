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
    from ..models.sync_journal_entry import SyncJournalEntry


T = TypeVar("T", bound="AppendReplicaChangesResponse")


@_attrs_define
class AppendReplicaChangesResponse:
    """
    Attributes:
        head_seq (int):
        accepted (list['SyncJournalEntry']):
        conflicts (list['SyncConflict']):
    """

    head_seq: int
    accepted: list["SyncJournalEntry"]
    conflicts: list["SyncConflict"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        head_seq = self.head_seq

        accepted = []
        for accepted_item_data in self.accepted:
            accepted_item = accepted_item_data.to_dict()
            accepted.append(accepted_item)

        conflicts = []
        for conflicts_item_data in self.conflicts:
            conflicts_item = conflicts_item_data.to_dict()
            conflicts.append(conflicts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "head_seq": head_seq,
                "accepted": accepted,
                "conflicts": conflicts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_conflict import SyncConflict
        from ..models.sync_journal_entry import SyncJournalEntry

        d = dict(src_dict)
        head_seq = d.pop("head_seq")

        accepted = []
        _accepted = d.pop("accepted")
        for accepted_item_data in _accepted:
            accepted_item = SyncJournalEntry.from_dict(accepted_item_data)

            accepted.append(accepted_item)

        conflicts = []
        _conflicts = d.pop("conflicts")
        for conflicts_item_data in _conflicts:
            conflicts_item = SyncConflict.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        append_replica_changes_response = cls(
            head_seq=head_seq,
            accepted=accepted,
            conflicts=conflicts,
        )

        append_replica_changes_response.additional_properties = d
        return append_replica_changes_response

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
