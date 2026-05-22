from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.context_web_socket_signal_type import ContextWebSocketSignalType

T = TypeVar("T", bound="ContextWebSocketSignal")


@_attrs_define
class ContextWebSocketSignal:
    """
    Attributes:
        type_ (ContextWebSocketSignalType):
        signal (str):
    """

    type_: ContextWebSocketSignalType
    signal: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        signal = self.signal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "signal": signal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ContextWebSocketSignalType(d.pop("type"))

        signal = d.pop("signal")

        context_web_socket_signal = cls(
            type_=type_,
            signal=signal,
        )

        context_web_socket_signal.additional_properties = d
        return context_web_socket_signal

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
