from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_preview_create_request_protocol import (
    SandboxPreviewCreateRequestProtocol,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxPreviewCreateRequest")


@_attrs_define
class SandboxPreviewCreateRequest:
    """
    Attributes:
        port (int): Loopback TCP port inside the sandbox runtime.
        protocol (Union[Unset, SandboxPreviewCreateRequestProtocol]): Protocol spoken by the loopback server. HTTPS
            permits a self-signed loopback certificate. Default: SandboxPreviewCreateRequestProtocol.HTTP.
        path (Union[Unset, str]): Same-origin absolute path, including an optional query or fragment, opened after
            browser bootstrap. Default: '/'.
        ttl_seconds (Union[Unset, int]):  Default: 900.
    """

    port: int
    protocol: Union[Unset, SandboxPreviewCreateRequestProtocol] = (
        SandboxPreviewCreateRequestProtocol.HTTP
    )
    path: Union[Unset, str] = "/"
    ttl_seconds: Union[Unset, int] = 900
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        path = self.path

        ttl_seconds = self.ttl_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if path is not UNSET:
            field_dict["path"] = path
        if ttl_seconds is not UNSET:
            field_dict["ttl_seconds"] = ttl_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        port = d.pop("port")

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, SandboxPreviewCreateRequestProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = SandboxPreviewCreateRequestProtocol(_protocol)

        path = d.pop("path", UNSET)

        ttl_seconds = d.pop("ttl_seconds", UNSET)

        sandbox_preview_create_request = cls(
            port=port,
            protocol=protocol,
            path=path,
            ttl_seconds=ttl_seconds,
        )

        sandbox_preview_create_request.additional_properties = d
        return sandbox_preview_create_request

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
