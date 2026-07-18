from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pool_strategy import PoolStrategy


T = TypeVar("T", bound="TemplateFromSandboxSpecOverrides")


@_attrs_define
class TemplateFromSandboxSpecOverrides:
    """Safe template fields that may override values inherited from the source
    sandbox's originating template. Pool defaults to zero idle sandboxes
    when omitted.

        Attributes:
            description (Union[Unset, str]):
            display_name (Union[Unset, str]):
            tags (Union[Unset, list[str]]):
            pool (Union[Unset, PoolStrategy]):
    """

    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    pool: Union[Unset, "PoolStrategy"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        pool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if pool is not UNSET:
            field_dict["pool"] = pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pool_strategy import PoolStrategy

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, PoolStrategy]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = PoolStrategy.from_dict(_pool)

        template_from_sandbox_spec_overrides = cls(
            description=description,
            display_name=display_name,
            tags=tags,
            pool=pool,
        )

        return template_from_sandbox_spec_overrides
