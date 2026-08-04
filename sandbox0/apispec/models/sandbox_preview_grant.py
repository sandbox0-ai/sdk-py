import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sandbox_preview_grant_protocol import SandboxPreviewGrantProtocol

T = TypeVar("T", bound="SandboxPreviewGrant")


@_attrs_define
class SandboxPreviewGrant:
    """
    Attributes:
        id (str):
        sandbox_id (str):
        port (int):
        protocol (SandboxPreviewGrantProtocol):
        url (str): One-time browser bootstrap URL for a newly created grant; a clean target URL for a renewal response.
            The resulting browser cookie is session-scoped while this server-side grant remains authoritative for
            expiration.
        target_url (str): Clean preview origin and path without credentials.
        expires_at (datetime.datetime):
        runtime_generation (int):
    """

    id: str
    sandbox_id: str
    port: int
    protocol: SandboxPreviewGrantProtocol
    url: str
    target_url: str
    expires_at: datetime.datetime
    runtime_generation: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sandbox_id = self.sandbox_id

        port = self.port

        protocol = self.protocol.value

        url = self.url

        target_url = self.target_url

        expires_at = self.expires_at.isoformat()

        runtime_generation = self.runtime_generation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sandbox_id": sandbox_id,
                "port": port,
                "protocol": protocol,
                "url": url,
                "target_url": target_url,
                "expires_at": expires_at,
                "runtime_generation": runtime_generation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sandbox_id = d.pop("sandbox_id")

        port = d.pop("port")

        protocol = SandboxPreviewGrantProtocol(d.pop("protocol"))

        url = d.pop("url")

        target_url = d.pop("target_url")

        expires_at = isoparse(d.pop("expires_at"))

        runtime_generation = d.pop("runtime_generation")

        sandbox_preview_grant = cls(
            id=id,
            sandbox_id=sandbox_id,
            port=port,
            protocol=protocol,
            url=url,
            target_url=target_url,
            expires_at=expires_at,
            runtime_generation=runtime_generation,
        )

        sandbox_preview_grant.additional_properties = d
        return sandbox_preview_grant

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
