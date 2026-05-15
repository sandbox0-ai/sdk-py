import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSHPublicKey")


@_attrs_define
class SSHPublicKey:
    """
    Attributes:
        id (str):
        name (str):
        public_key (str):
        key_type (str):
        fingerprint_sha256 (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        comment (Union[Unset, str]):
    """

    id: str
    name: str
    public_key: str
    key_type: str
    fingerprint_sha256: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    comment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        public_key = self.public_key

        key_type = self.key_type

        fingerprint_sha256 = self.fingerprint_sha256

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "public_key": public_key,
                "key_type": key_type,
                "fingerprint_sha256": fingerprint_sha256,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        public_key = d.pop("public_key")

        key_type = d.pop("key_type")

        fingerprint_sha256 = d.pop("fingerprint_sha256")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        comment = d.pop("comment", UNSET)

        ssh_public_key = cls(
            id=id,
            name=name,
            public_key=public_key,
            key_type=key_type,
            fingerprint_sha256=fingerprint_sha256,
            created_at=created_at,
            updated_at=updated_at,
            comment=comment,
        )

        ssh_public_key.additional_properties = d
        return ssh_public_key

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
