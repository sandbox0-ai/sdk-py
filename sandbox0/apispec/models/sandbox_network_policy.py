from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sandbox_network_policy_mode import SandboxNetworkPolicyMode
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.credential_binding import CredentialBinding
  from ..models.network_egress_policy import NetworkEgressPolicy





T = TypeVar("T", bound="SandboxNetworkPolicy")



@_attrs_define
class SandboxNetworkPolicy:
    """ 
        Attributes:
            mode (SandboxNetworkPolicyMode):
            egress (Union[Unset, NetworkEgressPolicy]): Egress rule set interpreted by the selected network mode.
                In `allow-all`, only `denied*` fields are enforced.
                In `block-all`, only `allowed*` fields are enforced.
                `trafficRules` is a rule-based alternative and must not be combined
                with the legacy `allowed*`/`denied*` fields.
            credential_bindings (Union[Unset, list['CredentialBinding']]):
     """

    mode: SandboxNetworkPolicyMode
    egress: Union[Unset, 'NetworkEgressPolicy'] = UNSET
    credential_bindings: Union[Unset, list['CredentialBinding']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_binding import CredentialBinding
        from ..models.network_egress_policy import NetworkEgressPolicy
        mode = self.mode.value

        egress: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.egress, Unset):
            egress = self.egress.to_dict()

        credential_bindings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.credential_bindings, Unset):
            credential_bindings = []
            for credential_bindings_item_data in self.credential_bindings:
                credential_bindings_item = credential_bindings_item_data.to_dict()
                credential_bindings.append(credential_bindings_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mode": mode,
        })
        if egress is not UNSET:
            field_dict["egress"] = egress
        if credential_bindings is not UNSET:
            field_dict["credentialBindings"] = credential_bindings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_binding import CredentialBinding
        from ..models.network_egress_policy import NetworkEgressPolicy
        d = dict(src_dict)
        mode = SandboxNetworkPolicyMode(d.pop("mode"))




        _egress = d.pop("egress", UNSET)
        egress: Union[Unset, NetworkEgressPolicy]
        if isinstance(_egress,  Unset):
            egress = UNSET
        else:
            egress = NetworkEgressPolicy.from_dict(_egress)




        credential_bindings = []
        _credential_bindings = d.pop("credentialBindings", UNSET)
        for credential_bindings_item_data in (_credential_bindings or []):
            credential_bindings_item = CredentialBinding.from_dict(credential_bindings_item_data)



            credential_bindings.append(credential_bindings_item)


        sandbox_network_policy = cls(
            mode=mode,
            egress=egress,
            credential_bindings=credential_bindings,
        )


        sandbox_network_policy.additional_properties = d
        return sandbox_network_policy

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
