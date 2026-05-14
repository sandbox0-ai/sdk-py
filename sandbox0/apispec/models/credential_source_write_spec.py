from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.static_ssh_private_key_source_spec import StaticSSHPrivateKeySourceSpec
  from ..models.static_tls_client_certificate_source_spec import StaticTLSClientCertificateSourceSpec
  from ..models.static_headers_source_spec import StaticHeadersSourceSpec
  from ..models.static_username_password_source_spec import StaticUsernamePasswordSourceSpec





T = TypeVar("T", bound="CredentialSourceWriteSpec")



@_attrs_define
class CredentialSourceWriteSpec:
    """ 
        Attributes:
            static_headers (Union[Unset, StaticHeadersSourceSpec]):
            static_tls_client_certificate (Union[Unset, StaticTLSClientCertificateSourceSpec]):
            static_username_password (Union[Unset, StaticUsernamePasswordSourceSpec]):
            static_ssh_private_key (Union[Unset, StaticSSHPrivateKeySourceSpec]):
     """

    static_headers: Union[Unset, 'StaticHeadersSourceSpec'] = UNSET
    static_tls_client_certificate: Union[Unset, 'StaticTLSClientCertificateSourceSpec'] = UNSET
    static_username_password: Union[Unset, 'StaticUsernamePasswordSourceSpec'] = UNSET
    static_ssh_private_key: Union[Unset, 'StaticSSHPrivateKeySourceSpec'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.static_ssh_private_key_source_spec import StaticSSHPrivateKeySourceSpec
        from ..models.static_tls_client_certificate_source_spec import StaticTLSClientCertificateSourceSpec
        from ..models.static_headers_source_spec import StaticHeadersSourceSpec
        from ..models.static_username_password_source_spec import StaticUsernamePasswordSourceSpec
        static_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static_headers, Unset):
            static_headers = self.static_headers.to_dict()

        static_tls_client_certificate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static_tls_client_certificate, Unset):
            static_tls_client_certificate = self.static_tls_client_certificate.to_dict()

        static_username_password: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static_username_password, Unset):
            static_username_password = self.static_username_password.to_dict()

        static_ssh_private_key: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static_ssh_private_key, Unset):
            static_ssh_private_key = self.static_ssh_private_key.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if static_headers is not UNSET:
            field_dict["staticHeaders"] = static_headers
        if static_tls_client_certificate is not UNSET:
            field_dict["staticTLSClientCertificate"] = static_tls_client_certificate
        if static_username_password is not UNSET:
            field_dict["staticUsernamePassword"] = static_username_password
        if static_ssh_private_key is not UNSET:
            field_dict["staticSSHPrivateKey"] = static_ssh_private_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.static_ssh_private_key_source_spec import StaticSSHPrivateKeySourceSpec
        from ..models.static_tls_client_certificate_source_spec import StaticTLSClientCertificateSourceSpec
        from ..models.static_headers_source_spec import StaticHeadersSourceSpec
        from ..models.static_username_password_source_spec import StaticUsernamePasswordSourceSpec
        d = dict(src_dict)
        _static_headers = d.pop("staticHeaders", UNSET)
        static_headers: Union[Unset, StaticHeadersSourceSpec]
        if isinstance(_static_headers,  Unset):
            static_headers = UNSET
        else:
            static_headers = StaticHeadersSourceSpec.from_dict(_static_headers)




        _static_tls_client_certificate = d.pop("staticTLSClientCertificate", UNSET)
        static_tls_client_certificate: Union[Unset, StaticTLSClientCertificateSourceSpec]
        if isinstance(_static_tls_client_certificate,  Unset):
            static_tls_client_certificate = UNSET
        else:
            static_tls_client_certificate = StaticTLSClientCertificateSourceSpec.from_dict(_static_tls_client_certificate)




        _static_username_password = d.pop("staticUsernamePassword", UNSET)
        static_username_password: Union[Unset, StaticUsernamePasswordSourceSpec]
        if isinstance(_static_username_password,  Unset):
            static_username_password = UNSET
        else:
            static_username_password = StaticUsernamePasswordSourceSpec.from_dict(_static_username_password)




        _static_ssh_private_key = d.pop("staticSSHPrivateKey", UNSET)
        static_ssh_private_key: Union[Unset, StaticSSHPrivateKeySourceSpec]
        if isinstance(_static_ssh_private_key,  Unset):
            static_ssh_private_key = UNSET
        else:
            static_ssh_private_key = StaticSSHPrivateKeySourceSpec.from_dict(_static_ssh_private_key)




        credential_source_write_spec = cls(
            static_headers=static_headers,
            static_tls_client_certificate=static_tls_client_certificate,
            static_username_password=static_username_password,
            static_ssh_private_key=static_ssh_private_key,
        )


        credential_source_write_spec.additional_properties = d
        return credential_source_write_spec

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
