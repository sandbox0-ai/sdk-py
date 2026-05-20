from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.function_runtime_state import FunctionRuntimeState
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.function_runtime_instance import FunctionRuntimeInstance
  from ..models.function_autoscaling import FunctionAutoscaling





T = TypeVar("T", bound="FunctionRuntimeStatus")



@_attrs_define
class FunctionRuntimeStatus:
    """ 
        Attributes:
            function_id (str):
            revision_id (str):
            revision_number (int):
            state (FunctionRuntimeState):
            autoscaling (FunctionAutoscaling): Function runtime pool autoscaling settings. target_concurrency is a soft
                routing and scale-out signal; it is not a strong distributed per-instance concurrency semaphore.
            runtime_sandbox_id (Union[Unset, str]): Compatibility summary for one current restored runtime sandbox, if one
                exists. Use instances for the full runtime pool.
            runtime_context_id (Union[Unset, str]): Compatibility summary for one current runtime process context, if one
                exists. Use instances for the full runtime pool.
            runtime_updated_at (Union[Unset, datetime.datetime]): Last time the runtime mapping was updated.
            instances (Union[Unset, list['FunctionRuntimeInstance']]):
     """

    function_id: str
    revision_id: str
    revision_number: int
    state: FunctionRuntimeState
    autoscaling: 'FunctionAutoscaling'
    runtime_sandbox_id: Union[Unset, str] = UNSET
    runtime_context_id: Union[Unset, str] = UNSET
    runtime_updated_at: Union[Unset, datetime.datetime] = UNSET
    instances: Union[Unset, list['FunctionRuntimeInstance']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_runtime_instance import FunctionRuntimeInstance
        from ..models.function_autoscaling import FunctionAutoscaling
        function_id = self.function_id

        revision_id = self.revision_id

        revision_number = self.revision_number

        state = self.state.value

        autoscaling = self.autoscaling.to_dict()

        runtime_sandbox_id = self.runtime_sandbox_id

        runtime_context_id = self.runtime_context_id

        runtime_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.runtime_updated_at, Unset):
            runtime_updated_at = self.runtime_updated_at.isoformat()

        instances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "function_id": function_id,
            "revision_id": revision_id,
            "revision_number": revision_number,
            "state": state,
            "autoscaling": autoscaling,
        })
        if runtime_sandbox_id is not UNSET:
            field_dict["runtime_sandbox_id"] = runtime_sandbox_id
        if runtime_context_id is not UNSET:
            field_dict["runtime_context_id"] = runtime_context_id
        if runtime_updated_at is not UNSET:
            field_dict["runtime_updated_at"] = runtime_updated_at
        if instances is not UNSET:
            field_dict["instances"] = instances

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_runtime_instance import FunctionRuntimeInstance
        from ..models.function_autoscaling import FunctionAutoscaling
        d = dict(src_dict)
        function_id = d.pop("function_id")

        revision_id = d.pop("revision_id")

        revision_number = d.pop("revision_number")

        state = FunctionRuntimeState(d.pop("state"))




        autoscaling = FunctionAutoscaling.from_dict(d.pop("autoscaling"))




        runtime_sandbox_id = d.pop("runtime_sandbox_id", UNSET)

        runtime_context_id = d.pop("runtime_context_id", UNSET)

        _runtime_updated_at = d.pop("runtime_updated_at", UNSET)
        runtime_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_runtime_updated_at,  Unset):
            runtime_updated_at = UNSET
        else:
            runtime_updated_at = isoparse(_runtime_updated_at)




        instances = []
        _instances = d.pop("instances", UNSET)
        for instances_item_data in (_instances or []):
            instances_item = FunctionRuntimeInstance.from_dict(instances_item_data)



            instances.append(instances_item)


        function_runtime_status = cls(
            function_id=function_id,
            revision_id=revision_id,
            revision_number=revision_number,
            state=state,
            autoscaling=autoscaling,
            runtime_sandbox_id=runtime_sandbox_id,
            runtime_context_id=runtime_context_id,
            runtime_updated_at=runtime_updated_at,
            instances=instances,
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
