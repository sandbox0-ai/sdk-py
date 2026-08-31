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
    from ..models.template_creation_status import TemplateCreationStatus


T = TypeVar("T", bound="SandboxTemplateStatus")


@_attrs_define
class SandboxTemplateStatus:
    """
    Attributes:
        creation (Union[Unset, TemplateCreationStatus]): Asynchronous creation status for templates built from a
            sandbox.
            Traditional image-based templates omit this object and are ready
            immediately after creation. Ready means the regional template source
            has been committed and the claim API may consume it.
    """

    creation: Union[Unset, "TemplateCreationStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.creation, Unset):
            creation = self.creation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creation is not UNSET:
            field_dict["creation"] = creation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_creation_status import TemplateCreationStatus

        d = dict(src_dict)
        _creation = d.pop("creation", UNSET)
        creation: Union[Unset, TemplateCreationStatus]
        if isinstance(_creation, Unset):
            creation = UNSET
        else:
            creation = TemplateCreationStatus.from_dict(_creation)

        sandbox_template_status = cls(
            creation=creation,
        )

        sandbox_template_status.additional_properties = d
        return sandbox_template_status

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
