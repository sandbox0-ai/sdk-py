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

from ..models.traffic_rule_action import TrafficRuleAction
from ..models.traffic_rule_app_protocol import TrafficRuleAppProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_spec import PortSpec


T = TypeVar("T", bound="TrafficRule")


@_attrs_define
class TrafficRule:
    """
    Attributes:
        action (TrafficRuleAction):
        name (Union[Unset, str]): Optional stable identifier used for merge and replacement.
        cidrs (Union[Unset, list[str]]): CIDR match list for the rule.
        domains (Union[Unset, list[str]]): Domain match list for the rule.
        ports (Union[Unset, list['PortSpec']]): Port/protocol constraints for the rule.
        app_protocols (Union[Unset, list[TrafficRuleAppProtocol]]): Classified application protocols matched by the
            rule.
    """

    action: TrafficRuleAction
    name: Union[Unset, str] = UNSET
    cidrs: Union[Unset, list[str]] = UNSET
    domains: Union[Unset, list[str]] = UNSET
    ports: Union[Unset, list["PortSpec"]] = UNSET
    app_protocols: Union[Unset, list[TrafficRuleAppProtocol]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        name = self.name

        cidrs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cidrs, Unset):
            cidrs = self.cidrs

        domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        app_protocols: Union[Unset, list[str]] = UNSET
        if not isinstance(self.app_protocols, Unset):
            app_protocols = []
            for app_protocols_item_data in self.app_protocols:
                app_protocols_item = app_protocols_item_data.value
                app_protocols.append(app_protocols_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if cidrs is not UNSET:
            field_dict["cidrs"] = cidrs
        if domains is not UNSET:
            field_dict["domains"] = domains
        if ports is not UNSET:
            field_dict["ports"] = ports
        if app_protocols is not UNSET:
            field_dict["appProtocols"] = app_protocols

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.port_spec import PortSpec

        d = dict(src_dict)
        action = TrafficRuleAction(d.pop("action"))

        name = d.pop("name", UNSET)

        cidrs = cast(list[str], d.pop("cidrs", UNSET))

        domains = cast(list[str], d.pop("domains", UNSET))

        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in _ports or []:
            ports_item = PortSpec.from_dict(ports_item_data)

            ports.append(ports_item)

        app_protocols = []
        _app_protocols = d.pop("appProtocols", UNSET)
        for app_protocols_item_data in _app_protocols or []:
            app_protocols_item = TrafficRuleAppProtocol(app_protocols_item_data)

            app_protocols.append(app_protocols_item)

        traffic_rule = cls(
            action=action,
            name=name,
            cidrs=cidrs,
            domains=domains,
            ports=ports,
            app_protocols=app_protocols,
        )

        traffic_rule.additional_properties = d
        return traffic_rule

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
