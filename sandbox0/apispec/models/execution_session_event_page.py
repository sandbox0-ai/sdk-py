from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execution_session_event import ExecutionSessionEvent
    from ..models.execution_session_event_cursor import ExecutionSessionEventCursor


T = TypeVar("T", bound="ExecutionSessionEventPage")


@_attrs_define
class ExecutionSessionEventPage:
    """
    Attributes:
        events (list['ExecutionSessionEvent']):
        cursor (ExecutionSessionEventCursor):
    """

    events: list["ExecutionSessionEvent"]
    cursor: "ExecutionSessionEventCursor"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        cursor = self.cursor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "cursor": cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_session_event import ExecutionSessionEvent
        from ..models.execution_session_event_cursor import ExecutionSessionEventCursor

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = ExecutionSessionEvent.from_dict(events_item_data)

            events.append(events_item)

        cursor = ExecutionSessionEventCursor.from_dict(d.pop("cursor"))

        execution_session_event_page = cls(
            events=events,
            cursor=cursor,
        )

        execution_session_event_page.additional_properties = d
        return execution_session_event_page

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
