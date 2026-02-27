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
    from ..models.sandbox_update_config import SandboxUpdateConfig


T = TypeVar("T", bound="SandboxUpdateRequest")


@_attrs_define
class SandboxUpdateRequest:
    """
    Attributes:
        config (Union[Unset, SandboxUpdateConfig]): Subset of SandboxConfig fields that can be updated at runtime
            without restarting the sandbox.
            Note: env_vars and webhook are not included as they only affect new processes or require restart.
    """

    config: Union[Unset, "SandboxUpdateConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_update_config import SandboxUpdateConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: Union[Unset, SandboxUpdateConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = SandboxUpdateConfig.from_dict(_config)

        sandbox_update_request = cls(
            config=config,
        )

        sandbox_update_request.additional_properties = d
        return sandbox_update_request

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
