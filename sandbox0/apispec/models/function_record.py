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

T = TypeVar("T", bound="FunctionRecord")


@_attrs_define
class FunctionRecord:
    """
    Attributes:
        id (str):
        team_id (str):
        name (str):
        slug (str):
        domain_label (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        host (str):
        url (str):
        active_revision_id (Union[Unset, str]):
        created_by (Union[Unset, str]):
    """

    id: str
    team_id: str
    name: str
    slug: str
    domain_label: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    host: str
    url: str
    active_revision_id: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        name = self.name

        slug = self.slug

        domain_label = self.domain_label

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        host = self.host

        url = self.url

        active_revision_id = self.active_revision_id

        created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "team_id": team_id,
                "name": name,
                "slug": slug,
                "domain_label": domain_label,
                "created_at": created_at,
                "updated_at": updated_at,
                "host": host,
                "url": url,
            }
        )
        if active_revision_id is not UNSET:
            field_dict["active_revision_id"] = active_revision_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        name = d.pop("name")

        slug = d.pop("slug")

        domain_label = d.pop("domain_label")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        host = d.pop("host")

        url = d.pop("url")

        active_revision_id = d.pop("active_revision_id", UNSET)

        created_by = d.pop("created_by", UNSET)

        function_record = cls(
            id=id,
            team_id=team_id,
            name=name,
            slug=slug,
            domain_label=domain_label,
            created_at=created_at,
            updated_at=updated_at,
            host=host,
            url=url,
            active_revision_id=active_revision_id,
            created_by=created_by,
        )

        function_record.additional_properties = d
        return function_record

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
