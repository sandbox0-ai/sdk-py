from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProcessEventLogSnapshot")


@_attrs_define
class ProcessEventLogSnapshot:
    """
    Attributes:
        next_seq (int):
        oldest_seq (int):
        capacity (int):
    """

    next_seq: int
    oldest_seq: int
    capacity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_seq = self.next_seq

        oldest_seq = self.oldest_seq

        capacity = self.capacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next_seq": next_seq,
                "oldest_seq": oldest_seq,
                "capacity": capacity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_seq = d.pop("next_seq")

        oldest_seq = d.pop("oldest_seq")

        capacity = d.pop("capacity")

        process_event_log_snapshot = cls(
            next_seq=next_seq,
            oldest_seq=oldest_seq,
            capacity=capacity,
        )

        process_event_log_snapshot.additional_properties = d
        return process_event_log_snapshot

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
