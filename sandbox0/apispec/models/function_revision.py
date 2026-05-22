import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.function_revision_source_type import FunctionRevisionSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_restore_mount import FunctionRestoreMount
    from ..models.function_revision_provenance import FunctionRevisionProvenance
    from ..models.function_revision_spec import FunctionRevisionSpec
    from ..models.sandbox_app_service import SandboxAppService


T = TypeVar("T", bound="FunctionRevision")


@_attrs_define
class FunctionRevision:
    """
    Attributes:
        id (str):
        function_id (str):
        team_id (str):
        revision_number (int):
        source_type (FunctionRevisionSourceType):
        revision_spec (FunctionRevisionSpec): Immutable execution contract used by Function Gateway to serve a revision.
        created_at (datetime.datetime):
        provenance (Union[Unset, FunctionRevisionProvenance]): Non-execution metadata describing how the revision spec
            was produced.
        source_sandbox_id (Union[Unset, str]): Compatibility mirror for sandbox-service revisions.
        source_service_id (Union[Unset, str]): Compatibility mirror for sandbox-service revisions.
        source_template_id (Union[Unset, str]): Compatibility mirror of revision_spec.template_id.
        restore_mounts (Union[Unset, list['FunctionRestoreMount']]): Compatibility mirror of revision_spec.mounts for
            prepared SandboxVolume mounts.
        service_snapshot (Union[Unset, SandboxAppService]): Canonical service model for sandbox exposure and function
            publishing.
        runtime_sandbox_id (Union[Unset, str]): Current restored runtime sandbox serving the revision, if one exists.
        runtime_context_id (Union[Unset, str]): Current runtime process context inside the restored runtime sandbox.
        runtime_updated_at (Union[Unset, datetime.datetime]): Last time the restored runtime sandbox mapping was
            updated.
        created_by (Union[Unset, str]):
    """

    id: str
    function_id: str
    team_id: str
    revision_number: int
    source_type: FunctionRevisionSourceType
    revision_spec: "FunctionRevisionSpec"
    created_at: datetime.datetime
    provenance: Union[Unset, "FunctionRevisionProvenance"] = UNSET
    source_sandbox_id: Union[Unset, str] = UNSET
    source_service_id: Union[Unset, str] = UNSET
    source_template_id: Union[Unset, str] = UNSET
    restore_mounts: Union[Unset, list["FunctionRestoreMount"]] = UNSET
    service_snapshot: Union[Unset, "SandboxAppService"] = UNSET
    runtime_sandbox_id: Union[Unset, str] = UNSET
    runtime_context_id: Union[Unset, str] = UNSET
    runtime_updated_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        function_id = self.function_id

        team_id = self.team_id

        revision_number = self.revision_number

        source_type = self.source_type.value

        revision_spec = self.revision_spec.to_dict()

        created_at = self.created_at.isoformat()

        provenance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.provenance, Unset):
            provenance = self.provenance.to_dict()

        source_sandbox_id = self.source_sandbox_id

        source_service_id = self.source_service_id

        source_template_id = self.source_template_id

        restore_mounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.restore_mounts, Unset):
            restore_mounts = []
            for restore_mounts_item_data in self.restore_mounts:
                restore_mounts_item = restore_mounts_item_data.to_dict()
                restore_mounts.append(restore_mounts_item)

        service_snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_snapshot, Unset):
            service_snapshot = self.service_snapshot.to_dict()

        runtime_sandbox_id = self.runtime_sandbox_id

        runtime_context_id = self.runtime_context_id

        runtime_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.runtime_updated_at, Unset):
            runtime_updated_at = self.runtime_updated_at.isoformat()

        created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "function_id": function_id,
                "team_id": team_id,
                "revision_number": revision_number,
                "source_type": source_type,
                "revision_spec": revision_spec,
                "created_at": created_at,
            }
        )
        if provenance is not UNSET:
            field_dict["provenance"] = provenance
        if source_sandbox_id is not UNSET:
            field_dict["source_sandbox_id"] = source_sandbox_id
        if source_service_id is not UNSET:
            field_dict["source_service_id"] = source_service_id
        if source_template_id is not UNSET:
            field_dict["source_template_id"] = source_template_id
        if restore_mounts is not UNSET:
            field_dict["restore_mounts"] = restore_mounts
        if service_snapshot is not UNSET:
            field_dict["service_snapshot"] = service_snapshot
        if runtime_sandbox_id is not UNSET:
            field_dict["runtime_sandbox_id"] = runtime_sandbox_id
        if runtime_context_id is not UNSET:
            field_dict["runtime_context_id"] = runtime_context_id
        if runtime_updated_at is not UNSET:
            field_dict["runtime_updated_at"] = runtime_updated_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_restore_mount import FunctionRestoreMount
        from ..models.function_revision_provenance import FunctionRevisionProvenance
        from ..models.function_revision_spec import FunctionRevisionSpec
        from ..models.sandbox_app_service import SandboxAppService

        d = dict(src_dict)
        id = d.pop("id")

        function_id = d.pop("function_id")

        team_id = d.pop("team_id")

        revision_number = d.pop("revision_number")

        source_type = FunctionRevisionSourceType(d.pop("source_type"))

        revision_spec = FunctionRevisionSpec.from_dict(d.pop("revision_spec"))

        created_at = isoparse(d.pop("created_at"))

        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, FunctionRevisionProvenance]
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = FunctionRevisionProvenance.from_dict(_provenance)

        source_sandbox_id = d.pop("source_sandbox_id", UNSET)

        source_service_id = d.pop("source_service_id", UNSET)

        source_template_id = d.pop("source_template_id", UNSET)

        restore_mounts = []
        _restore_mounts = d.pop("restore_mounts", UNSET)
        for restore_mounts_item_data in _restore_mounts or []:
            restore_mounts_item = FunctionRestoreMount.from_dict(
                restore_mounts_item_data
            )

            restore_mounts.append(restore_mounts_item)

        _service_snapshot = d.pop("service_snapshot", UNSET)
        service_snapshot: Union[Unset, SandboxAppService]
        if isinstance(_service_snapshot, Unset):
            service_snapshot = UNSET
        else:
            service_snapshot = SandboxAppService.from_dict(_service_snapshot)

        runtime_sandbox_id = d.pop("runtime_sandbox_id", UNSET)

        runtime_context_id = d.pop("runtime_context_id", UNSET)

        _runtime_updated_at = d.pop("runtime_updated_at", UNSET)
        runtime_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_runtime_updated_at, Unset):
            runtime_updated_at = UNSET
        else:
            runtime_updated_at = isoparse(_runtime_updated_at)

        created_by = d.pop("created_by", UNSET)

        function_revision = cls(
            id=id,
            function_id=function_id,
            team_id=team_id,
            revision_number=revision_number,
            source_type=source_type,
            revision_spec=revision_spec,
            created_at=created_at,
            provenance=provenance,
            source_sandbox_id=source_sandbox_id,
            source_service_id=source_service_id,
            source_template_id=source_template_id,
            restore_mounts=restore_mounts,
            service_snapshot=service_snapshot,
            runtime_sandbox_id=runtime_sandbox_id,
            runtime_context_id=runtime_context_id,
            runtime_updated_at=runtime_updated_at,
            created_by=created_by,
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
