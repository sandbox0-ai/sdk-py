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

T = TypeVar("T", bound="Function")


@_attrs_define
class Function:
    """
    Attributes:
        id (str):
        team_id (str):
        name (str):
        slug (str):
        domain_label (str):
        enabled (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        active_revision_id (Union[Unset, str]):
        created_by (Union[Unset, str]):
        deleted_at (Union[Unset, datetime.datetime]): Set when the function has been soft-deleted. Deleted functions are
            hidden from normal list/get APIs and do not serve traffic.
    """

    id: str
    team_id: str
    name: str
    slug: str
    domain_label: str
    enabled: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    active_revision_id: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        name = self.name

        slug = self.slug

        domain_label = self.domain_label

        enabled = self.enabled

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        active_revision_id = self.active_revision_id

        created_by = self.created_by

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "team_id": team_id,
                "name": name,
                "slug": slug,
                "domain_label": domain_label,
                "enabled": enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if active_revision_id is not UNSET:
            field_dict["active_revision_id"] = active_revision_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        name = d.pop("name")

        slug = d.pop("slug")

        domain_label = d.pop("domain_label")

        enabled = d.pop("enabled")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        active_revision_id = d.pop("active_revision_id", UNSET)

        created_by = d.pop("created_by", UNSET)

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        function = cls(
            id=id,
            team_id=team_id,
            name=name,
            slug=slug,
            domain_label=domain_label,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            active_revision_id=active_revision_id,
            created_by=created_by,
            deleted_at=deleted_at,
        )

        function.additional_properties = d
        return function

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
