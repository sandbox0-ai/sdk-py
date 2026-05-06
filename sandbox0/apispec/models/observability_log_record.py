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
    from ..models.observability_log_record_attributes import (
        ObservabilityLogRecordAttributes,
    )
    from ..models.observability_log_record_resource_attributes import (
        ObservabilityLogRecordResourceAttributes,
    )


T = TypeVar("T", bound="ObservabilityLogRecord")


@_attrs_define
class ObservabilityLogRecord:
    """
    Attributes:
        timestamp (Union[Unset, str]):
        trace_id (Union[Unset, str]):
        span_id (Union[Unset, str]):
        severity_text (Union[Unset, str]):
        severity_number (Union[Unset, int]):
        body (Union[Unset, str]):
        resource_attributes (Union[Unset, ObservabilityLogRecordResourceAttributes]):
        attributes (Union[Unset, ObservabilityLogRecordAttributes]):
    """

    timestamp: Union[Unset, str] = UNSET
    trace_id: Union[Unset, str] = UNSET
    span_id: Union[Unset, str] = UNSET
    severity_text: Union[Unset, str] = UNSET
    severity_number: Union[Unset, int] = UNSET
    body: Union[Unset, str] = UNSET
    resource_attributes: Union[Unset, "ObservabilityLogRecordResourceAttributes"] = (
        UNSET
    )
    attributes: Union[Unset, "ObservabilityLogRecordAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        trace_id = self.trace_id

        span_id = self.span_id

        severity_text = self.severity_text

        severity_number = self.severity_number

        body = self.body

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
        if severity_text is not UNSET:
            field_dict["severity_text"] = severity_text
        if severity_number is not UNSET:
            field_dict["severity_number"] = severity_number
        if body is not UNSET:
            field_dict["body"] = body
        if resource_attributes is not UNSET:
            field_dict["resource_attributes"] = resource_attributes
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observability_log_record_attributes import (
            ObservabilityLogRecordAttributes,
        )
        from ..models.observability_log_record_resource_attributes import (
            ObservabilityLogRecordResourceAttributes,
        )

        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        span_id = d.pop("span_id", UNSET)

        severity_text = d.pop("severity_text", UNSET)

        severity_number = d.pop("severity_number", UNSET)

        body = d.pop("body", UNSET)

        _resource_attributes = d.pop("resource_attributes", UNSET)
        resource_attributes: Union[Unset, ObservabilityLogRecordResourceAttributes]
        if isinstance(_resource_attributes, Unset):
            resource_attributes = UNSET
        else:
            resource_attributes = ObservabilityLogRecordResourceAttributes.from_dict(
                _resource_attributes
            )

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, ObservabilityLogRecordAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ObservabilityLogRecordAttributes.from_dict(_attributes)

        observability_log_record = cls(
            timestamp=timestamp,
            trace_id=trace_id,
            span_id=span_id,
            severity_text=severity_text,
            severity_number=severity_number,
            body=body,
            resource_attributes=resource_attributes,
            attributes=attributes,
        )

        observability_log_record.additional_properties = d
        return observability_log_record

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
