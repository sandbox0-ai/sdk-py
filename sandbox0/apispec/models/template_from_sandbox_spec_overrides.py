from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateFromSandboxSpecOverrides")


@_attrs_define
class TemplateFromSandboxSpecOverrides:
    """Safe template fields that may override values inherited from the source sandbox's originating template.

    Attributes:
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
    """

    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        template_from_sandbox_spec_overrides = cls(
            description=description,
            display_name=display_name,
            tags=tags,
        )

        return template_from_sandbox_spec_overrides
