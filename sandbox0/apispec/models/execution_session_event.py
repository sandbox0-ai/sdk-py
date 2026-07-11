import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.execution_session_event_stream import ExecutionSessionEventStream
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionEvent")


@_attrs_define
class ExecutionSessionEvent:
    """
    Attributes:
        seq (int):
        session_id (str):
        runtime_generation (int):
        type_ (str):
        occurred_at (datetime.datetime):
        attempt_id (Union[Unset, str]):
        stream (Union[Unset, ExecutionSessionEventStream]):
        data_base64 (Union[Unset, str]): Base64-encoded event bytes.
        exit_code (Union[Unset, int]):
        reason (Union[Unset, str]):
    """

    seq: int
    session_id: str
    runtime_generation: int
    type_: str
    occurred_at: datetime.datetime
    attempt_id: Union[Unset, str] = UNSET
    stream: Union[Unset, ExecutionSessionEventStream] = UNSET
    data_base64: Union[Unset, str] = UNSET
    exit_code: Union[Unset, int] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seq = self.seq

        session_id = self.session_id

        runtime_generation = self.runtime_generation

        type_ = self.type_

        occurred_at = self.occurred_at.isoformat()

        attempt_id = self.attempt_id

        stream: Union[Unset, str] = UNSET
        if not isinstance(self.stream, Unset):
            stream = self.stream.value

        data_base64 = self.data_base64

        exit_code = self.exit_code

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seq": seq,
                "session_id": session_id,
                "runtime_generation": runtime_generation,
                "type": type_,
                "occurred_at": occurred_at,
            }
        )
        if attempt_id is not UNSET:
            field_dict["attempt_id"] = attempt_id
        if stream is not UNSET:
            field_dict["stream"] = stream
        if data_base64 is not UNSET:
            field_dict["data_base64"] = data_base64
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seq = d.pop("seq")

        session_id = d.pop("session_id")

        runtime_generation = d.pop("runtime_generation")

        type_ = d.pop("type")

        occurred_at = isoparse(d.pop("occurred_at"))

        attempt_id = d.pop("attempt_id", UNSET)

        _stream = d.pop("stream", UNSET)
        stream: Union[Unset, ExecutionSessionEventStream]
        if isinstance(_stream, Unset):
            stream = UNSET
        else:
            stream = ExecutionSessionEventStream(_stream)

        data_base64 = d.pop("data_base64", UNSET)

        exit_code = d.pop("exit_code", UNSET)

        reason = d.pop("reason", UNSET)

        execution_session_event = cls(
            seq=seq,
            session_id=session_id,
            runtime_generation=runtime_generation,
            type_=type_,
            occurred_at=occurred_at,
            attempt_id=attempt_id,
            stream=stream,
            data_base64=data_base64,
            exit_code=exit_code,
            reason=reason,
        )

        execution_session_event.additional_properties = d
        return execution_session_event

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
