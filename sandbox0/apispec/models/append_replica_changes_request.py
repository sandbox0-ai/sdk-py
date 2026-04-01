from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.change_request import ChangeRequest


T = TypeVar("T", bound="AppendReplicaChangesRequest")


@_attrs_define
class AppendReplicaChangesRequest:
    """
    Attributes:
        request_id (str):
        base_seq (int):
        changes (list['ChangeRequest']):
    """

    request_id: str
    base_seq: int
    changes: list["ChangeRequest"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        base_seq = self.base_seq

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request_id": request_id,
                "base_seq": base_seq,
                "changes": changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_request import ChangeRequest

        d = dict(src_dict)
        request_id = d.pop("request_id")

        base_seq = d.pop("base_seq")

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = ChangeRequest.from_dict(changes_item_data)

            changes.append(changes_item)

        append_replica_changes_request = cls(
            request_id=request_id,
            base_seq=base_seq,
            changes=changes,
        )

        append_replica_changes_request.additional_properties = d
        return append_replica_changes_request

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
