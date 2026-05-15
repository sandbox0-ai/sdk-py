from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="StaticSSHPrivateKeySourceSpec")



@_attrs_define
class StaticSSHPrivateKeySourceSpec:
    """ 
        Attributes:
            private_key_pem (str):
            passphrase (Union[Unset, str]):
     """

    private_key_pem: str
    passphrase: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        private_key_pem = self.private_key_pem

        passphrase = self.passphrase


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "privateKeyPem": private_key_pem,
        })
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private_key_pem = d.pop("privateKeyPem")

        passphrase = d.pop("passphrase", UNSET)

        static_ssh_private_key_source_spec = cls(
            private_key_pem=private_key_pem,
            passphrase=passphrase,
        )


        static_ssh_private_key_source_spec.additional_properties = d
        return static_ssh_private_key_source_spec

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
