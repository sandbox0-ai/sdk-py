from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Snapshot")


@_attrs_define
class Snapshot:
    """
    Attributes:
        id (str):
        volume_id (str):
        name (str):
        size_bytes (int):
        created_at (str):
        description (Union[Unset, str]):
        expires_at (Union[None, Unset, str]):
    """

    id: str
    volume_id: str
    name: str
    size_bytes: int
    created_at: str
    description: Union[Unset, str] = UNSET
    expires_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        volume_id = self.volume_id

        name = self.name

        size_bytes = self.size_bytes

        created_at = self.created_at

        description = self.description

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "volume_id": volume_id,
                "name": name,
                "size_bytes": size_bytes,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        volume_id = d.pop("volume_id")

        name = d.pop("name")

        size_bytes = d.pop("size_bytes")

        created_at = d.pop("created_at")

        description = d.pop("description", UNSET)

        def _parse_expires_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        snapshot = cls(
            id=id,
            volume_id=volume_id,
            name=name,
            size_bytes=size_bytes,
            created_at=created_at,
            description=description,
            expires_at=expires_at,
        )

        snapshot.additional_properties = d
        return snapshot

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
