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

from ..models.sandbox_runtime_metric_gap_reason import SandboxRuntimeMetricGapReason
from ..models.sandbox_runtime_metric_name import SandboxRuntimeMetricName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_runtime_metric_gap_dimensions import (
        SandboxRuntimeMetricGapDimensions,
    )


T = TypeVar("T", bound="SandboxRuntimeMetricGap")


@_attrs_define
class SandboxRuntimeMetricGap:
    """
    Attributes:
        metric (SandboxRuntimeMetricName):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        reason (SandboxRuntimeMetricGapReason):
        dimensions (Union[Unset, SandboxRuntimeMetricGapDimensions]):
    """

    metric: SandboxRuntimeMetricName
    start_time: datetime.datetime
    end_time: datetime.datetime
    reason: SandboxRuntimeMetricGapReason
    dimensions: Union[Unset, "SandboxRuntimeMetricGapDimensions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric.value

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        reason = self.reason.value

        dimensions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "start_time": start_time,
                "end_time": end_time,
                "reason": reason,
            }
        )
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_runtime_metric_gap_dimensions import (
            SandboxRuntimeMetricGapDimensions,
        )

        d = dict(src_dict)
        metric = SandboxRuntimeMetricName(d.pop("metric"))

        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        reason = SandboxRuntimeMetricGapReason(d.pop("reason"))

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: Union[Unset, SandboxRuntimeMetricGapDimensions]
        if isinstance(_dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = SandboxRuntimeMetricGapDimensions.from_dict(_dimensions)

        sandbox_runtime_metric_gap = cls(
            metric=metric,
            start_time=start_time,
            end_time=end_time,
            reason=reason,
            dimensions=dimensions,
        )

        sandbox_runtime_metric_gap.additional_properties = d
        return sandbox_runtime_metric_gap

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
