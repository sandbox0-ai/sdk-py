from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.context_web_socket_output_source import ContextWebSocketOutputSource
from ..models.context_web_socket_output_type import ContextWebSocketOutputType

T = TypeVar("T", bound="ContextWebSocketOutput")


@_attrs_define
class ContextWebSocketOutput:
    """
    Attributes:
        type_ (ContextWebSocketOutputType):
        source (ContextWebSocketOutputSource):
        data (str):
    """

    type_: ContextWebSocketOutputType
    source: ContextWebSocketOutputSource
    data: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        source = self.source.value

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "source": source,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ContextWebSocketOutputType(d.pop("type"))

        source = ContextWebSocketOutputSource(d.pop("source"))

        data = d.pop("data")

        context_web_socket_output = cls(
            type_=type_,
            source=source,
            data=data,
        )

        context_web_socket_output.additional_properties = d
        return context_web_socket_output

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
