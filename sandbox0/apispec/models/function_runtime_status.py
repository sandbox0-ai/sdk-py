from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.function_runtime_phase import FunctionRuntimePhase
from ..models.function_runtime_readiness_state import FunctionRuntimeReadinessState
from ..models.function_runtime_state import FunctionRuntimeState
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.function_runtime_instance import FunctionRuntimeInstance
  from ..models.function_autoscaling import FunctionAutoscaling
  from ..models.function_runtime_event import FunctionRuntimeEvent





T = TypeVar("T", bound="FunctionRuntimeStatus")



@_attrs_define
class FunctionRuntimeStatus:
    """ 
        Attributes:
            function_id (str):
            revision_id (str):
            revision_number (int):
            state (FunctionRuntimeState):
            phase (FunctionRuntimePhase):
            autoscaling (FunctionAutoscaling): Function runtime pool autoscaling settings. target_concurrency is a soft
                routing and scale-out signal; it is not a strong distributed per-instance concurrency semaphore.
            readiness_state (FunctionRuntimeReadinessState):
            runtime_sandbox_id (Union[Unset, str]): Compatibility summary for one current restored runtime sandbox, if one
                exists. Use instances for the full runtime pool.
            runtime_context_id (Union[Unset, str]): Compatibility summary for one current runtime process context, if one
                exists. Use instances for the full runtime pool.
            runtime_updated_at (Union[Unset, datetime.datetime]): Last time the runtime mapping was updated.
            startup_duration_ms (Union[Unset, int]):
            last_error (Union[Unset, str]):
            last_error_at (Union[Unset, datetime.datetime]):
            instances (Union[Unset, list['FunctionRuntimeInstance']]):
            recent_events (Union[Unset, list['FunctionRuntimeEvent']]):
     """

    function_id: str
    revision_id: str
    revision_number: int
    state: FunctionRuntimeState
    phase: FunctionRuntimePhase
    autoscaling: 'FunctionAutoscaling'
    readiness_state: FunctionRuntimeReadinessState
    runtime_sandbox_id: Union[Unset, str] = UNSET
    runtime_context_id: Union[Unset, str] = UNSET
    runtime_updated_at: Union[Unset, datetime.datetime] = UNSET
    startup_duration_ms: Union[Unset, int] = UNSET
    last_error: Union[Unset, str] = UNSET
    last_error_at: Union[Unset, datetime.datetime] = UNSET
    instances: Union[Unset, list['FunctionRuntimeInstance']] = UNSET
    recent_events: Union[Unset, list['FunctionRuntimeEvent']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_runtime_instance import FunctionRuntimeInstance
        from ..models.function_autoscaling import FunctionAutoscaling
        from ..models.function_runtime_event import FunctionRuntimeEvent
        function_id = self.function_id

        revision_id = self.revision_id

        revision_number = self.revision_number

        state = self.state.value

        phase = self.phase.value

        autoscaling = self.autoscaling.to_dict()

        readiness_state = self.readiness_state.value

        runtime_sandbox_id = self.runtime_sandbox_id

        runtime_context_id = self.runtime_context_id

        runtime_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.runtime_updated_at, Unset):
            runtime_updated_at = self.runtime_updated_at.isoformat()

        startup_duration_ms = self.startup_duration_ms

        last_error = self.last_error

        last_error_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_error_at, Unset):
            last_error_at = self.last_error_at.isoformat()

        instances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)



        recent_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.recent_events, Unset):
            recent_events = []
            for recent_events_item_data in self.recent_events:
                recent_events_item = recent_events_item_data.to_dict()
                recent_events.append(recent_events_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "function_id": function_id,
            "revision_id": revision_id,
            "revision_number": revision_number,
            "state": state,
            "phase": phase,
            "autoscaling": autoscaling,
            "readiness_state": readiness_state,
        })
        if runtime_sandbox_id is not UNSET:
            field_dict["runtime_sandbox_id"] = runtime_sandbox_id
        if runtime_context_id is not UNSET:
            field_dict["runtime_context_id"] = runtime_context_id
        if runtime_updated_at is not UNSET:
            field_dict["runtime_updated_at"] = runtime_updated_at
        if startup_duration_ms is not UNSET:
            field_dict["startup_duration_ms"] = startup_duration_ms
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if last_error_at is not UNSET:
            field_dict["last_error_at"] = last_error_at
        if instances is not UNSET:
            field_dict["instances"] = instances
        if recent_events is not UNSET:
            field_dict["recent_events"] = recent_events

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_runtime_instance import FunctionRuntimeInstance
        from ..models.function_autoscaling import FunctionAutoscaling
        from ..models.function_runtime_event import FunctionRuntimeEvent
        d = dict(src_dict)
        function_id = d.pop("function_id")

        revision_id = d.pop("revision_id")

        revision_number = d.pop("revision_number")

        state = FunctionRuntimeState(d.pop("state"))




        phase = FunctionRuntimePhase(d.pop("phase"))




        autoscaling = FunctionAutoscaling.from_dict(d.pop("autoscaling"))




        readiness_state = FunctionRuntimeReadinessState(d.pop("readiness_state"))




        runtime_sandbox_id = d.pop("runtime_sandbox_id", UNSET)

        runtime_context_id = d.pop("runtime_context_id", UNSET)

        _runtime_updated_at = d.pop("runtime_updated_at", UNSET)
        runtime_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_runtime_updated_at,  Unset):
            runtime_updated_at = UNSET
        else:
            runtime_updated_at = isoparse(_runtime_updated_at)




        startup_duration_ms = d.pop("startup_duration_ms", UNSET)

        last_error = d.pop("last_error", UNSET)

        _last_error_at = d.pop("last_error_at", UNSET)
        last_error_at: Union[Unset, datetime.datetime]
        if isinstance(_last_error_at,  Unset):
            last_error_at = UNSET
        else:
            last_error_at = isoparse(_last_error_at)




        instances = []
        _instances = d.pop("instances", UNSET)
        for instances_item_data in (_instances or []):
            instances_item = FunctionRuntimeInstance.from_dict(instances_item_data)



            instances.append(instances_item)


        recent_events = []
        _recent_events = d.pop("recent_events", UNSET)
        for recent_events_item_data in (_recent_events or []):
            recent_events_item = FunctionRuntimeEvent.from_dict(recent_events_item_data)



            recent_events.append(recent_events_item)


        function_runtime_status = cls(
            function_id=function_id,
            revision_id=revision_id,
            revision_number=revision_number,
            state=state,
            phase=phase,
            autoscaling=autoscaling,
            readiness_state=readiness_state,
            runtime_sandbox_id=runtime_sandbox_id,
            runtime_context_id=runtime_context_id,
            runtime_updated_at=runtime_updated_at,
            startup_duration_ms=startup_duration_ms,
            last_error=last_error,
            last_error_at=last_error_at,
            instances=instances,
            recent_events=recent_events,
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
