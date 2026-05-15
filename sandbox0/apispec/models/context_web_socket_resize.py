from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.context_web_socket_resize_type import ContextWebSocketResizeType

T = TypeVar("T", bound="ContextWebSocketResize")


@_attrs_define
class ContextWebSocketResize:
    """
    Attributes:
        type_ (ContextWebSocketResizeType):
        rows (int):
        cols (int):
    """

    type_: ContextWebSocketResizeType
    rows: int
    cols: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        rows = self.rows

        cols = self.cols

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "rows": rows,
                "cols": cols,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ContextWebSocketResizeType(d.pop("type"))

        rows = d.pop("rows")

        cols = d.pop("cols")

        context_web_socket_resize = cls(
            type_=type_,
            rows=rows,
            cols=cols,
        )

        context_web_socket_resize.additional_properties = d
        return context_web_socket_resize

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
