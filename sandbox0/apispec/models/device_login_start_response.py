from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceLoginStartResponse")


@_attrs_define
class DeviceLoginStartResponse:
    """
    Attributes:
        device_login_id (str):
        user_code (str):
        verification_uri (str):
        expires_at (int):
        interval_seconds (int):
        verification_uri_complete (Union[Unset, str]):
    """

    device_login_id: str
    user_code: str
    verification_uri: str
    expires_at: int
    interval_seconds: int
    verification_uri_complete: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_login_id = self.device_login_id

        user_code = self.user_code

        verification_uri = self.verification_uri

        expires_at = self.expires_at

        interval_seconds = self.interval_seconds

        verification_uri_complete = self.verification_uri_complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device_login_id": device_login_id,
                "user_code": user_code,
                "verification_uri": verification_uri,
                "expires_at": expires_at,
                "interval_seconds": interval_seconds,
            }
        )
        if verification_uri_complete is not UNSET:
            field_dict["verification_uri_complete"] = verification_uri_complete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_login_id = d.pop("device_login_id")

        user_code = d.pop("user_code")

        verification_uri = d.pop("verification_uri")

        expires_at = d.pop("expires_at")

        interval_seconds = d.pop("interval_seconds")

        verification_uri_complete = d.pop("verification_uri_complete", UNSET)

        device_login_start_response = cls(
            device_login_id=device_login_id,
            user_code=user_code,
            verification_uri=verification_uri,
            expires_at=expires_at,
            interval_seconds=interval_seconds,
            verification_uri_complete=verification_uri_complete,
        )

        device_login_start_response.additional_properties = d
        return device_login_start_response

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
