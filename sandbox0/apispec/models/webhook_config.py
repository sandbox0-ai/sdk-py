from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookConfig")


@_attrs_define
class WebhookConfig:
    """
    Attributes:
        url (Union[Unset, str]): Required when webhook is enabled. Target URL that receives event callbacks.
        secret (Union[Unset, str]): Optional. Shared secret used to sign webhook payloads.
        watch_dir (Union[Unset, str]): Optional. When set, procd subscribes to file events under this directory (same
            semantics as the file watch WebSocket API) and emits file.modified events.
    """

    url: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    watch_dir: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        secret = self.secret

        watch_dir = self.watch_dir

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if secret is not UNSET:
            field_dict["secret"] = secret
        if watch_dir is not UNSET:
            field_dict["watch_dir"] = watch_dir

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        secret = d.pop("secret", UNSET)

        watch_dir = d.pop("watch_dir", UNSET)

        webhook_config = cls(
            url=url,
            secret=secret,
            watch_dir=watch_dir,
        )

        webhook_config.additional_properties = d
        return webhook_config

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
