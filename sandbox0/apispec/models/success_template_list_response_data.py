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
    from ..models.template import Template


T = TypeVar("T", bound="SuccessTemplateListResponseData")


@_attrs_define
class SuccessTemplateListResponseData:
    """
    Attributes:
        templates (Union[Unset, list['Template']]):
        count (Union[Unset, int]):
    """

    templates: Union[Unset, list["Template"]] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()
                templates.append(templates_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if templates is not UNSET:
            field_dict["templates"] = templates
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template import Template

        d = dict(src_dict)
        templates = []
        _templates = d.pop("templates", UNSET)
        for templates_item_data in _templates or []:
            templates_item = Template.from_dict(templates_item_data)

            templates.append(templates_item)

        count = d.pop("count", UNSET)

        success_template_list_response_data = cls(
            templates=templates,
            count=count,
        )

        success_template_list_response_data.additional_properties = d
        return success_template_list_response_data

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
