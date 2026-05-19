from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.context_web_socket_done_type import ContextWebSocketDoneType
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ContextWebSocketDone")



@_attrs_define
class ContextWebSocketDone:
    """ 
        Attributes:
            type_ (ContextWebSocketDoneType):
            request_id (Union[Unset, str]): Present for request-scoped REPL completion events.
            exit_code (Union[Unset, int]): Present when the underlying process has exited.
            state (Union[Unset, str]): Final process state when the underlying process has exited.
     """

    type_: ContextWebSocketDoneType
    request_id: Union[Unset, str] = UNSET
    exit_code: Union[Unset, int] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        request_id = self.request_id

        exit_code = self.exit_code

        state = self.state


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ContextWebSocketDoneType(d.pop("type"))




        request_id = d.pop("request_id", UNSET)

        exit_code = d.pop("exit_code", UNSET)

        state = d.pop("state", UNSET)

        context_web_socket_done = cls(
            type_=type_,
            request_id=request_id,
            exit_code=exit_code,
            state=state,
        )


        context_web_socket_done.additional_properties = d
        return context_web_socket_done

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
