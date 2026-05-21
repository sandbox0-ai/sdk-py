from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FunctionAutoscaling")


@_attrs_define
class FunctionAutoscaling:
    """Function runtime pool autoscaling settings. target_concurrency is a soft routing and scale-out signal; it is not a
    strong distributed per-instance concurrency semaphore.

        Attributes:
            min_warm (int): Minimum ready runtime sandboxes the autoscaler keeps after traffic has created capacity.
                Default: 0.
            max_active (int): Hard upper bound for active runtime sandboxes for the function. Default: 20.
            target_concurrency (int): Soft per-runtime in-flight request target used for routing and scale-out. Default: 80.
            scale_down_after_seconds (int): Idle time before the autoscaler removes extra runtime sandboxes above min_warm.
                Default: 300.
    """

    min_warm: int = 0
    max_active: int = 20
    target_concurrency: int = 80
    scale_down_after_seconds: int = 300
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_warm = self.min_warm

        max_active = self.max_active

        target_concurrency = self.target_concurrency

        scale_down_after_seconds = self.scale_down_after_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min_warm": min_warm,
                "max_active": max_active,
                "target_concurrency": target_concurrency,
                "scale_down_after_seconds": scale_down_after_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_warm = d.pop("min_warm")

        max_active = d.pop("max_active")

        target_concurrency = d.pop("target_concurrency")

        scale_down_after_seconds = d.pop("scale_down_after_seconds")

        function_autoscaling = cls(
            min_warm=min_warm,
            max_active=max_active,
            target_concurrency=target_concurrency,
            scale_down_after_seconds=scale_down_after_seconds,
        )

        function_autoscaling.additional_properties = d
        return function_autoscaling

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
