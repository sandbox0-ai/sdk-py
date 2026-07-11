import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.sandbox_runtime_metric_freshness import SandboxRuntimeMetricFreshness
    from ..models.sandbox_runtime_metric_gap import SandboxRuntimeMetricGap
    from ..models.sandbox_runtime_metric_series import SandboxRuntimeMetricSeries


T = TypeVar("T", bound="SandboxRuntimeMetricsResponse")


@_attrs_define
class SandboxRuntimeMetricsResponse:
    """
    Attributes:
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        step_seconds (int):
        series (list['SandboxRuntimeMetricSeries']):
        freshness (SandboxRuntimeMetricFreshness): Freshness is measured relative to the requested end_time, including
            for historical queries.
        gaps (list['SandboxRuntimeMetricGap']):
        partial (bool):
    """

    start_time: datetime.datetime
    end_time: datetime.datetime
    step_seconds: int
    series: list["SandboxRuntimeMetricSeries"]
    freshness: "SandboxRuntimeMetricFreshness"
    gaps: list["SandboxRuntimeMetricGap"]
    partial: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        step_seconds = self.step_seconds

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        freshness = self.freshness.to_dict()

        gaps = []
        for gaps_item_data in self.gaps:
            gaps_item = gaps_item_data.to_dict()
            gaps.append(gaps_item)

        partial = self.partial

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_time": start_time,
                "end_time": end_time,
                "step_seconds": step_seconds,
                "series": series,
                "freshness": freshness,
                "gaps": gaps,
                "partial": partial,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_runtime_metric_freshness import (
            SandboxRuntimeMetricFreshness,
        )
        from ..models.sandbox_runtime_metric_gap import SandboxRuntimeMetricGap
        from ..models.sandbox_runtime_metric_series import SandboxRuntimeMetricSeries

        d = dict(src_dict)
        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        step_seconds = d.pop("step_seconds")

        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = SandboxRuntimeMetricSeries.from_dict(series_item_data)

            series.append(series_item)

        freshness = SandboxRuntimeMetricFreshness.from_dict(d.pop("freshness"))

        gaps = []
        _gaps = d.pop("gaps")
        for gaps_item_data in _gaps:
            gaps_item = SandboxRuntimeMetricGap.from_dict(gaps_item_data)

            gaps.append(gaps_item)

        partial = d.pop("partial")

        sandbox_runtime_metrics_response = cls(
            start_time=start_time,
            end_time=end_time,
            step_seconds=step_seconds,
            series=series,
            freshness=freshness,
            gaps=gaps,
            partial=partial,
        )

        sandbox_runtime_metrics_response.additional_properties = d
        return sandbox_runtime_metrics_response

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
