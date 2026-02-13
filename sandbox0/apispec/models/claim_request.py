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
    from ..models.sandbox_config import SandboxConfig


T = TypeVar("T", bound="ClaimRequest")


@_attrs_define
class ClaimRequest:
    """
    Attributes:
        template (Union[Unset, str]):
        config (Union[Unset, SandboxConfig]):
    """

    template: Union[Unset, str] = UNSET
    config: Union[Unset, "SandboxConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template = self.template

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template is not UNSET:
            field_dict["template"] = template
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_config import SandboxConfig

        d = dict(src_dict)
        template = d.pop("template", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, SandboxConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = SandboxConfig.from_dict(_config)

        claim_request = cls(
            template=template,
            config=config,
        )

        claim_request.additional_properties = d
        return claim_request

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
