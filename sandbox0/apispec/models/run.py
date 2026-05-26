from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.run_scale_policy import RunScalePolicy





T = TypeVar("T", bound="Run")



@_attrs_define
class Run:
    """ 
        Attributes:
            id (str):
            team_id (str):
            name (str):
            slug (str):
            domain_label (str):
            enabled (bool):
            scale (RunScalePolicy): Scale-to-zero policy. Runs do not have a minimum idle instance count.
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            created_by (Union[Unset, str]):
            url (Union[Unset, str]):
            active_revision_id (Union[Unset, str]):
     """

    id: str
    team_id: str
    name: str
    slug: str
    domain_label: str
    enabled: bool
    scale: 'RunScalePolicy'
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    active_revision_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_scale_policy import RunScalePolicy
        id = self.id

        team_id = self.team_id

        name = self.name

        slug = self.slug

        domain_label = self.domain_label

        enabled = self.enabled

        scale = self.scale.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by = self.created_by

        url = self.url

        active_revision_id = self.active_revision_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "team_id": team_id,
            "name": name,
            "slug": slug,
            "domain_label": domain_label,
            "enabled": enabled,
            "scale": scale,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if url is not UNSET:
            field_dict["url"] = url
        if active_revision_id is not UNSET:
            field_dict["active_revision_id"] = active_revision_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_scale_policy import RunScalePolicy
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("team_id")

        name = d.pop("name")

        slug = d.pop("slug")

        domain_label = d.pop("domain_label")

        enabled = d.pop("enabled")

        scale = RunScalePolicy.from_dict(d.pop("scale"))




        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        created_by = d.pop("created_by", UNSET)

        url = d.pop("url", UNSET)

        active_revision_id = d.pop("active_revision_id", UNSET)

        run = cls(
            id=id,
            team_id=team_id,
            name=name,
            slug=slug,
            domain_label=domain_label,
            enabled=enabled,
            scale=scale,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            url=url,
            active_revision_id=active_revision_id,
        )


        run.additional_properties = d
        return run

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
