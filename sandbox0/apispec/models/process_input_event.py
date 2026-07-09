from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_event_type import ProcessEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_input_event_payload import ProcessInputEventPayload


T = TypeVar("T", bound="ProcessInputEvent")


@_attrs_define
class ProcessInputEvent:
    """
    Attributes:
        event_id (str): Idempotency key for retries.
        channel (str):
        type_ (ProcessEventType):
        payload (Union[Unset, ProcessInputEventPayload]):
    """

    event_id: str
    channel: str
    type_: ProcessEventType
    payload: Union[Unset, "ProcessInputEventPayload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        channel = self.channel

        type_ = self.type_.value

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_id": event_id,
                "channel": channel,
                "type": type_,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_input_event_payload import ProcessInputEventPayload

        d = dict(src_dict)
        event_id = d.pop("event_id")

        channel = d.pop("channel")

        type_ = ProcessEventType(d.pop("type"))

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, ProcessInputEventPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ProcessInputEventPayload.from_dict(_payload)

        process_input_event = cls(
            event_id=event_id,
            channel=channel,
            type_=type_,
            payload=payload,
        )

        process_input_event.additional_properties = d
        return process_input_event

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
