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

from ..models.sandbox_observability_log_stream import SandboxObservabilityLogStream
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_observability_log_entry_attributes import (
        SandboxObservabilityLogEntryAttributes,
    )


T = TypeVar("T", bound="SandboxObservabilityLogEntry")


@_attrs_define
class SandboxObservabilityLogEntry:
    """
    Attributes:
        team_id (str):
        sandbox_id (str):
        region_id (str):
        cluster_id (str):
        occurred_at (datetime.datetime):
        ingested_at (datetime.datetime):
        message (str):
        cursor (str):
        context_id (Union[Unset, str]):
        process_id (Union[Unset, str]):
        stream (Union[Unset, SandboxObservabilityLogStream]):
        attributes (Union[Unset, SandboxObservabilityLogEntryAttributes]):
    """

    team_id: str
    sandbox_id: str
    region_id: str
    cluster_id: str
    occurred_at: datetime.datetime
    ingested_at: datetime.datetime
    message: str
    cursor: str
    context_id: Union[Unset, str] = UNSET
    process_id: Union[Unset, str] = UNSET
    stream: Union[Unset, SandboxObservabilityLogStream] = UNSET
    attributes: Union[Unset, "SandboxObservabilityLogEntryAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        sandbox_id = self.sandbox_id

        region_id = self.region_id

        cluster_id = self.cluster_id

        occurred_at = self.occurred_at.isoformat()

        ingested_at = self.ingested_at.isoformat()

        message = self.message

        cursor = self.cursor

        context_id = self.context_id

        process_id = self.process_id

        stream: Union[Unset, str] = UNSET
        if not isinstance(self.stream, Unset):
            stream = self.stream.value

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
                "message": message,
                "cursor": cursor,
            }
        )
        if context_id is not UNSET:
            field_dict["context_id"] = context_id
        if process_id is not UNSET:
            field_dict["process_id"] = process_id
        if stream is not UNSET:
            field_dict["stream"] = stream
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_observability_log_entry_attributes import (
            SandboxObservabilityLogEntryAttributes,
        )

        d = dict(src_dict)
        team_id = d.pop("team_id")

        sandbox_id = d.pop("sandbox_id")

        region_id = d.pop("region_id")

        cluster_id = d.pop("cluster_id")

        occurred_at = isoparse(d.pop("occurred_at"))

        ingested_at = isoparse(d.pop("ingested_at"))

        message = d.pop("message")

        cursor = d.pop("cursor")

        context_id = d.pop("context_id", UNSET)

        process_id = d.pop("process_id", UNSET)

        _stream = d.pop("stream", UNSET)
        stream: Union[Unset, SandboxObservabilityLogStream]
        if isinstance(_stream, Unset):
            stream = UNSET
        else:
            stream = SandboxObservabilityLogStream(_stream)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, SandboxObservabilityLogEntryAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = SandboxObservabilityLogEntryAttributes.from_dict(_attributes)

        sandbox_observability_log_entry = cls(
            team_id=team_id,
            sandbox_id=sandbox_id,
            region_id=region_id,
            cluster_id=cluster_id,
            occurred_at=occurred_at,
            ingested_at=ingested_at,
            message=message,
            cursor=cursor,
            context_id=context_id,
            process_id=process_id,
            stream=stream,
            attributes=attributes,
        )

        sandbox_observability_log_entry.additional_properties = d
        return sandbox_observability_log_entry

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
