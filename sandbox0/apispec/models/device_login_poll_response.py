from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_login_poll_response_status import DeviceLoginPollResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_response import LoginResponse


T = TypeVar("T", bound="DeviceLoginPollResponse")


@_attrs_define
class DeviceLoginPollResponse:
    """
    Attributes:
        status (DeviceLoginPollResponseStatus):
        interval_seconds (Union[Unset, int]):
        expires_at (Union[Unset, int]):
        login (Union[Unset, LoginResponse]):
    """

    status: DeviceLoginPollResponseStatus
    interval_seconds: Union[Unset, int] = UNSET
    expires_at: Union[Unset, int] = UNSET
    login: Union[Unset, "LoginResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        interval_seconds = self.interval_seconds

        expires_at = self.expires_at

        login: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.login, Unset):
            login = self.login.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if interval_seconds is not UNSET:
            field_dict["interval_seconds"] = interval_seconds
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if login is not UNSET:
            field_dict["login"] = login

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_response import LoginResponse

        d = dict(src_dict)
        status = DeviceLoginPollResponseStatus(d.pop("status"))

        interval_seconds = d.pop("interval_seconds", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        _login = d.pop("login", UNSET)
        login: Union[Unset, LoginResponse]
        if isinstance(_login, Unset):
            login = UNSET
        else:
            login = LoginResponse.from_dict(_login)

        device_login_poll_response = cls(
            status=status,
            interval_seconds=interval_seconds,
            expires_at=expires_at,
            login=login,
        )

        device_login_poll_response.additional_properties = d
        return device_login_poll_response

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
