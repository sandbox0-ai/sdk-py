from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForkSandboxConfig")


@_attrs_define
class ForkSandboxConfig:
    """
    Attributes:
        ttl (Union[Unset, int]): Runtime soft time-to-live in seconds for the forked sandbox. Omit to inherit the source
            setting. Set 0 to disable soft expiration.
        hard_ttl (Union[Unset, int]): Sandbox hard time-to-live in seconds for the forked sandbox. Omit to inherit the
            source setting. Set 0 to disable hard expiration.
    """

    ttl: Union[Unset, int] = UNSET
    hard_ttl: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        ttl = self.ttl

        hard_ttl = self.hard_ttl

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if hard_ttl is not UNSET:
            field_dict["hard_ttl"] = hard_ttl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ttl = d.pop("ttl", UNSET)

        hard_ttl = d.pop("hard_ttl", UNSET)

        fork_sandbox_config = cls(
            ttl=ttl,
            hard_ttl=hard_ttl,
        )

        return fork_sandbox_config
