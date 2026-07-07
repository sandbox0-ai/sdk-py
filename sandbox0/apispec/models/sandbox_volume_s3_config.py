from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_volume_s3_config_provider import SandboxVolumeS3ConfigProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxVolumeS3Config")


@_attrs_define
class SandboxVolumeS3Config:
    """
    Attributes:
        provider (SandboxVolumeS3ConfigProvider):
        bucket (str):
        prefix (Union[Unset, str]):
        region (Union[Unset, str]):
        endpoint_url (Union[Unset, str]):
    """

    provider: SandboxVolumeS3ConfigProvider
    bucket: str
    prefix: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    endpoint_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.value

        bucket = self.bucket

        prefix = self.prefix

        region = self.region

        endpoint_url = self.endpoint_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "bucket": bucket,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if region is not UNSET:
            field_dict["region"] = region
        if endpoint_url is not UNSET:
            field_dict["endpoint_url"] = endpoint_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = SandboxVolumeS3ConfigProvider(d.pop("provider"))

        bucket = d.pop("bucket")

        prefix = d.pop("prefix", UNSET)

        region = d.pop("region", UNSET)

        endpoint_url = d.pop("endpoint_url", UNSET)

        sandbox_volume_s3_config = cls(
            provider=provider,
            bucket=bucket,
            prefix=prefix,
            region=region,
            endpoint_url=endpoint_url,
        )

        sandbox_volume_s3_config.additional_properties = d
        return sandbox_volume_s3_config

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
