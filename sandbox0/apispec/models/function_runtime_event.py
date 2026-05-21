from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.function_runtime_phase import FunctionRuntimePhase
from ..models.function_runtime_readiness_state import FunctionRuntimeReadinessState
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="FunctionRuntimeEvent")



@_attrs_define
class FunctionRuntimeEvent:
    """ 
        Attributes:
            id (str):
            team_id (str):
            function_id (str):
            revision_id (str):
            phase (FunctionRuntimePhase):
            readiness_state (FunctionRuntimeReadinessState):
            created_at (datetime.datetime):
            runtime_instance_id (Union[Unset, str]):
            runtime_sandbox_id (Union[Unset, str]):
            runtime_context_id (Union[Unset, str]):
            reason (Union[Unset, str]):
            message (Union[Unset, str]):
            startup_duration_ms (Union[Unset, int]):
     """

    id: str
    team_id: str
    function_id: str
    revision_id: str
    phase: FunctionRuntimePhase
    readiness_state: FunctionRuntimeReadinessState
    created_at: datetime.datetime
    runtime_instance_id: Union[Unset, str] = UNSET
    runtime_sandbox_id: Union[Unset, str] = UNSET
    runtime_context_id: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    startup_duration_ms: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        function_id = self.function_id

        revision_id = self.revision_id

        phase = self.phase.value

        readiness_state = self.readiness_state.value

        created_at = self.created_at.isoformat()

        runtime_instance_id = self.runtime_instance_id

        runtime_sandbox_id = self.runtime_sandbox_id

        runtime_context_id = self.runtime_context_id

        reason = self.reason

        message = self.message

        startup_duration_ms = self.startup_duration_ms


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "team_id": team_id,
            "function_id": function_id,
            "revision_id": revision_id,
            "phase": phase,
            "readiness_state": readiness_state,
            "created_at": created_at,
        })
        if runtime_instance_id is not UNSET:
            field_dict["runtime_instance_id"] = runtime_instance_id
        if runtime_sandbox_id is not UNSET:
            field_dict["runtime_sandbox_id"] = runtime_sandbox_id
        if runtime_context_id is not UNSET:
            field_dict["runtime_context_id"] = runtime_context_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message
        if startup_duration_ms is not UNSET:
            field_dict["startup_duration_ms"] = startup_duration_ms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        function_id = d.pop("function_id")

        revision_id = d.pop("revision_id")

        phase = FunctionRuntimePhase(d.pop("phase"))




        readiness_state = FunctionRuntimeReadinessState(d.pop("readiness_state"))




        created_at = isoparse(d.pop("created_at"))




        runtime_instance_id = d.pop("runtime_instance_id", UNSET)

        runtime_sandbox_id = d.pop("runtime_sandbox_id", UNSET)

        runtime_context_id = d.pop("runtime_context_id", UNSET)

        reason = d.pop("reason", UNSET)

        message = d.pop("message", UNSET)

        startup_duration_ms = d.pop("startup_duration_ms", UNSET)

        function_runtime_event = cls(
            id=id,
            team_id=team_id,
            function_id=function_id,
            revision_id=revision_id,
            phase=phase,
            readiness_state=readiness_state,
            created_at=created_at,
            runtime_instance_id=runtime_instance_id,
            runtime_sandbox_id=runtime_sandbox_id,
            runtime_context_id=runtime_context_id,
            reason=reason,
            message=message,
            startup_duration_ms=startup_duration_ms,
        )


        function_runtime_event.additional_properties = d
        return function_runtime_event

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
