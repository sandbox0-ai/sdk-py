from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_watch_event_type import FileWatchEventType

T = TypeVar("T", bound="FileWatchEvent")


@_attrs_define
class FileWatchEvent:
    """
    Attributes:
        type_ (FileWatchEventType):
        watch_id (str):
        event (str):
        path (str):
    """

    type_: FileWatchEventType
    watch_id: str
    event: str
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        watch_id = self.watch_id

        event = self.event

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "watch_id": watch_id,
                "event": event,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FileWatchEventType(d.pop("type"))

        watch_id = d.pop("watch_id")

        event = d.pop("event")

        path = d.pop("path")

        file_watch_event = cls(
            type_=type_,
            watch_id=watch_id,
            event=event,
            path=path,
        )

        file_watch_event.additional_properties = d
        return file_watch_event

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
