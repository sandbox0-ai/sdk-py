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
    from ..models.sandbox_observability_effective_event_query import (
        SandboxObservabilityEffectiveEventQuery,
    )
    from ..models.sandbox_observability_event import SandboxObservabilityEvent


T = TypeVar("T", bound="SandboxObservabilityEventsResponse")


@_attrs_define
class SandboxObservabilityEventsResponse:
    """
    Attributes:
        events (list['SandboxObservabilityEvent']):
        effective_query (SandboxObservabilityEffectiveEventQuery): Normalized schema ceiling and execution-scope filters
            applied by the
            server. This metadata is returned even when no events match.
        next_cursor (Union[Unset, str]):
        watermark (Union[Unset, str]):
    """

    events: list["SandboxObservabilityEvent"]
    effective_query: "SandboxObservabilityEffectiveEventQuery"
    next_cursor: Union[Unset, str] = UNSET
    watermark: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        effective_query = self.effective_query.to_dict()

        next_cursor = self.next_cursor

        watermark = self.watermark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "effective_query": effective_query,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if watermark is not UNSET:
            field_dict["watermark"] = watermark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_observability_effective_event_query import (
            SandboxObservabilityEffectiveEventQuery,
        )
        from ..models.sandbox_observability_event import SandboxObservabilityEvent

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = SandboxObservabilityEvent.from_dict(events_item_data)

            events.append(events_item)

        effective_query = SandboxObservabilityEffectiveEventQuery.from_dict(
            d.pop("effective_query")
        )

        next_cursor = d.pop("next_cursor", UNSET)

        watermark = d.pop("watermark", UNSET)

        sandbox_observability_events_response = cls(
            events=events,
            effective_query=effective_query,
            next_cursor=next_cursor,
            watermark=watermark,
        )

        sandbox_observability_events_response.additional_properties = d
        return sandbox_observability_events_response

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
