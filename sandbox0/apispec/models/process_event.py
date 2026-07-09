import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.process_event_type import ProcessEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_event_payload import ProcessEventPayload


T = TypeVar("T", bound="ProcessEvent")


@_attrs_define
class ProcessEvent:
    """
    Attributes:
        seq (int):
        process_id (str):
        type_ (ProcessEventType):
        timestamp (datetime.datetime):
        event_id (Union[Unset, str]):
        channel (Union[Unset, str]):
        payload (Union[Unset, ProcessEventPayload]):
    """

    seq: int
    process_id: str
    type_: ProcessEventType
    timestamp: datetime.datetime
    event_id: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    payload: Union[Unset, "ProcessEventPayload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        process_id = self.process_id

        type_ = self.type_.value

        timestamp = self.timestamp.isoformat()

        event_id = self.event_id

        channel = self.channel

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seq": seq,
                "process_id": process_id,
                "type": type_,
                "timestamp": timestamp,
            }
        )
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_event_payload import ProcessEventPayload

        d = dict(src_dict)
        seq = d.pop("seq")

        process_id = d.pop("process_id")

        type_ = ProcessEventType(d.pop("type"))

        timestamp = isoparse(d.pop("timestamp"))

        event_id = d.pop("event_id", UNSET)

        channel = d.pop("channel", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, ProcessEventPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ProcessEventPayload.from_dict(_payload)

        process_event = cls(
            seq=seq,
            process_id=process_id,
            type_=type_,
            timestamp=timestamp,
            event_id=event_id,
            channel=channel,
            payload=payload,
        )

        process_event.additional_properties = d
        return process_event

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
