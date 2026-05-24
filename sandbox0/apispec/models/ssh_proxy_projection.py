from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="SSHProxyProjection")



@_attrs_define
class SSHProxyProjection:
    """ Transparent SSH proxy projection used for SSH egress re-origination.

        Attributes:
            sandbox_public_keys (Union[Unset, list[str]]): Fake public keys accepted from sandbox-side SSH clients.
            upstream_username (Union[Unset, str]): Username used by netd when authenticating to the upstream SSH server.
            known_hosts (Union[Unset, list[str]]): OpenSSH known_hosts entries used to verify upstream host keys.
     """

    sandbox_public_keys: Union[Unset, list[str]] = UNSET
    upstream_username: Union[Unset, str] = UNSET
    known_hosts: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sandbox_public_keys: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sandbox_public_keys, Unset):
            sandbox_public_keys = self.sandbox_public_keys



        upstream_username = self.upstream_username

        known_hosts: Union[Unset, list[str]] = UNSET
        if not isinstance(self.known_hosts, Unset):
            known_hosts = self.known_hosts




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sandbox_public_keys is not UNSET:
            field_dict["sandboxPublicKeys"] = sandbox_public_keys
        if upstream_username is not UNSET:
            field_dict["upstreamUsername"] = upstream_username
        if known_hosts is not UNSET:
            field_dict["knownHosts"] = known_hosts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_public_keys = cast(list[str], d.pop("sandboxPublicKeys", UNSET))


        upstream_username = d.pop("upstreamUsername", UNSET)

        known_hosts = cast(list[str], d.pop("knownHosts", UNSET))


        ssh_proxy_projection = cls(
            sandbox_public_keys=sandbox_public_keys,
            upstream_username=upstream_username,
            known_hosts=known_hosts,
        )


        ssh_proxy_projection.additional_properties = d
        return ssh_proxy_projection

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
