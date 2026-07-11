from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionSignalRequest")


@_attrs_define
class ExecutionSessionSignalRequest:
    """
    Attributes:
        signal (str):
        expected_attempt_id (Union[Unset, str]):
    """

    signal: str
    expected_attempt_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal = self.signal

        expected_attempt_id = self.expected_attempt_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signal": signal,
            }
        )
        if expected_attempt_id is not UNSET:
            field_dict["expected_attempt_id"] = expected_attempt_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signal = d.pop("signal")

        expected_attempt_id = d.pop("expected_attempt_id", UNSET)

        execution_session_signal_request = cls(
            signal=signal,
            expected_attempt_id=expected_attempt_id,
        )

        execution_session_signal_request.additional_properties = d
        return execution_session_signal_request

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
