from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_session_web_socket_error_type import (
    ExecutionSessionWebSocketErrorType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionWebSocketError")


@_attrs_define
class ExecutionSessionWebSocketError:
    """
    Attributes:
        type_ (ExecutionSessionWebSocketErrorType):
        error (str):
        request_id (Union[Unset, str]):
    """

    type_: ExecutionSessionWebSocketErrorType
    error: str
    request_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        error = self.error

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "error": error,
            }
        )
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ExecutionSessionWebSocketErrorType(d.pop("type"))

        error = d.pop("error")

        request_id = d.pop("request_id", UNSET)

        execution_session_web_socket_error = cls(
            type_=type_,
            error=error,
            request_id=request_id,
        )

        execution_session_web_socket_error.additional_properties = d
        return execution_session_web_socket_error

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
