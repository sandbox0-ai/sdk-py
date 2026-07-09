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
    from ..models.http_channel_spec_headers import HTTPChannelSpecHeaders


T = TypeVar("T", bound="HTTPChannelSpec")


@_attrs_define
class HTTPChannelSpec:
    """
    Attributes:
        base_url (str):
        headers (Union[Unset, HTTPChannelSpecHeaders]):
        timeout_sec (Union[Unset, int]):
    """

    base_url: str
    headers: Union[Unset, "HTTPChannelSpecHeaders"] = UNSET
    timeout_sec: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_url = self.base_url

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        timeout_sec = self.timeout_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_url": base_url,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if timeout_sec is not UNSET:
            field_dict["timeout_sec"] = timeout_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_channel_spec_headers import HTTPChannelSpecHeaders

        d = dict(src_dict)
        base_url = d.pop("base_url")

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, HTTPChannelSpecHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HTTPChannelSpecHeaders.from_dict(_headers)

        timeout_sec = d.pop("timeout_sec", UNSET)

        http_channel_spec = cls(
            base_url=base_url,
            headers=headers,
            timeout_sec=timeout_sec,
        )

        http_channel_spec.additional_properties = d
        return http_channel_spec

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
