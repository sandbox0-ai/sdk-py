from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_session_web_socket_input_type import (
    ExecutionSessionWebSocketInputType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionWebSocketInput")


@_attrs_define
class ExecutionSessionWebSocketInput:
    """
    Attributes:
        input_id (str): Client-generated operation identifier used to deduplicate recorded retries.
        type_ (ExecutionSessionWebSocketInputType):
        expected_attempt_id (Union[Unset, str]):
        data_base64 (Union[Unset, str]): Base64-encoded input bytes accepted into the current attempt input queue.
            WebSocket closure never implies EOF.
        eof (Union[Unset, bool]):  Default: False.
        request_id (Union[Unset, str]):
    """

    input_id: str
    type_: ExecutionSessionWebSocketInputType
    expected_attempt_id: Union[Unset, str] = UNSET
    data_base64: Union[Unset, str] = UNSET
    eof: Union[Unset, bool] = False
    request_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_id = self.input_id

        type_ = self.type_.value

        expected_attempt_id = self.expected_attempt_id

        data_base64 = self.data_base64

        eof = self.eof

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_id": input_id,
                "type": type_,
            }
        )
        if expected_attempt_id is not UNSET:
            field_dict["expected_attempt_id"] = expected_attempt_id
        if data_base64 is not UNSET:
            field_dict["data_base64"] = data_base64
        if eof is not UNSET:
            field_dict["eof"] = eof
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_id = d.pop("input_id")

        type_ = ExecutionSessionWebSocketInputType(d.pop("type"))

        expected_attempt_id = d.pop("expected_attempt_id", UNSET)

        data_base64 = d.pop("data_base64", UNSET)

        eof = d.pop("eof", UNSET)

        request_id = d.pop("request_id", UNSET)

        execution_session_web_socket_input = cls(
            input_id=input_id,
            type_=type_,
            expected_attempt_id=expected_attempt_id,
            data_base64=data_base64,
            eof=eof,
            request_id=request_id,
        )

        execution_session_web_socket_input.additional_properties = d
        return execution_session_web_socket_input

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
