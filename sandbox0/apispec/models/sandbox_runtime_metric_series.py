from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_runtime_metric_kind import SandboxRuntimeMetricKind
from ..models.sandbox_runtime_metric_name import SandboxRuntimeMetricName
from ..models.sandbox_runtime_metric_statistic import SandboxRuntimeMetricStatistic
from ..models.sandbox_runtime_metric_unit import SandboxRuntimeMetricUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_runtime_metric_segment import SandboxRuntimeMetricSegment
    from ..models.sandbox_runtime_metric_series_dimensions import (
        SandboxRuntimeMetricSeriesDimensions,
    )


T = TypeVar("T", bound="SandboxRuntimeMetricSeries")


@_attrs_define
class SandboxRuntimeMetricSeries:
    """
    Attributes:
        metric (SandboxRuntimeMetricName):
        kind (SandboxRuntimeMetricKind):
        unit (SandboxRuntimeMetricUnit):
        statistic (SandboxRuntimeMetricStatistic):
        segments (list['SandboxRuntimeMetricSegment']):
        dimensions (Union[Unset, SandboxRuntimeMetricSeriesDimensions]):
    """

    metric: SandboxRuntimeMetricName
    kind: SandboxRuntimeMetricKind
    unit: SandboxRuntimeMetricUnit
    statistic: SandboxRuntimeMetricStatistic
    segments: list["SandboxRuntimeMetricSegment"]
    dimensions: Union[Unset, "SandboxRuntimeMetricSeriesDimensions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric.value

        kind = self.kind.value

        unit = self.unit.value

        statistic = self.statistic.value

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        dimensions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "kind": kind,
                "unit": unit,
                "statistic": statistic,
                "segments": segments,
            }
        )
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_runtime_metric_segment import SandboxRuntimeMetricSegment
        from ..models.sandbox_runtime_metric_series_dimensions import (
            SandboxRuntimeMetricSeriesDimensions,
        )

        d = dict(src_dict)
        metric = SandboxRuntimeMetricName(d.pop("metric"))

        kind = SandboxRuntimeMetricKind(d.pop("kind"))

        unit = SandboxRuntimeMetricUnit(d.pop("unit"))

        statistic = SandboxRuntimeMetricStatistic(d.pop("statistic"))

        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = SandboxRuntimeMetricSegment.from_dict(segments_item_data)

            segments.append(segments_item)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: Union[Unset, SandboxRuntimeMetricSeriesDimensions]
        if isinstance(_dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = SandboxRuntimeMetricSeriesDimensions.from_dict(_dimensions)

        sandbox_runtime_metric_series = cls(
            metric=metric,
            kind=kind,
            unit=unit,
            statistic=statistic,
            segments=segments,
            dimensions=dimensions,
        )

        sandbox_runtime_metric_series.additional_properties = d
        return sandbox_runtime_metric_series

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
