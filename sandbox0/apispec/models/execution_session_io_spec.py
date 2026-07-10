from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_session_io_mode import ExecutionSessionIOMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_session_terminal_spec import ExecutionSessionTerminalSpec


T = TypeVar("T", bound="ExecutionSessionIOSpec")


@_attrs_define
class ExecutionSessionIOSpec:
    """
    Attributes:
        mode (Union[Unset, ExecutionSessionIOMode]):
        terminal (Union[Unset, ExecutionSessionTerminalSpec]):
    """

    mode: Union[Unset, ExecutionSessionIOMode] = UNSET
    terminal: Union[Unset, "ExecutionSessionTerminalSpec"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        terminal: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.terminal, Unset):
            terminal = self.terminal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if terminal is not UNSET:
            field_dict["terminal"] = terminal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_session_terminal_spec import (
            ExecutionSessionTerminalSpec,
        )

        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, ExecutionSessionIOMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ExecutionSessionIOMode(_mode)

        _terminal = d.pop("terminal", UNSET)
        terminal: Union[Unset, ExecutionSessionTerminalSpec]
        if isinstance(_terminal, Unset):
            terminal = UNSET
        else:
            terminal = ExecutionSessionTerminalSpec.from_dict(_terminal)

        execution_session_io_spec = cls(
            mode=mode,
            terminal=terminal,
        )

        execution_session_io_spec.additional_properties = d
        return execution_session_io_spec

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
