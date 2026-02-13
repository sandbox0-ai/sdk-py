from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_spec import PortSpec


T = TypeVar("T", bound="NetworkEgressPolicy")


@_attrs_define
class NetworkEgressPolicy:
    """
    Attributes:
        allowed_cidrs (Union[Unset, list[str]]):
        allowed_domains (Union[Unset, list[str]]):
        allowed_ports (Union[Unset, list['PortSpec']]):
        denied_domains (Union[Unset, list[str]]):
        denied_cidrs (Union[Unset, list[str]]):
        denied_ports (Union[Unset, list['PortSpec']]):
    """

    allowed_cidrs: Union[Unset, list[str]] = UNSET
    allowed_domains: Union[Unset, list[str]] = UNSET
    allowed_ports: Union[Unset, list["PortSpec"]] = UNSET
    denied_domains: Union[Unset, list[str]] = UNSET
    denied_cidrs: Union[Unset, list[str]] = UNSET
    denied_ports: Union[Unset, list["PortSpec"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_cidrs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_cidrs, Unset):
            allowed_cidrs = self.allowed_cidrs

        allowed_domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_domains, Unset):
            allowed_domains = self.allowed_domains

        allowed_ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allowed_ports, Unset):
            allowed_ports = []
            for allowed_ports_item_data in self.allowed_ports:
                allowed_ports_item = allowed_ports_item_data.to_dict()
                allowed_ports.append(allowed_ports_item)

        denied_domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.denied_domains, Unset):
            denied_domains = self.denied_domains

        denied_cidrs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.denied_cidrs, Unset):
            denied_cidrs = self.denied_cidrs

        denied_ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.denied_ports, Unset):
            denied_ports = []
            for denied_ports_item_data in self.denied_ports:
                denied_ports_item = denied_ports_item_data.to_dict()
                denied_ports.append(denied_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_cidrs is not UNSET:
            field_dict["allowedCidrs"] = allowed_cidrs
        if allowed_domains is not UNSET:
            field_dict["allowedDomains"] = allowed_domains
        if allowed_ports is not UNSET:
            field_dict["allowedPorts"] = allowed_ports
        if denied_domains is not UNSET:
            field_dict["deniedDomains"] = denied_domains
        if denied_cidrs is not UNSET:
            field_dict["deniedCidrs"] = denied_cidrs
        if denied_ports is not UNSET:
            field_dict["deniedPorts"] = denied_ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.port_spec import PortSpec

        d = dict(src_dict)
        allowed_cidrs = cast(list[str], d.pop("allowedCidrs", UNSET))

        allowed_domains = cast(list[str], d.pop("allowedDomains", UNSET))

        allowed_ports = []
        _allowed_ports = d.pop("allowedPorts", UNSET)
        for allowed_ports_item_data in _allowed_ports or []:
            allowed_ports_item = PortSpec.from_dict(allowed_ports_item_data)

            allowed_ports.append(allowed_ports_item)

        denied_domains = cast(list[str], d.pop("deniedDomains", UNSET))

        denied_cidrs = cast(list[str], d.pop("deniedCidrs", UNSET))

        denied_ports = []
        _denied_ports = d.pop("deniedPorts", UNSET)
        for denied_ports_item_data in _denied_ports or []:
            denied_ports_item = PortSpec.from_dict(denied_ports_item_data)

            denied_ports.append(denied_ports_item)

        network_egress_policy = cls(
            allowed_cidrs=allowed_cidrs,
            allowed_domains=allowed_domains,
            allowed_ports=allowed_ports,
            denied_domains=denied_domains,
            denied_cidrs=denied_cidrs,
            denied_ports=denied_ports,
        )

        network_egress_policy.additional_properties = d
        return network_egress_policy

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
