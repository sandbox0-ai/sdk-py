from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tpl_sandbox_network_policy_mode import TplSandboxNetworkPolicyMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_egress_policy import NetworkEgressPolicy


T = TypeVar("T", bound="TplSandboxNetworkPolicy")


@_attrs_define
class TplSandboxNetworkPolicy:
    """
    Attributes:
        mode (TplSandboxNetworkPolicyMode):
        egress (Union[Unset, NetworkEgressPolicy]):
    """

    mode: TplSandboxNetworkPolicyMode
    egress: Union[Unset, "NetworkEgressPolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        egress: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.egress, Unset):
            egress = self.egress.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if egress is not UNSET:
            field_dict["egress"] = egress

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_egress_policy import NetworkEgressPolicy

        d = dict(src_dict)
        mode = TplSandboxNetworkPolicyMode(d.pop("mode"))

        _egress = d.pop("egress", UNSET)
        egress: Union[Unset, NetworkEgressPolicy]
        if isinstance(_egress, Unset):
            egress = UNSET
        else:
            egress = NetworkEgressPolicy.from_dict(_egress)

        tpl_sandbox_network_policy = cls(
            mode=mode,
            egress=egress,
        )

        tpl_sandbox_network_policy.additional_properties = d
        return tpl_sandbox_network_policy

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
