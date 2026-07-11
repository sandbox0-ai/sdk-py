from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionInputRequest")


@_attrs_define
class ExecutionSessionInputRequest:
    """
    Attributes:
        input_id (str): Client-generated operation identifier used to deduplicate recorded retries.
        expected_attempt_id (Union[Unset, str]):
        data_base64 (Union[Unset, str]): Base64-encoded input bytes accepted into the current attempt input queue.
            WebSocket closure never implies EOF.
        eof (Union[Unset, bool]):  Default: False.
    """

    input_id: str
    expected_attempt_id: Union[Unset, str] = UNSET
    data_base64: Union[Unset, str] = UNSET
    eof: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_id = self.input_id

        expected_attempt_id = self.expected_attempt_id

        data_base64 = self.data_base64

        eof = self.eof

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_id": input_id,
            }
        )
        if expected_attempt_id is not UNSET:
            field_dict["expected_attempt_id"] = expected_attempt_id
        if data_base64 is not UNSET:
            field_dict["data_base64"] = data_base64
        if eof is not UNSET:
            field_dict["eof"] = eof

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_id = d.pop("input_id")

        expected_attempt_id = d.pop("expected_attempt_id", UNSET)

        data_base64 = d.pop("data_base64", UNSET)

        eof = d.pop("eof", UNSET)

        execution_session_input_request = cls(
            input_id=input_id,
            expected_attempt_id=expected_attempt_id,
            data_base64=data_base64,
            eof=eof,
        )

        execution_session_input_request.additional_properties = d
        return execution_session_input_request

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
