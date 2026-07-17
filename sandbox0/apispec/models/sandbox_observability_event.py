import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.observability_event_source import ObservabilityEventSource
from ..models.sandbox_audit_event_phase import SandboxAuditEventPhase
from ..models.sandbox_observability_event_schema_version import (
    SandboxObservabilityEventSchemaVersion,
)
from ..models.sandbox_observability_event_type import SandboxObservabilityEventType
from ..models.sandbox_observability_outcome import SandboxObservabilityOutcome
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_audit_actor import SandboxAuditActor
    from ..models.sandbox_audit_integrity import SandboxAuditIntegrity
    from ..models.sandbox_audit_producer import SandboxAuditProducer
    from ..models.sandbox_audit_request import SandboxAuditRequest
    from ..models.sandbox_audit_resource import SandboxAuditResource
    from ..models.sandbox_observability_event_attributes import (
        SandboxObservabilityEventAttributes,
    )


T = TypeVar("T", bound="SandboxObservabilityEvent")


@_attrs_define
class SandboxObservabilityEvent:
    """
    Attributes:
        event_id (UUID):
        schema_version (SandboxObservabilityEventSchemaVersion):
        team_id (str):
        sandbox_id (str):
        region_id (str):
        cluster_id (str):
        occurred_at (datetime.datetime):
        ingested_at (datetime.datetime):
        source (ObservabilityEventSource):
        event_type (SandboxObservabilityEventType):
        phase (SandboxAuditEventPhase):
        outcome (SandboxObservabilityOutcome):
        actor (SandboxAuditActor):
        action (str):
        resource (SandboxAuditResource):
        operation_id (str):
        producer (SandboxAuditProducer):
        integrity (SandboxAuditIntegrity):
        parent_event_id (Union[Unset, UUID]):
        request (Union[Unset, SandboxAuditRequest]):
        attributes (Union[Unset, SandboxObservabilityEventAttributes]):
    """

    event_id: UUID
    schema_version: SandboxObservabilityEventSchemaVersion
    team_id: str
    sandbox_id: str
    region_id: str
    cluster_id: str
    occurred_at: datetime.datetime
    ingested_at: datetime.datetime
    source: ObservabilityEventSource
    event_type: SandboxObservabilityEventType
    phase: SandboxAuditEventPhase
    outcome: SandboxObservabilityOutcome
    actor: "SandboxAuditActor"
    action: str
    resource: "SandboxAuditResource"
    operation_id: str
    producer: "SandboxAuditProducer"
    integrity: "SandboxAuditIntegrity"
    parent_event_id: Union[Unset, UUID] = UNSET
    request: Union[Unset, "SandboxAuditRequest"] = UNSET
    attributes: Union[Unset, "SandboxObservabilityEventAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = str(self.event_id)

        schema_version = self.schema_version.value

        team_id = self.team_id

        sandbox_id = self.sandbox_id

        region_id = self.region_id

        cluster_id = self.cluster_id

        occurred_at = self.occurred_at.isoformat()

        ingested_at = self.ingested_at.isoformat()

        source = self.source.value

        event_type = self.event_type.value

        phase = self.phase.value

        outcome = self.outcome.value

        actor = self.actor.to_dict()

        action = self.action

        resource = self.resource.to_dict()

        operation_id = self.operation_id

        producer = self.producer.to_dict()

        integrity = self.integrity.to_dict()

        parent_event_id: Union[Unset, str] = UNSET
        if not isinstance(self.parent_event_id, Unset):
            parent_event_id = str(self.parent_event_id)

        request: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_id": event_id,
                "schema_version": schema_version,
                "team_id": team_id,
                "sandbox_id": sandbox_id,
                "region_id": region_id,
                "cluster_id": cluster_id,
                "occurred_at": occurred_at,
                "ingested_at": ingested_at,
                "source": source,
                "event_type": event_type,
                "phase": phase,
                "outcome": outcome,
                "actor": actor,
                "action": action,
                "resource": resource,
                "operation_id": operation_id,
                "producer": producer,
                "integrity": integrity,
            }
        )
        if parent_event_id is not UNSET:
            field_dict["parent_event_id"] = parent_event_id
        if request is not UNSET:
            field_dict["request"] = request
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_audit_actor import SandboxAuditActor
        from ..models.sandbox_audit_integrity import SandboxAuditIntegrity
        from ..models.sandbox_audit_producer import SandboxAuditProducer
        from ..models.sandbox_audit_request import SandboxAuditRequest
        from ..models.sandbox_audit_resource import SandboxAuditResource
        from ..models.sandbox_observability_event_attributes import (
            SandboxObservabilityEventAttributes,
        )

        d = dict(src_dict)
        event_id = UUID(d.pop("event_id"))

        schema_version = SandboxObservabilityEventSchemaVersion(d.pop("schema_version"))

        team_id = d.pop("team_id")

        sandbox_id = d.pop("sandbox_id")

        region_id = d.pop("region_id")

        cluster_id = d.pop("cluster_id")

        occurred_at = isoparse(d.pop("occurred_at"))

        ingested_at = isoparse(d.pop("ingested_at"))

        source = ObservabilityEventSource(d.pop("source"))

        event_type = SandboxObservabilityEventType(d.pop("event_type"))

        phase = SandboxAuditEventPhase(d.pop("phase"))

        outcome = SandboxObservabilityOutcome(d.pop("outcome"))

        actor = SandboxAuditActor.from_dict(d.pop("actor"))

        action = d.pop("action")

        resource = SandboxAuditResource.from_dict(d.pop("resource"))

        operation_id = d.pop("operation_id")

        producer = SandboxAuditProducer.from_dict(d.pop("producer"))

        integrity = SandboxAuditIntegrity.from_dict(d.pop("integrity"))

        _parent_event_id = d.pop("parent_event_id", UNSET)
        parent_event_id: Union[Unset, UUID]
        if isinstance(_parent_event_id, Unset):
            parent_event_id = UNSET
        else:
            parent_event_id = UUID(_parent_event_id)

        _request = d.pop("request", UNSET)
        request: Union[Unset, SandboxAuditRequest]
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = SandboxAuditRequest.from_dict(_request)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, SandboxObservabilityEventAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = SandboxObservabilityEventAttributes.from_dict(_attributes)

        sandbox_observability_event = cls(
            event_id=event_id,
            schema_version=schema_version,
            team_id=team_id,
            sandbox_id=sandbox_id,
            region_id=region_id,
            cluster_id=cluster_id,
            occurred_at=occurred_at,
            ingested_at=ingested_at,
            source=source,
            event_type=event_type,
            phase=phase,
            outcome=outcome,
            actor=actor,
            action=action,
            resource=resource,
            operation_id=operation_id,
            producer=producer,
            integrity=integrity,
            parent_event_id=parent_event_id,
            request=request,
            attributes=attributes,
        )

        sandbox_observability_event.additional_properties = d
        return sandbox_observability_event

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
