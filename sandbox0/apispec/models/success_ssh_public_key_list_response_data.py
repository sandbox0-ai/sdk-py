from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssh_public_key import SSHPublicKey


T = TypeVar("T", bound="SuccessSSHPublicKeyListResponseData")


@_attrs_define
class SuccessSSHPublicKeyListResponseData:
    """
    Attributes:
        ssh_keys (Union[Unset, list['SSHPublicKey']]):
    """

    ssh_keys: Union[Unset, list["SSHPublicKey"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssh_keys: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = []
            for ssh_keys_item_data in self.ssh_keys:
                ssh_keys_item = ssh_keys_item_data.to_dict()
                ssh_keys.append(ssh_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ssh_public_key import SSHPublicKey

        d = dict(src_dict)
        ssh_keys = []
        _ssh_keys = d.pop("ssh_keys", UNSET)
        for ssh_keys_item_data in _ssh_keys or []:
            ssh_keys_item = SSHPublicKey.from_dict(ssh_keys_item_data)

            ssh_keys.append(ssh_keys_item)

        success_ssh_public_key_list_response_data = cls(
            ssh_keys=ssh_keys,
        )

        success_ssh_public_key_list_response_data.additional_properties = d
        return success_ssh_public_key_list_response_data

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
