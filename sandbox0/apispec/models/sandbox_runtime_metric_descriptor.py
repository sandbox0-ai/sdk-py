from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_runtime_metric_kind import SandboxRuntimeMetricKind
from ..models.sandbox_runtime_metric_name import SandboxRuntimeMetricName
from ..models.sandbox_runtime_metric_unit import SandboxRuntimeMetricUnit

T = TypeVar("T", bound="SandboxRuntimeMetricDescriptor")


@_attrs_define
class SandboxRuntimeMetricDescriptor:
    """
    Attributes:
        name (SandboxRuntimeMetricName):
        kind (SandboxRuntimeMetricKind):
        unit (SandboxRuntimeMetricUnit):
        dimensions (list[str]):
        description (str):
    """

    name: SandboxRuntimeMetricName
    kind: SandboxRuntimeMetricKind
    unit: SandboxRuntimeMetricUnit
    dimensions: list[str]
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        kind = self.kind.value

        unit = self.unit.value

        dimensions = self.dimensions

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "unit": unit,
                "dimensions": dimensions,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = SandboxRuntimeMetricName(d.pop("name"))

        kind = SandboxRuntimeMetricKind(d.pop("kind"))

        unit = SandboxRuntimeMetricUnit(d.pop("unit"))

        dimensions = cast(list[str], d.pop("dimensions"))

        description = d.pop("description")

        sandbox_runtime_metric_descriptor = cls(
            name=name,
            kind=kind,
            unit=unit,
            dimensions=dimensions,
            description=description,
        )

        sandbox_runtime_metric_descriptor.additional_properties = d
        return sandbox_runtime_metric_descriptor

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
