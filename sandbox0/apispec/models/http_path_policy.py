from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HTTPPathPolicy")


@_attrs_define
class HTTPPathPolicy:
    """HTTP path allow and deny lists.

    Attributes:
        allowed (Union[Unset, list[str]]): When any allowed path list is non-empty, only listed exact paths are allowed.
        denied (Union[Unset, list[str]]): Exact paths that are always denied before allowed is evaluated.
        allowed_prefixes (Union[Unset, list[str]]): When any allowed path list is non-empty, only paths with listed
            prefixes are allowed.
        denied_prefixes (Union[Unset, list[str]]): Path prefixes that are always denied before allowed is evaluated.
    """

    allowed: Union[Unset, list[str]] = UNSET
    denied: Union[Unset, list[str]] = UNSET
    allowed_prefixes: Union[Unset, list[str]] = UNSET
    denied_prefixes: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = self.allowed

        denied: Union[Unset, list[str]] = UNSET
        if not isinstance(self.denied, Unset):
            denied = self.denied

        allowed_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_prefixes, Unset):
            allowed_prefixes = self.allowed_prefixes

        denied_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.denied_prefixes, Unset):
            denied_prefixes = self.denied_prefixes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if denied is not UNSET:
            field_dict["denied"] = denied
        if allowed_prefixes is not UNSET:
            field_dict["allowedPrefixes"] = allowed_prefixes
        if denied_prefixes is not UNSET:
            field_dict["deniedPrefixes"] = denied_prefixes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed = cast(list[str], d.pop("allowed", UNSET))

        denied = cast(list[str], d.pop("denied", UNSET))

        allowed_prefixes = cast(list[str], d.pop("allowedPrefixes", UNSET))

        denied_prefixes = cast(list[str], d.pop("deniedPrefixes", UNSET))

        http_path_policy = cls(
            allowed=allowed,
            denied=denied,
            allowed_prefixes=allowed_prefixes,
            denied_prefixes=denied_prefixes,
        )

        http_path_policy.additional_properties = d
        return http_path_policy

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
