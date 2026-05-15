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
    from ..models.pre_stop_hook import PreStopHook


T = TypeVar("T", bound="LifecyclePolicy")


@_attrs_define
class LifecyclePolicy:
    """
    Attributes:
        default_ttl (Union[Unset, int]):
        max_ttl (Union[Unset, int]):
        idle_timeout (Union[Unset, int]):
        pre_stop (Union[Unset, PreStopHook]):
    """

    default_ttl: Union[Unset, int] = UNSET
    max_ttl: Union[Unset, int] = UNSET
    idle_timeout: Union[Unset, int] = UNSET
    pre_stop: Union[Unset, "PreStopHook"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_ttl = self.default_ttl

        max_ttl = self.max_ttl

        idle_timeout = self.idle_timeout

        pre_stop: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pre_stop, Unset):
            pre_stop = self.pre_stop.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_ttl is not UNSET:
            field_dict["defaultTTL"] = default_ttl
        if max_ttl is not UNSET:
            field_dict["maxTTL"] = max_ttl
        if idle_timeout is not UNSET:
            field_dict["idleTimeout"] = idle_timeout
        if pre_stop is not UNSET:
            field_dict["preStop"] = pre_stop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pre_stop_hook import PreStopHook

        d = dict(src_dict)
        default_ttl = d.pop("defaultTTL", UNSET)

        max_ttl = d.pop("maxTTL", UNSET)

        idle_timeout = d.pop("idleTimeout", UNSET)

        _pre_stop = d.pop("preStop", UNSET)
        pre_stop: Union[Unset, PreStopHook]
        if isinstance(_pre_stop, Unset):
            pre_stop = UNSET
        else:
            pre_stop = PreStopHook.from_dict(_pre_stop)

        lifecycle_policy = cls(
            default_ttl=default_ttl,
            max_ttl=max_ttl,
            idle_timeout=idle_timeout,
            pre_stop=pre_stop,
        )

        lifecycle_policy.additional_properties = d
        return lifecycle_policy

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
