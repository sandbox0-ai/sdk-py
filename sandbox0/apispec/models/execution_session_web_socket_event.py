from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_session_web_socket_event_type import (
    ExecutionSessionWebSocketEventType,
)

if TYPE_CHECKING:
    from ..models.execution_session_event import ExecutionSessionEvent


T = TypeVar("T", bound="ExecutionSessionWebSocketEvent")


@_attrs_define
class ExecutionSessionWebSocketEvent:
    """
    Attributes:
        type_ (ExecutionSessionWebSocketEventType):
        event (ExecutionSessionEvent):
    """

    type_: ExecutionSessionWebSocketEventType
    event: "ExecutionSessionEvent"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        event = self.event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "event": event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_session_event import ExecutionSessionEvent

        d = dict(src_dict)
        type_ = ExecutionSessionWebSocketEventType(d.pop("type"))

        event = ExecutionSessionEvent.from_dict(d.pop("event"))

        execution_session_web_socket_event = cls(
            type_=type_,
            event=event,
        )

        execution_session_web_socket_event.additional_properties = d
        return execution_session_web_socket_event

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
