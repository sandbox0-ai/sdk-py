from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sandbox_template_spec import SandboxTemplateSpec


T = TypeVar("T", bound="TemplateCreateRequest")


@_attrs_define
class TemplateCreateRequest:
    """
    Attributes:
        template_id (str):
        spec (SandboxTemplateSpec):
    """

    template_id: str
    spec: "SandboxTemplateSpec"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_id": template_id,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_template_spec import SandboxTemplateSpec

        d = dict(src_dict)
        template_id = d.pop("template_id")

        spec = SandboxTemplateSpec.from_dict(d.pop("spec"))

        template_create_request = cls(
            template_id=template_id,
            spec=spec,
        )

        template_create_request.additional_properties = d
        return template_create_request

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
