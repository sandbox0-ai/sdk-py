import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_template_spec import SandboxTemplateSpec


T = TypeVar("T", bound="Template")


@_attrs_define
class Template:
    """
    Attributes:
        template_id (str):
        scope (str):
        spec (SandboxTemplateSpec):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        team_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
    """

    template_id: str
    scope: str
    spec: "SandboxTemplateSpec"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    team_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        scope = self.scope

        spec = self.spec.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        team_id = self.team_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_id": template_id,
                "scope": scope,
                "spec": spec,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_template_spec import SandboxTemplateSpec

        d = dict(src_dict)
        template_id = d.pop("template_id")

        scope = d.pop("scope")

        spec = SandboxTemplateSpec.from_dict(d.pop("spec"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        team_id = d.pop("team_id", UNSET)

        user_id = d.pop("user_id", UNSET)

        template = cls(
            template_id=template_id,
            scope=scope,
            spec=spec,
            created_at=created_at,
            updated_at=updated_at,
            team_id=team_id,
            user_id=user_id,
        )

        template.additional_properties = d
        return template

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
