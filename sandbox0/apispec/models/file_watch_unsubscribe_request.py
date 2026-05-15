from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_watch_unsubscribe_request_action import (
    FileWatchUnsubscribeRequestAction,
)

T = TypeVar("T", bound="FileWatchUnsubscribeRequest")


@_attrs_define
class FileWatchUnsubscribeRequest:
    """
    Attributes:
        action (FileWatchUnsubscribeRequestAction):
        watch_id (str):
    """

    action: FileWatchUnsubscribeRequestAction
    watch_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        watch_id = self.watch_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "watch_id": watch_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = FileWatchUnsubscribeRequestAction(d.pop("action"))

        watch_id = d.pop("watch_id")

        file_watch_unsubscribe_request = cls(
            action=action,
            watch_id=watch_id,
        )

        file_watch_unsubscribe_request.additional_properties = d
        return file_watch_unsubscribe_request

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
