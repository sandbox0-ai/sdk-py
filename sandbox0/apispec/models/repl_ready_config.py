from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repl_ready_mode import REPLReadyMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="REPLReadyConfig")


@_attrs_define
class REPLReadyConfig:
    """
    Attributes:
        mode (Union[Unset, REPLReadyMode]):
        token (Union[Unset, str]):
        startup_delay_ms (Union[Unset, int]):
    """

    mode: Union[Unset, REPLReadyMode] = UNSET
    token: Union[Unset, str] = UNSET
    startup_delay_ms: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        token = self.token

        startup_delay_ms = self.startup_delay_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if token is not UNSET:
            field_dict["token"] = token
        if startup_delay_ms is not UNSET:
            field_dict["startup_delay_ms"] = startup_delay_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, REPLReadyMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = REPLReadyMode(_mode)

        token = d.pop("token", UNSET)

        startup_delay_ms = d.pop("startup_delay_ms", UNSET)

        repl_ready_config = cls(
            mode=mode,
            token=token,
            startup_delay_ms=startup_delay_ms,
        )

        repl_ready_config.additional_properties = d
        return repl_ready_config

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
