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
    from ..models.sandbox_app_service_view import SandboxAppServiceView


T = TypeVar("T", bound="SuccessSandboxServicesResponseData")


@_attrs_define
class SuccessSandboxServicesResponseData:
    """
    Attributes:
        sandbox_id (str):
        services (list['SandboxAppServiceView']):
        exposure_domain (Union[Unset, str]):
    """

    sandbox_id: str
    services: list["SandboxAppServiceView"]
    exposure_domain: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()
            services.append(services_item)

        exposure_domain = self.exposure_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "services": services,
            }
        )
        if exposure_domain is not UNSET:
            field_dict["exposure_domain"] = exposure_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_app_service_view import SandboxAppServiceView

        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = SandboxAppServiceView.from_dict(services_item_data)

            services.append(services_item)

        exposure_domain = d.pop("exposure_domain", UNSET)

        success_sandbox_services_response_data = cls(
            sandbox_id=sandbox_id,
            services=services,
            exposure_domain=exposure_domain,
        )

        success_sandbox_services_response_data.additional_properties = d
        return success_sandbox_services_response_data

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
