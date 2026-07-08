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
        access_key (str): Access key for this S3 backend volume. Required with secret_key. Stored encrypted and omitted
            from API responses.
        secret_key (str): Secret key for this S3 backend volume. Required with access_key. Stored encrypted and omitted
            from API responses.
        provider (Union[Unset, CreateSandboxVolumeS3ConfigProvider]): S3-compatible provider. ali is Aliyun OSS; r2 is
            Cloudflare R2. Default: CreateSandboxVolumeS3ConfigProvider.AWS.
        prefix (Union[Unset, str]): Optional object key prefix to expose as the volume root.
        region (Union[Unset, str]): AWS region for the target bucket. Required for provider aws unless endpoint_url is
            provided.
        endpoint_url (Union[Unset, str]): Optional endpoint override. Required for ali and r2. For aws, endpoint_url can
            be used instead of region for S3-compatible endpoints.
        session_token (Union[Unset, str]): Optional temporary credential session token.
    """

    bucket: str
    access_key: str
    secret_key: str
    provider: Union[Unset, CreateSandboxVolumeS3ConfigProvider] = (
        CreateSandboxVolumeS3ConfigProvider.AWS
    )
    prefix: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    endpoint_url: Union[Unset, str] = UNSET
    session_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        access_key = self.access_key

        secret_key = self.secret_key

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        prefix = self.prefix

        region = self.region

        endpoint_url = self.endpoint_url

        session_token = self.session_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "access_key": access_key,
                "secret_key": secret_key,
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
        if session_token is not UNSET:
            field_dict["session_token"] = session_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        access_key = d.pop("access_key")

        secret_key = d.pop("secret_key")

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CreateSandboxVolumeS3ConfigProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = CreateSandboxVolumeS3ConfigProvider(_provider)

        prefix = d.pop("prefix", UNSET)

        region = d.pop("region", UNSET)

        endpoint_url = d.pop("endpoint_url", UNSET)

        session_token = d.pop("session_token", UNSET)

        create_sandbox_volume_s3_config = cls(
            bucket=bucket,
            access_key=access_key,
            secret_key=secret_key,
            provider=provider,
            prefix=prefix,
            region=region,
            endpoint_url=endpoint_url,
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
