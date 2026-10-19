from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StaticS3SourceSpec")


@_attrs_define
class StaticS3SourceSpec:
    """Team-owned S3 connection for isolated external mounts. Stored as platform-side secret material; never returned in
    source metadata or injected into the user sandbox.

        Attributes:
            bucket (str):
            region (str):
            access_key (str):
            secret_key (str):
            prefix (Union[Unset, str]): Optional canonical directory prefix ending in a slash. Mount bindings may only
                narrow this scope. The combined S3 key must fit 1024 UTF-8 bytes.
            endpoint_url (Union[Unset, str]): Optional HTTPS origin for an S3-compatible provider. Private and metadata
                network addresses are rejected by the worker transport.
            allow_write (Union[Unset, bool]): Authorizes writable bindings. Omitted or false permits read-only mounts only.
                Default: False.
            session_token (Union[Unset, str]):
    """

    bucket: str
    region: str
    access_key: str
    secret_key: str
    prefix: Union[Unset, str] = UNSET
    endpoint_url: Union[Unset, str] = UNSET
    allow_write: Union[Unset, bool] = False
    session_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        region = self.region

        access_key = self.access_key

        secret_key = self.secret_key

        prefix = self.prefix

        endpoint_url = self.endpoint_url

        allow_write = self.allow_write

        session_token = self.session_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "region": region,
                "accessKey": access_key,
                "secretKey": secret_key,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if endpoint_url is not UNSET:
            field_dict["endpointUrl"] = endpoint_url
        if allow_write is not UNSET:
            field_dict["allowWrite"] = allow_write
        if session_token is not UNSET:
            field_dict["sessionToken"] = session_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        region = d.pop("region")

        access_key = d.pop("accessKey")

        secret_key = d.pop("secretKey")

        prefix = d.pop("prefix", UNSET)

        endpoint_url = d.pop("endpointUrl", UNSET)

        allow_write = d.pop("allowWrite", UNSET)

        session_token = d.pop("sessionToken", UNSET)

        static_s3_source_spec = cls(
            bucket=bucket,
            region=region,
            access_key=access_key,
            secret_key=secret_key,
            prefix=prefix,
            endpoint_url=endpoint_url,
            allow_write=allow_write,
            session_token=session_token,
        )

        static_s3_source_spec.additional_properties = d
        return static_s3_source_spec

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
