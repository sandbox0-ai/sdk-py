from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_projection_type import CredentialProjectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_headers_projection import HTTPHeadersProjection
    from ..models.tls_client_certificate_projection import (
        TLSClientCertificateProjection,
    )
    from ..models.username_password_projection import UsernamePasswordProjection


T = TypeVar("T", bound="ProjectionSpec")


@_attrs_define
class ProjectionSpec:
    """
    Attributes:
        type_ (CredentialProjectionType):
        http_headers (Union[Unset, HTTPHeadersProjection]):
        tls_client_certificate (Union[Unset, TLSClientCertificateProjection]): Client certificate projection used for
            TLS terminate-reoriginate auth.
        username_password (Union[Unset, UsernamePasswordProjection]): Username/password projection used for SOCKS5 and
            MQTT auth handshakes.
    """

    type_: CredentialProjectionType
    http_headers: Union[Unset, "HTTPHeadersProjection"] = UNSET
    tls_client_certificate: Union[Unset, "TLSClientCertificateProjection"] = UNSET
    username_password: Union[Unset, "UsernamePasswordProjection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        http_headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http_headers, Unset):
            http_headers = self.http_headers.to_dict()

        tls_client_certificate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tls_client_certificate, Unset):
            tls_client_certificate = self.tls_client_certificate.to_dict()

        username_password: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.username_password, Unset):
            username_password = self.username_password.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if http_headers is not UNSET:
            field_dict["httpHeaders"] = http_headers
        if tls_client_certificate is not UNSET:
            field_dict["tlsClientCertificate"] = tls_client_certificate
        if username_password is not UNSET:
            field_dict["usernamePassword"] = username_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_headers_projection import HTTPHeadersProjection
        from ..models.tls_client_certificate_projection import (
            TLSClientCertificateProjection,
        )
        from ..models.username_password_projection import UsernamePasswordProjection

        d = dict(src_dict)
        type_ = CredentialProjectionType(d.pop("type"))

        _http_headers = d.pop("httpHeaders", UNSET)
        http_headers: Union[Unset, HTTPHeadersProjection]
        if isinstance(_http_headers, Unset):
            http_headers = UNSET
        else:
            http_headers = HTTPHeadersProjection.from_dict(_http_headers)

        _tls_client_certificate = d.pop("tlsClientCertificate", UNSET)
        tls_client_certificate: Union[Unset, TLSClientCertificateProjection]
        if isinstance(_tls_client_certificate, Unset):
            tls_client_certificate = UNSET
        else:
            tls_client_certificate = TLSClientCertificateProjection.from_dict(
                _tls_client_certificate
            )

        _username_password = d.pop("usernamePassword", UNSET)
        username_password: Union[Unset, UsernamePasswordProjection]
        if isinstance(_username_password, Unset):
            username_password = UNSET
        else:
            username_password = UsernamePasswordProjection.from_dict(_username_password)

        projection_spec = cls(
            type_=type_,
            http_headers=http_headers,
            tls_client_certificate=tls_client_certificate,
            username_password=username_password,
        )

        projection_spec.additional_properties = d
        return projection_spec

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
