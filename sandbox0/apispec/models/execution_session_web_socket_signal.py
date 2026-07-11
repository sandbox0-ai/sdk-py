from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_session_web_socket_signal_type import (
    ExecutionSessionWebSocketSignalType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionWebSocketSignal")


@_attrs_define
class ExecutionSessionWebSocketSignal:
    """
    Attributes:
        signal (str):
        type_ (ExecutionSessionWebSocketSignalType):
        expected_attempt_id (Union[Unset, str]):
        request_id (Union[Unset, str]):
    """

    signal: str
    type_: ExecutionSessionWebSocketSignalType
    expected_attempt_id: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal = self.signal

        type_ = self.type_.value

        expected_attempt_id = self.expected_attempt_id

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signal": signal,
                "type": type_,
            }
        )
        if expected_attempt_id is not UNSET:
            field_dict["expected_attempt_id"] = expected_attempt_id
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signal = d.pop("signal")

        type_ = ExecutionSessionWebSocketSignalType(d.pop("type"))

        expected_attempt_id = d.pop("expected_attempt_id", UNSET)

        request_id = d.pop("request_id", UNSET)

        execution_session_web_socket_signal = cls(
            signal=signal,
            type_=type_,
            expected_attempt_id=expected_attempt_id,
            request_id=request_id,
        )

        execution_session_web_socket_signal.additional_properties = d
        return execution_session_web_socket_signal

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
