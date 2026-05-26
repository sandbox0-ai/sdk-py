from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.run_revision_status import RunRevisionStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.run_revision_spec import RunRevisionSpec
  from ..models.run_source import RunSource





T = TypeVar("T", bound="RunRevision")



@_attrs_define
class RunRevision:
    """ 
        Attributes:
            id (str):
            run_id (str):
            team_id (str):
            number (int):
            source (RunSource):
            spec (RunRevisionSpec): Canonical runtime contract compiled from every run deploy mode.
            status (RunRevisionStatus):
            created_at (datetime.datetime):
            runtime_sandbox_id (Union[Unset, str]):
            runtime_cluster_id (Union[Unset, str]):
            runtime_context_id (Union[Unset, str]):
            activated_at (Union[Unset, datetime.datetime]):
     """

    id: str
    run_id: str
    team_id: str
    number: int
    source: 'RunSource'
    spec: 'RunRevisionSpec'
    status: RunRevisionStatus
    created_at: datetime.datetime
    runtime_sandbox_id: Union[Unset, str] = UNSET
    runtime_cluster_id: Union[Unset, str] = UNSET
    runtime_context_id: Union[Unset, str] = UNSET
    activated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_revision_spec import RunRevisionSpec
        from ..models.run_source import RunSource
        id = self.id

        run_id = self.run_id

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
            "run_id": run_id,
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
        from ..models.run_revision_spec import RunRevisionSpec
        from ..models.run_source import RunSource
        d = dict(src_dict)
        id = d.pop("id")

        run_id = d.pop("run_id")

        team_id = d.pop("team_id")

        number = d.pop("number")

        source = RunSource.from_dict(d.pop("source"))




        spec = RunRevisionSpec.from_dict(d.pop("spec"))




        status = RunRevisionStatus(d.pop("status"))




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




        run_revision = cls(
            id=id,
            run_id=run_id,
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


        run_revision.additional_properties = d
        return run_revision

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
