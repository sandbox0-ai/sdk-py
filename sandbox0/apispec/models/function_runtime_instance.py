from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.function_runtime_instance_state import FunctionRuntimeInstanceState
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="FunctionRuntimeInstance")



@_attrs_define
class FunctionRuntimeInstance:
    """ 
        Attributes:
            id (str):
            team_id (str):
            function_id (str):
            revision_id (str):
            sandbox_id (str):
            state (FunctionRuntimeInstanceState):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            context_id (Union[Unset, str]):
            last_error (Union[Unset, str]):
            ready_at (Union[Unset, datetime.datetime]):
            last_used_at (Union[Unset, datetime.datetime]):
            draining_at (Union[Unset, datetime.datetime]):
            failed_at (Union[Unset, datetime.datetime]):
     """

    id: str
    team_id: str
    function_id: str
    revision_id: str
    sandbox_id: str
    state: FunctionRuntimeInstanceState
    created_at: datetime.datetime
    updated_at: datetime.datetime
    context_id: Union[Unset, str] = UNSET
    last_error: Union[Unset, str] = UNSET
    ready_at: Union[Unset, datetime.datetime] = UNSET
    last_used_at: Union[Unset, datetime.datetime] = UNSET
    draining_at: Union[Unset, datetime.datetime] = UNSET
    failed_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        function_id = self.function_id

        revision_id = self.revision_id

        sandbox_id = self.sandbox_id

        state = self.state.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        context_id = self.context_id

        last_error = self.last_error

        ready_at: Union[Unset, str] = UNSET
        if not isinstance(self.ready_at, Unset):
            ready_at = self.ready_at.isoformat()

        last_used_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        draining_at: Union[Unset, str] = UNSET
        if not isinstance(self.draining_at, Unset):
            draining_at = self.draining_at.isoformat()

        failed_at: Union[Unset, str] = UNSET
        if not isinstance(self.failed_at, Unset):
            failed_at = self.failed_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "team_id": team_id,
            "function_id": function_id,
            "revision_id": revision_id,
            "sandbox_id": sandbox_id,
            "state": state,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if context_id is not UNSET:
            field_dict["context_id"] = context_id
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if ready_at is not UNSET:
            field_dict["ready_at"] = ready_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if draining_at is not UNSET:
            field_dict["draining_at"] = draining_at
        if failed_at is not UNSET:
            field_dict["failed_at"] = failed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        function_id = d.pop("function_id")

        revision_id = d.pop("revision_id")

        sandbox_id = d.pop("sandbox_id")

        state = FunctionRuntimeInstanceState(d.pop("state"))




        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        context_id = d.pop("context_id", UNSET)

        last_error = d.pop("last_error", UNSET)

        _ready_at = d.pop("ready_at", UNSET)
        ready_at: Union[Unset, datetime.datetime]
        if isinstance(_ready_at,  Unset):
            ready_at = UNSET
        else:
            ready_at = isoparse(_ready_at)




        _last_used_at = d.pop("last_used_at", UNSET)
        last_used_at: Union[Unset, datetime.datetime]
        if isinstance(_last_used_at,  Unset):
            last_used_at = UNSET
        else:
            last_used_at = isoparse(_last_used_at)




        _draining_at = d.pop("draining_at", UNSET)
        draining_at: Union[Unset, datetime.datetime]
        if isinstance(_draining_at,  Unset):
            draining_at = UNSET
        else:
            draining_at = isoparse(_draining_at)




        _failed_at = d.pop("failed_at", UNSET)
        failed_at: Union[Unset, datetime.datetime]
        if isinstance(_failed_at,  Unset):
            failed_at = UNSET
        else:
            failed_at = isoparse(_failed_at)




        function_runtime_instance = cls(
            id=id,
            team_id=team_id,
            function_id=function_id,
            revision_id=revision_id,
            sandbox_id=sandbox_id,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            context_id=context_id,
            last_error=last_error,
            ready_at=ready_at,
            last_used_at=last_used_at,
            draining_at=draining_at,
            failed_at=failed_at,
        )


        function_runtime_instance.additional_properties = d
        return function_runtime_instance

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
