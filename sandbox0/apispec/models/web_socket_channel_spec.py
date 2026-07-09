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
    from ..models.web_socket_channel_spec_headers import WebSocketChannelSpecHeaders


T = TypeVar("T", bound="WebSocketChannelSpec")


@_attrs_define
class WebSocketChannelSpec:
    """
    Attributes:
        url (str):
        headers (Union[Unset, WebSocketChannelSpecHeaders]):
    """

    url: str
    headers: Union[Unset, "WebSocketChannelSpecHeaders"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_socket_channel_spec_headers import WebSocketChannelSpecHeaders

        d = dict(src_dict)
        url = d.pop("url")

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, WebSocketChannelSpecHeaders]
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WebSocketChannelSpecHeaders.from_dict(_headers)

        web_socket_channel_spec = cls(
            url=url,
            headers=headers,
        )

        web_socket_channel_spec.additional_properties = d
        return web_socket_channel_spec

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
