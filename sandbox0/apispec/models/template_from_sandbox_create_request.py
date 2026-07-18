from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_from_sandbox_spec_overrides import (
        TemplateFromSandboxSpecOverrides,
    )


T = TypeVar("T", bound="TemplateFromSandboxCreateRequest")


@_attrs_define
class TemplateFromSandboxCreateRequest:
    """Creates a template by capturing the current root filesystem of an existing sandbox.

    Attributes:
        template_id (str):
        sandbox_id (str):
        spec_overrides (Union[Unset, TemplateFromSandboxSpecOverrides]): Safe template fields that may override values
            inherited from the source
            sandbox's originating template. Pool defaults to zero idle sandboxes
            when omitted.
    """

    template_id: str
    sandbox_id: str
    spec_overrides: Union[Unset, "TemplateFromSandboxSpecOverrides"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        sandbox_id = self.sandbox_id

        spec_overrides: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spec_overrides, Unset):
            spec_overrides = self.spec_overrides.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "template_id": template_id,
                "sandbox_id": sandbox_id,
            }
        )
        if spec_overrides is not UNSET:
            field_dict["spec_overrides"] = spec_overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_from_sandbox_spec_overrides import (
            TemplateFromSandboxSpecOverrides,
        )

        d = dict(src_dict)
        template_id = d.pop("template_id")

        sandbox_id = d.pop("sandbox_id")

        _spec_overrides = d.pop("spec_overrides", UNSET)
        spec_overrides: Union[Unset, TemplateFromSandboxSpecOverrides]
        if isinstance(_spec_overrides, Unset):
            spec_overrides = UNSET
        else:
            spec_overrides = TemplateFromSandboxSpecOverrides.from_dict(_spec_overrides)

        template_from_sandbox_create_request = cls(
            template_id=template_id,
            sandbox_id=sandbox_id,
            spec_overrides=spec_overrides,
        )

        return template_from_sandbox_create_request
