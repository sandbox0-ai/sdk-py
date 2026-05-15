from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SandboxAppServiceRouteRateLimit")


@_attrs_define
class SandboxAppServiceRouteRateLimit:
    """
    Attributes:
        rps (int):
        burst (int):
    """

    rps: int
    burst: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rps = self.rps

        burst = self.burst

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rps": rps,
                "burst": burst,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rps = d.pop("rps")

        burst = d.pop("burst")

        sandbox_app_service_route_rate_limit = cls(
            rps=rps,
            burst=burst,
        )

        sandbox_app_service_route_rate_limit.additional_properties = d
        return sandbox_app_service_route_rate_limit

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
