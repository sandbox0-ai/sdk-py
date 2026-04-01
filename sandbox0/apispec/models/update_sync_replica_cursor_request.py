from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateSyncReplicaCursorRequest")


@_attrs_define
class UpdateSyncReplicaCursorRequest:
    """
    Attributes:
        last_applied_seq (int):
    """

    last_applied_seq: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_applied_seq = self.last_applied_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_applied_seq": last_applied_seq,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_applied_seq = d.pop("last_applied_seq")

        update_sync_replica_cursor_request = cls(
            last_applied_seq=last_applied_seq,
        )

        update_sync_replica_cursor_request.additional_properties = d
        return update_sync_replica_cursor_request

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
