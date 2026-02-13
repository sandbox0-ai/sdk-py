from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.context_web_socket_input_type import ContextWebSocketInputType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContextWebSocketInput")


@_attrs_define
class ContextWebSocketInput:
    """
    Attributes:
        type_ (ContextWebSocketInputType):
        data (Union[Unset, str]):
        request_id (Union[Unset, str]):
    """

    type_: ContextWebSocketInputType
    data: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        data = self.data

        request_id = self.request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ContextWebSocketInputType(d.pop("type"))

        data = d.pop("data", UNSET)

        request_id = d.pop("request_id", UNSET)

        context_web_socket_input = cls(
            type_=type_,
            data=data,
            request_id=request_id,
        )

        context_web_socket_input.additional_properties = d
        return context_web_socket_input

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
