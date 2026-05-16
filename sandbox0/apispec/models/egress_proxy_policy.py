from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.egress_proxy_type import EgressProxyType
from ..types import UNSET, Unset


T = TypeVar("T", bound="EgressProxyPolicy")


@_attrs_define
class EgressProxyPolicy:
    """Customer-managed transparent egress proxy for allowed TCP traffic.

    Attributes:
        type_ (EgressProxyType):
        address (str): SOCKS5 proxy endpoint in host:port form. Example: proxy.example.com:1080.
        credential_ref (Union[Unset, str]): Optional credential binding ref using a username_password projection.
    """

    type_: EgressProxyType
    address: str
    credential_ref: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        address = self.address

        credential_ref = self.credential_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "address": address,
            }
        )
        if credential_ref is not UNSET:
            field_dict["credentialRef"] = credential_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = EgressProxyType(d.pop("type"))

        address = d.pop("address")

        credential_ref = d.pop("credentialRef", UNSET)

        egress_proxy_policy = cls(
            type_=type_,
            address=address,
            credential_ref=credential_ref,
        )

        egress_proxy_policy.additional_properties = d
        return egress_proxy_policy

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
