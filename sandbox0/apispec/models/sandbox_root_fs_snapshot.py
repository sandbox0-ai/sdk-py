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

T = TypeVar("T", bound="SandboxRootFSSnapshot")


@_attrs_define
class SandboxRootFSSnapshot:
    """
    Attributes:
        id (str):
        sandbox_id (str):
        created_at (datetime.datetime):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        expires_at (Union[Unset, datetime.datetime]): Optional snapshot expiration timestamp. Zero value means not set.
    """

    id: str
    sandbox_id: str
    created_at: datetime.datetime
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sandbox_id = self.sandbox_id

        created_at = self.created_at.isoformat()

        name = self.name

        description = self.description

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sandbox_id": sandbox_id,
                "created_at": created_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sandbox_id = d.pop("sandbox_id")

        created_at = isoparse(d.pop("created_at"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        sandbox_root_fs_snapshot = cls(
            id=id,
            sandbox_id=sandbox_id,
            created_at=created_at,
            name=name,
            description=description,
            expires_at=expires_at,
        )

        sandbox_root_fs_snapshot.additional_properties = d
        return sandbox_root_fs_snapshot

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
