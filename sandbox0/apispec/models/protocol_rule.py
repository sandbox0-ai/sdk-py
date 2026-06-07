from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.egress_tls_mode import EgressTLSMode
from ..models.protocol_rule_protocol import ProtocolRuleProtocol
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.mcp_protocol_rule import MCPProtocolRule
  from ..models.http_match import HTTPMatch
  from ..models.port_spec import PortSpec





T = TypeVar("T", bound="ProtocolRule")



@_attrs_define
class ProtocolRule:
    """ Protocol-aware egress controls applied after destination traffic is allowed.

        Attributes:
            protocol (ProtocolRuleProtocol):
            name (Union[Unset, str]): Optional stable identifier used for merge and replacement.
            domains (Union[Unset, list[str]]): Domain match list for the rule.
            ports (Union[Unset, list['PortSpec']]): Port/protocol constraints for the rule.
            tls_mode (Union[Unset, EgressTLSMode]):
            http_match (Union[Unset, HTTPMatch]): Request-level matcher for HTTP-family egress credential rules.
            mcp (Union[Unset, MCPProtocolRule]): Model Context Protocol operation policy.
     """

    protocol: ProtocolRuleProtocol
    name: Union[Unset, str] = UNSET
    domains: Union[Unset, list[str]] = UNSET
    ports: Union[Unset, list['PortSpec']] = UNSET
    tls_mode: Union[Unset, EgressTLSMode] = UNSET
    http_match: Union[Unset, 'HTTPMatch'] = UNSET
    mcp: Union[Unset, 'MCPProtocolRule'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_protocol_rule import MCPProtocolRule
        from ..models.http_match import HTTPMatch
        from ..models.port_spec import PortSpec
        protocol = self.protocol.value

        name = self.name

        domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains



        ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)



        tls_mode: Union[Unset, str] = UNSET
        if not isinstance(self.tls_mode, Unset):
            tls_mode = self.tls_mode.value


        http_match: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http_match, Unset):
            http_match = self.http_match.to_dict()

        mcp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mcp, Unset):
            mcp = self.mcp.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "protocol": protocol,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if domains is not UNSET:
            field_dict["domains"] = domains
        if ports is not UNSET:
            field_dict["ports"] = ports
        if tls_mode is not UNSET:
            field_dict["tlsMode"] = tls_mode
        if http_match is not UNSET:
            field_dict["httpMatch"] = http_match
        if mcp is not UNSET:
            field_dict["mcp"] = mcp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_protocol_rule import MCPProtocolRule
        from ..models.http_match import HTTPMatch
        from ..models.port_spec import PortSpec
        d = dict(src_dict)
        protocol = ProtocolRuleProtocol(d.pop("protocol"))




        name = d.pop("name", UNSET)

        domains = cast(list[str], d.pop("domains", UNSET))


        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in (_ports or []):
            ports_item = PortSpec.from_dict(ports_item_data)



            ports.append(ports_item)


        _tls_mode = d.pop("tlsMode", UNSET)
        tls_mode: Union[Unset, EgressTLSMode]
        if isinstance(_tls_mode,  Unset):
            tls_mode = UNSET
        else:
            tls_mode = EgressTLSMode(_tls_mode)




        _http_match = d.pop("httpMatch", UNSET)
        http_match: Union[Unset, HTTPMatch]
        if isinstance(_http_match,  Unset):
            http_match = UNSET
        else:
            http_match = HTTPMatch.from_dict(_http_match)




        _mcp = d.pop("mcp", UNSET)
        mcp: Union[Unset, MCPProtocolRule]
        if isinstance(_mcp,  Unset):
            mcp = UNSET
        else:
            mcp = MCPProtocolRule.from_dict(_mcp)




        protocol_rule = cls(
            protocol=protocol,
            name=name,
            domains=domains,
            ports=ports,
            tls_mode=tls_mode,
            http_match=http_match,
            mcp=mcp,
        )


        protocol_rule.additional_properties = d
        return protocol_rule

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
