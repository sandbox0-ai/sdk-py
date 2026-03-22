from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticTLSClientCertificateSourceSpec")


@_attrs_define
class StaticTLSClientCertificateSourceSpec:
    """
    Attributes:
        certificate_pem (str):
        private_key_pem (str):
        ca_pem (Union[Unset, str]):
    """

    certificate_pem: str
    private_key_pem: str
    ca_pem: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate_pem = self.certificate_pem

        private_key_pem = self.private_key_pem

        ca_pem = self.ca_pem

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certificatePem": certificate_pem,
                "privateKeyPem": private_key_pem,
            }
        )
        if ca_pem is not UNSET:
            field_dict["caPem"] = ca_pem

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate_pem = d.pop("certificatePem")

        private_key_pem = d.pop("privateKeyPem")

        ca_pem = d.pop("caPem", UNSET)

        static_tls_client_certificate_source_spec = cls(
            certificate_pem=certificate_pem,
            private_key_pem=private_key_pem,
            ca_pem=ca_pem,
        )

        static_tls_client_certificate_source_spec.additional_properties = d
        return static_tls_client_certificate_source_spec

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
