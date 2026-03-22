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

from ..models.egress_auth_failure_policy import EgressAuthFailurePolicy
from ..models.egress_auth_protocol import EgressAuthProtocol
from ..models.egress_auth_rollout_mode import EgressAuthRolloutMode
from ..models.egress_tls_mode import EgressTLSMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_spec import PortSpec


T = TypeVar("T", bound="EgressCredentialRule")


@_attrs_define
class EgressCredentialRule:
    """
    Attributes:
        credential_ref (str): Stable binding ref to resolve when this traffic rule matches.
            The referenced binding must be present in `network.credentialBindings`.
        name (Union[Unset, str]): Optional stable identifier used for merge and replacement.
        rollout (Union[Unset, EgressAuthRolloutMode]):
        protocol (Union[Unset, EgressAuthProtocol]):
        tls_mode (Union[Unset, EgressTLSMode]):
        failure_policy (Union[Unset, EgressAuthFailurePolicy]):
        domains (Union[Unset, list[str]]): Domain match list for the rule.
        ports (Union[Unset, list['PortSpec']]): Port/protocol constraints for the rule.
    """

    credential_ref: str
    name: Union[Unset, str] = UNSET
    rollout: Union[Unset, EgressAuthRolloutMode] = UNSET
    protocol: Union[Unset, EgressAuthProtocol] = UNSET
    tls_mode: Union[Unset, EgressTLSMode] = UNSET
    failure_policy: Union[Unset, EgressAuthFailurePolicy] = UNSET
    domains: Union[Unset, list[str]] = UNSET
    ports: Union[Unset, list["PortSpec"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credential_ref = self.credential_ref

        name = self.name

        rollout: Union[Unset, str] = UNSET
        if not isinstance(self.rollout, Unset):
            rollout = self.rollout.value

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        tls_mode: Union[Unset, str] = UNSET
        if not isinstance(self.tls_mode, Unset):
            tls_mode = self.tls_mode.value

        failure_policy: Union[Unset, str] = UNSET
        if not isinstance(self.failure_policy, Unset):
            failure_policy = self.failure_policy.value

        domains: Union[Unset, list[str]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentialRef": credential_ref,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if rollout is not UNSET:
            field_dict["rollout"] = rollout
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if tls_mode is not UNSET:
            field_dict["tlsMode"] = tls_mode
        if failure_policy is not UNSET:
            field_dict["failurePolicy"] = failure_policy
        if domains is not UNSET:
            field_dict["domains"] = domains
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.port_spec import PortSpec

        d = dict(src_dict)
        credential_ref = d.pop("credentialRef")

        name = d.pop("name", UNSET)

        _rollout = d.pop("rollout", UNSET)
        rollout: Union[Unset, EgressAuthRolloutMode]
        if isinstance(_rollout, Unset):
            rollout = UNSET
        else:
            rollout = EgressAuthRolloutMode(_rollout)

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, EgressAuthProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = EgressAuthProtocol(_protocol)

        _tls_mode = d.pop("tlsMode", UNSET)
        tls_mode: Union[Unset, EgressTLSMode]
        if isinstance(_tls_mode, Unset):
            tls_mode = UNSET
        else:
            tls_mode = EgressTLSMode(_tls_mode)

        _failure_policy = d.pop("failurePolicy", UNSET)
        failure_policy: Union[Unset, EgressAuthFailurePolicy]
        if isinstance(_failure_policy, Unset):
            failure_policy = UNSET
        else:
            failure_policy = EgressAuthFailurePolicy(_failure_policy)

        domains = cast(list[str], d.pop("domains", UNSET))

        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in _ports or []:
            ports_item = PortSpec.from_dict(ports_item_data)

            ports.append(ports_item)

        egress_credential_rule = cls(
            credential_ref=credential_ref,
            name=name,
            rollout=rollout,
            protocol=protocol,
            tls_mode=tls_mode,
            failure_policy=failure_policy,
            domains=domains,
            ports=ports,
        )

        egress_credential_rule.additional_properties = d
        return egress_credential_rule

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
