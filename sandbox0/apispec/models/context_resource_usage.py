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
    from ..models.resource_usage import ResourceUsage


T = TypeVar("T", bound="ContextResourceUsage")


@_attrs_define
class ContextResourceUsage:
    """
    Attributes:
        context_id (Union[Unset, str]):
        type_ (Union[Unset, str]):
        alias (Union[Unset, str]): Alias for the REPL or CLI tool (e.g., python, node, bash, redis-cli)
        running (Union[Unset, bool]):
        paused (Union[Unset, bool]):
        usage (Union[Unset, ResourceUsage]):
    """

    context_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    running: Union[Unset, bool] = UNSET
    paused: Union[Unset, bool] = UNSET
    usage: Union[Unset, "ResourceUsage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_id = self.context_id

        type_ = self.type_

        alias = self.alias

        running = self.running

        paused = self.paused

        usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_id is not UNSET:
            field_dict["context_id"] = context_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if alias is not UNSET:
            field_dict["alias"] = alias
        if running is not UNSET:
            field_dict["running"] = running
        if paused is not UNSET:
            field_dict["paused"] = paused
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_usage import ResourceUsage

        d = dict(src_dict)
        context_id = d.pop("context_id", UNSET)

        type_ = d.pop("type", UNSET)

        alias = d.pop("alias", UNSET)

        running = d.pop("running", UNSET)

        paused = d.pop("paused", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, ResourceUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = ResourceUsage.from_dict(_usage)

        context_resource_usage = cls(
            context_id=context_id,
            type_=type_,
            alias=alias,
            running=running,
            paused=paused,
            usage=usage,
        )

        context_resource_usage.additional_properties = d
        return context_resource_usage

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
