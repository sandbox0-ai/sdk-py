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
    from ..models.fork_sandbox_config import ForkSandboxConfig


T = TypeVar("T", bound="ForkSandboxRequest")


@_attrs_define
class ForkSandboxRequest:
    """Optional fork overrides. Omit config to inherit the source sandbox configuration.
    The source sandbox may be running or paused; running sources are checkpointed
    before the paused child sandbox is created.

        Attributes:
            config (Union[Unset, ForkSandboxConfig]):
    """

    config: Union[Unset, "ForkSandboxConfig"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fork_sandbox_config import ForkSandboxConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: Union[Unset, ForkSandboxConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ForkSandboxConfig.from_dict(_config)

        fork_sandbox_request = cls(
            config=config,
        )

        return fork_sandbox_request
