from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sandbox_app_service import SandboxAppService


T = TypeVar("T", bound="SandboxServicesUpdateRequest")


@_attrs_define
class SandboxServicesUpdateRequest:
    """
    Attributes:
        services (list['SandboxAppService']):
    """

    services: list["SandboxAppService"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()
            services.append(services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "services": services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_app_service import SandboxAppService

        d = dict(src_dict)
        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = SandboxAppService.from_dict(services_item_data)

            services.append(services_item)

        sandbox_services_update_request = cls(
            services=services,
        )

        sandbox_services_update_request.additional_properties = d
        return sandbox_services_update_request

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
