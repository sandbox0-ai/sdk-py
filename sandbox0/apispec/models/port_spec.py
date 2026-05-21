from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortSpec")


@_attrs_define
class PortSpec:
    """
    Attributes:
        port (int):
        protocol (Union[Unset, str]):
        end_port (Union[Unset, int]):
    """

    port: int
    protocol: Union[Unset, str] = UNSET
    end_port: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        protocol = self.protocol

        end_port = self.end_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if end_port is not UNSET:
            field_dict["endPort"] = end_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        port = d.pop("port")

        protocol = d.pop("protocol", UNSET)

        end_port = d.pop("endPort", UNSET)

        port_spec = cls(
            port=port,
            protocol=protocol,
            end_port=end_port,
        )

        port_spec.additional_properties = d
        return port_spec

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
