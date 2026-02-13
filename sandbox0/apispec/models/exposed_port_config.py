from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExposedPortConfig")


@_attrs_define
class ExposedPortConfig:
    """
    Attributes:
        port (int):
        resume (bool): Port-level resume gate for public exposure traffic. Evaluated only when
            sandbox auto_resume is true. Priority: sandbox auto_resume (global gate)
            > exposed_ports[].resume (per-port gate).
        public_url (Union[Unset, str]): The full public URL to access this exposed port.
            Format: https://<sandboxName>--p<port>.<regionID>.<rootDomain>
    """

    port: int
    resume: bool
    public_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        resume = self.resume

        public_url = self.public_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
                "resume": resume,
            }
        )
        if public_url is not UNSET:
            field_dict["public_url"] = public_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        port = d.pop("port")

        resume = d.pop("resume")

        public_url = d.pop("public_url", UNSET)

        exposed_port_config = cls(
            port=port,
            resume=resume,
            public_url=public_url,
        )

        exposed_port_config.additional_properties = d
        return exposed_port_config

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
