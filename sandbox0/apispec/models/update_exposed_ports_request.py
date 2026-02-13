from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exposed_port_config import ExposedPortConfig


T = TypeVar("T", bound="UpdateExposedPortsRequest")


@_attrs_define
class UpdateExposedPortsRequest:
    """
    Attributes:
        ports (list['ExposedPortConfig']):
    """

    ports: list["ExposedPortConfig"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ports = []
        for ports_item_data in self.ports:
            ports_item = ports_item_data.to_dict()
            ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ports": ports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exposed_port_config import ExposedPortConfig

        d = dict(src_dict)
        ports = []
        _ports = d.pop("ports")
        for ports_item_data in _ports:
            ports_item = ExposedPortConfig.from_dict(ports_item_data)

            ports.append(ports_item)

        update_exposed_ports_request = cls(
            ports=ports,
        )

        update_exposed_ports_request.additional_properties = d
        return update_exposed_ports_request

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
