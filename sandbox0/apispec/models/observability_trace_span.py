from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observability_trace_span_attributes import (
        ObservabilityTraceSpanAttributes,
    )
    from ..models.observability_trace_span_resource_attributes import (
        ObservabilityTraceSpanResourceAttributes,
    )


T = TypeVar("T", bound="ObservabilityTraceSpan")


@_attrs_define
class ObservabilityTraceSpan:
    """
    Attributes:
        timestamp (Union[Unset, str]):
        trace_id (Union[Unset, str]):
        span_id (Union[Unset, str]):
        parent_span_id (Union[Unset, str]):
        service_name (Union[Unset, str]):
        name (Union[Unset, str]):
        kind (Union[Unset, str]):
        duration_nano (Union[Unset, int]):
        status_code (Union[Unset, str]):
        status_message (Union[Unset, str]):
        resource_attributes (Union[Unset, ObservabilityTraceSpanResourceAttributes]):
        attributes (Union[Unset, ObservabilityTraceSpanAttributes]):
    """

    timestamp: Union[Unset, str] = UNSET
    trace_id: Union[Unset, str] = UNSET
    span_id: Union[Unset, str] = UNSET
    parent_span_id: Union[Unset, str] = UNSET
    service_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    duration_nano: Union[Unset, int] = UNSET
    status_code: Union[Unset, str] = UNSET
    status_message: Union[Unset, str] = UNSET
    resource_attributes: Union[Unset, "ObservabilityTraceSpanResourceAttributes"] = (
        UNSET
    )
    attributes: Union[Unset, "ObservabilityTraceSpanAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        trace_id = self.trace_id

        span_id = self.span_id

        parent_span_id = self.parent_span_id

        service_name = self.service_name

        name = self.name

        kind = self.kind

        duration_nano = self.duration_nano

        status_code = self.status_code

        status_message = self.status_message

        resource_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resource_attributes, Unset):
            resource_attributes = self.resource_attributes.to_dict()

        attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if parent_span_id is not UNSET:
            field_dict["parent_span_id"] = parent_span_id
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if name is not UNSET:
            field_dict["name"] = name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if duration_nano is not UNSET:
            field_dict["duration_nano"] = duration_nano
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if resource_attributes is not UNSET:
            field_dict["resource_attributes"] = resource_attributes
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observability_trace_span_attributes import (
            ObservabilityTraceSpanAttributes,
        )
        from ..models.observability_trace_span_resource_attributes import (
            ObservabilityTraceSpanResourceAttributes,
        )

        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        span_id = d.pop("span_id", UNSET)

        parent_span_id = d.pop("parent_span_id", UNSET)

        service_name = d.pop("service_name", UNSET)

        name = d.pop("name", UNSET)

        kind = d.pop("kind", UNSET)

        duration_nano = d.pop("duration_nano", UNSET)

        status_code = d.pop("status_code", UNSET)

        status_message = d.pop("status_message", UNSET)

        _resource_attributes = d.pop("resource_attributes", UNSET)
        resource_attributes: Union[Unset, ObservabilityTraceSpanResourceAttributes]
        if isinstance(_resource_attributes, Unset):
            resource_attributes = UNSET
        else:
            resource_attributes = ObservabilityTraceSpanResourceAttributes.from_dict(
                _resource_attributes
            )

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, ObservabilityTraceSpanAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ObservabilityTraceSpanAttributes.from_dict(_attributes)

        observability_trace_span = cls(
            timestamp=timestamp,
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=parent_span_id,
            service_name=service_name,
            name=name,
            kind=kind,
            duration_nano=duration_nano,
            status_code=status_code,
            status_message=status_message,
            resource_attributes=resource_attributes,
            attributes=attributes,
        )

        observability_trace_span.additional_properties = d
        return observability_trace_span

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
