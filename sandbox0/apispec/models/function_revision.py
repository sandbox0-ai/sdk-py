from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.function_revision_status import FunctionRevisionStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.function_source import FunctionSource
  from ..models.function_revision_spec import FunctionRevisionSpec





T = TypeVar("T", bound="FunctionRevision")



@_attrs_define
class FunctionRevision:
    """ 
        Attributes:
            id (str):
            function_id (str):
            team_id (str):
            number (int):
            source (FunctionSource):
            spec (FunctionRevisionSpec): Canonical runtime contract compiled from every function deploy mode.
            status (FunctionRevisionStatus):
            created_at (datetime.datetime):
            runtime_sandbox_id (Union[Unset, str]):
            runtime_cluster_id (Union[Unset, str]):
            runtime_context_id (Union[Unset, str]):
            activated_at (Union[Unset, datetime.datetime]):
     """

    id: str
    function_id: str
    team_id: str
    number: int
    source: 'FunctionSource'
    spec: 'FunctionRevisionSpec'
    status: FunctionRevisionStatus
    created_at: datetime.datetime
    runtime_sandbox_id: Union[Unset, str] = UNSET
    runtime_cluster_id: Union[Unset, str] = UNSET
    runtime_context_id: Union[Unset, str] = UNSET
    activated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_source import FunctionSource
        from ..models.function_revision_spec import FunctionRevisionSpec
        id = self.id

        function_id = self.function_id

        team_id = self.team_id

        number = self.number

        source = self.source.to_dict()

        spec = self.spec.to_dict()

        status = self.status.value

        created_at = self.created_at.isoformat()

        runtime_sandbox_id = self.runtime_sandbox_id

        runtime_cluster_id = self.runtime_cluster_id

        runtime_context_id = self.runtime_context_id

        activated_at: Union[Unset, str] = UNSET
        if not isinstance(self.activated_at, Unset):
            activated_at = self.activated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "function_id": function_id,
            "team_id": team_id,
            "number": number,
            "source": source,
            "spec": spec,
            "status": status,
            "created_at": created_at,
        })
        if runtime_sandbox_id is not UNSET:
            field_dict["runtime_sandbox_id"] = runtime_sandbox_id
        if runtime_cluster_id is not UNSET:
            field_dict["runtime_cluster_id"] = runtime_cluster_id
        if runtime_context_id is not UNSET:
            field_dict["runtime_context_id"] = runtime_context_id
        if activated_at is not UNSET:
            field_dict["activated_at"] = activated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_source import FunctionSource
        from ..models.function_revision_spec import FunctionRevisionSpec
        d = dict(src_dict)
        id = d.pop("id")

        function_id = d.pop("function_id")

        team_id = d.pop("team_id")

        number = d.pop("number")

        source = FunctionSource.from_dict(d.pop("source"))




        spec = FunctionRevisionSpec.from_dict(d.pop("spec"))




        status = FunctionRevisionStatus(d.pop("status"))




        created_at = isoparse(d.pop("created_at"))




        runtime_sandbox_id = d.pop("runtime_sandbox_id", UNSET)

        runtime_cluster_id = d.pop("runtime_cluster_id", UNSET)

        runtime_context_id = d.pop("runtime_context_id", UNSET)

        _activated_at = d.pop("activated_at", UNSET)
        activated_at: Union[Unset, datetime.datetime]
        if isinstance(_activated_at,  Unset):
            activated_at = UNSET
        else:
            activated_at = isoparse(_activated_at)




        function_revision = cls(
            id=id,
            function_id=function_id,
            team_id=team_id,
            number=number,
            source=source,
            spec=spec,
            status=status,
            created_at=created_at,
            runtime_sandbox_id=runtime_sandbox_id,
            runtime_cluster_id=runtime_cluster_id,
            runtime_context_id=runtime_context_id,
            activated_at=activated_at,
        )


        function_revision.additional_properties = d
        return function_revision

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
