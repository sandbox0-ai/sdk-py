import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.function_runtime_state import FunctionRuntimeState
from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctionRuntimeStatus")


@_attrs_define
class FunctionRuntimeStatus:
    """
    Attributes:
        function_id (str):
        revision_id (str):
        revision_number (int):
        state (FunctionRuntimeState):
        runtime_sandbox_id (Union[Unset, str]): Current restored runtime sandbox, if one exists.
        runtime_context_id (Union[Unset, str]): Current runtime process context, if one exists.
        runtime_updated_at (Union[Unset, datetime.datetime]): Last time the runtime mapping was updated.
    """

    function_id: str
    revision_id: str
    revision_number: int
    state: FunctionRuntimeState
    runtime_sandbox_id: Union[Unset, str] = UNSET
    runtime_context_id: Union[Unset, str] = UNSET
    runtime_updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function_id = self.function_id

        revision_id = self.revision_id

        revision_number = self.revision_number

        state = self.state.value

        runtime_sandbox_id = self.runtime_sandbox_id

        runtime_context_id = self.runtime_context_id

        runtime_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.runtime_updated_at, Unset):
            runtime_updated_at = self.runtime_updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function_id": function_id,
                "revision_id": revision_id,
                "revision_number": revision_number,
                "state": state,
            }
        )
        if runtime_sandbox_id is not UNSET:
            field_dict["runtime_sandbox_id"] = runtime_sandbox_id
        if runtime_context_id is not UNSET:
            field_dict["runtime_context_id"] = runtime_context_id
        if runtime_updated_at is not UNSET:
            field_dict["runtime_updated_at"] = runtime_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        function_id = d.pop("function_id")

        revision_id = d.pop("revision_id")

        revision_number = d.pop("revision_number")

        state = FunctionRuntimeState(d.pop("state"))

        runtime_sandbox_id = d.pop("runtime_sandbox_id", UNSET)

        runtime_context_id = d.pop("runtime_context_id", UNSET)

        _runtime_updated_at = d.pop("runtime_updated_at", UNSET)
        runtime_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_runtime_updated_at, Unset):
            runtime_updated_at = UNSET
        else:
            runtime_updated_at = isoparse(_runtime_updated_at)

        function_runtime_status = cls(
            function_id=function_id,
            revision_id=revision_id,
            revision_number=revision_number,
            state=state,
            runtime_sandbox_id=runtime_sandbox_id,
            runtime_context_id=runtime_context_id,
            runtime_updated_at=runtime_updated_at,
        )

        function_runtime_status.additional_properties = d
        return function_runtime_status

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
