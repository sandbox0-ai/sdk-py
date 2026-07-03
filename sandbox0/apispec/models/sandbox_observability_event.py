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

from ..models.observability_event_source import ObservabilityEventSource
from ..models.sandbox_observability_event_type import SandboxObservabilityEventType
from ..models.sandbox_observability_outcome import SandboxObservabilityOutcome
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_observability_event_attributes import (
        SandboxObservabilityEventAttributes,
    )


T = TypeVar("T", bound="SandboxObservabilityEvent")


@_attrs_define
class SandboxObservabilityEvent:
    """
    Attributes:
        team_id (str):
        sandbox_id (str):
        region_id (str):
        cluster_id (str):
        occurred_at (datetime.datetime):
        ingested_at (datetime.datetime):
        source (ObservabilityEventSource):
        event_type (SandboxObservabilityEventType):
        cursor (str):
        watermark (str):
        outcome (Union[Unset, SandboxObservabilityOutcome]):
        attributes (Union[Unset, SandboxObservabilityEventAttributes]):
    """

    team_id: str
    sandbox_id: str
    region_id: str
    cluster_id: str
    occurred_at: datetime.datetime
    ingested_at: datetime.datetime
    source: ObservabilityEventSource
    event_type: SandboxObservabilityEventType
    cursor: str
    watermark: str
    outcome: Union[Unset, SandboxObservabilityOutcome] = UNSET
    attributes: Union[Unset, "SandboxObservabilityEventAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        sandbox_id = self.sandbox_id

        region_id = self.region_id

        cluster_id = self.cluster_id

        occurred_at = self.occurred_at.isoformat()

        ingested_at = self.ingested_at.isoformat()

        source = self.source.value

        event_type = self.event_type.value

        cursor = self.cursor

        watermark = self.watermark

        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "sandbox_id": sandbox_id,
                "region_id": region_id,
                "cluster_id": cluster_id,
                "occurred_at": occurred_at,
                "ingested_at": ingested_at,
                "source": source,
                "event_type": event_type,
                "cursor": cursor,
                "watermark": watermark,
            }
        )
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_observability_event_attributes import (
            SandboxObservabilityEventAttributes,
        )

        d = dict(src_dict)
        team_id = d.pop("team_id")

        sandbox_id = d.pop("sandbox_id")

        region_id = d.pop("region_id")

        cluster_id = d.pop("cluster_id")

        occurred_at = isoparse(d.pop("occurred_at"))

        ingested_at = isoparse(d.pop("ingested_at"))

        source = ObservabilityEventSource(d.pop("source"))

        event_type = SandboxObservabilityEventType(d.pop("event_type"))

        cursor = d.pop("cursor")

        watermark = d.pop("watermark")

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, SandboxObservabilityOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = SandboxObservabilityOutcome(_outcome)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, SandboxObservabilityEventAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = SandboxObservabilityEventAttributes.from_dict(_attributes)

        sandbox_observability_event = cls(
            team_id=team_id,
            sandbox_id=sandbox_id,
            region_id=region_id,
            cluster_id=cluster_id,
            occurred_at=occurred_at,
            ingested_at=ingested_at,
            source=source,
            event_type=event_type,
            cursor=cursor,
            watermark=watermark,
            outcome=outcome,
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
