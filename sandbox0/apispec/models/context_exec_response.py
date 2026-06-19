from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ContextExecResponse")



@_attrs_define
class ContextExecResponse:
    r""" 
        Attributes:
            output_raw (str): Raw PTY output, may contain terminal control characters (e.g. \r)
            exit_code (Union[Unset, int]): Present when the underlying process has exited.
            state (Union[Unset, str]): Final process state when the underlying process has exited.
     """

    output_raw: str
    exit_code: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        output_raw = self.output_raw

        exit_code = self.exit_code

        state = self.state


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "output_raw": output_raw,
        })
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        output_raw = d.pop("output_raw")

        exit_code = d.pop("exit_code", UNSET)

        state = d.pop("state", UNSET)

        context_exec_response = cls(
            output_raw=output_raw,
            exit_code=exit_code,
            state=state,
        )


        context_exec_response.additional_properties = d
        return context_exec_response

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
