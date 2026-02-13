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
    from ..models.exposed_port_config import ExposedPortConfig


T = TypeVar("T", bound="SuccessExposedPortsResponseData")


@_attrs_define
class SuccessExposedPortsResponseData:
    """
    Attributes:
        sandbox_id (str):
        exposed_ports (list['ExposedPortConfig']):
        exposure_domain (Union[Unset, str]): The base exposure domain (e.g., "aws-us-east-1.sandbox0.app").
            Useful for clients that need to construct URLs manually.
    """

    sandbox_id: str
    exposed_ports: list["ExposedPortConfig"]
    exposure_domain: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        exposed_ports = []
        for exposed_ports_item_data in self.exposed_ports:
            exposed_ports_item = exposed_ports_item_data.to_dict()
            exposed_ports.append(exposed_ports_item)

        exposure_domain = self.exposure_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "exposed_ports": exposed_ports,
            }
        )
        if exposure_domain is not UNSET:
            field_dict["exposure_domain"] = exposure_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exposed_port_config import ExposedPortConfig

        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        exposed_ports = []
        _exposed_ports = d.pop("exposed_ports")
        for exposed_ports_item_data in _exposed_ports:
            exposed_ports_item = ExposedPortConfig.from_dict(exposed_ports_item_data)

            exposed_ports.append(exposed_ports_item)

        exposure_domain = d.pop("exposure_domain", UNSET)

        success_exposed_ports_response_data = cls(
            sandbox_id=sandbox_id,
            exposed_ports=exposed_ports,
            exposure_domain=exposure_domain,
        )

        success_exposed_ports_response_data.additional_properties = d
        return success_exposed_ports_response_data

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
