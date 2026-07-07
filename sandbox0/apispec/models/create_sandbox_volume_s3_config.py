from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_sandbox_volume_s3_config_provider import (
    CreateSandboxVolumeS3ConfigProvider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSandboxVolumeS3Config")


@_attrs_define
class CreateSandboxVolumeS3Config:
    """
    Attributes:
        bucket (str):
        provider (Union[Unset, CreateSandboxVolumeS3ConfigProvider]): S3-compatible provider. ali is Aliyun OSS; r2 is
            Cloudflare R2. Default: CreateSandboxVolumeS3ConfigProvider.AWS.
        prefix (Union[Unset, str]): Optional object key prefix to expose as the volume root.
        region (Union[Unset, str]): Optional region override. Defaults to the storage-proxy S3 region when omitted.
        endpoint_url (Union[Unset, str]): Optional endpoint override. Required for ali and r2.
        access_key (Union[Unset, str]): Optional access key override. Must be provided together with secret_key.
        secret_key (Union[Unset, str]): Optional secret key override. Must be provided together with access_key.
        session_token (Union[Unset, str]): Optional temporary credential session token.
    """

    bucket: str
    provider: Union[Unset, CreateSandboxVolumeS3ConfigProvider] = (
        CreateSandboxVolumeS3ConfigProvider.AWS
    )
    prefix: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    endpoint_url: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    session_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        prefix = self.prefix

        region = self.region

        endpoint_url = self.endpoint_url

        access_key = self.access_key

        secret_key = self.secret_key

        session_token = self.session_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if region is not UNSET:
            field_dict["region"] = region
        if endpoint_url is not UNSET:
            field_dict["endpoint_url"] = endpoint_url
        if access_key is not UNSET:
            field_dict["access_key"] = access_key
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key
        if session_token is not UNSET:
            field_dict["session_token"] = session_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CreateSandboxVolumeS3ConfigProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = CreateSandboxVolumeS3ConfigProvider(_provider)

        prefix = d.pop("prefix", UNSET)

        region = d.pop("region", UNSET)

        endpoint_url = d.pop("endpoint_url", UNSET)

        access_key = d.pop("access_key", UNSET)

        secret_key = d.pop("secret_key", UNSET)

        session_token = d.pop("session_token", UNSET)

        create_sandbox_volume_s3_config = cls(
            bucket=bucket,
            provider=provider,
            prefix=prefix,
            region=region,
            endpoint_url=endpoint_url,
            access_key=access_key,
            secret_key=secret_key,
            session_token=session_token,
        )

        create_sandbox_volume_s3_config.additional_properties = d
        return create_sandbox_volume_s3_config

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
