from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionTerminalSpec")


@_attrs_define
class ExecutionSessionTerminalSpec:
    """
    Attributes:
        rows (Union[Unset, int]):  Default: 24.
        cols (Union[Unset, int]):  Default: 80.
        term (Union[Unset, str]):  Default: 'xterm-256color'.
    """

    rows: Union[Unset, int] = 24
    cols: Union[Unset, int] = 80
    term: Union[Unset, str] = "xterm-256color"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rows = self.rows

        cols = self.cols

        term = self.term

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows
        if cols is not UNSET:
            field_dict["cols"] = cols
        if term is not UNSET:
            field_dict["term"] = term

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rows = d.pop("rows", UNSET)

        cols = d.pop("cols", UNSET)

        term = d.pop("term", UNSET)

        execution_session_terminal_spec = cls(
            rows=rows,
            cols=cols,
            term=term,
        )

        execution_session_terminal_spec.additional_properties = d
        return execution_session_terminal_spec

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
