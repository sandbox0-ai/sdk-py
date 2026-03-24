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
    from ..models.regional_session import RegionalSession
    from ..models.user import User


T = TypeVar("T", bound="LoginResponse")


@_attrs_define
class LoginResponse:
    """
    Attributes:
        access_token (str):
        refresh_token (str):
        expires_at (int):
        user (User):
        regional_session (Union[Unset, RegionalSession]):
    """

    access_token: str
    refresh_token: str
    expires_at: int
    user: "User"
    regional_session: Union[Unset, "RegionalSession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        refresh_token = self.refresh_token

        expires_at = self.expires_at

        user = self.user.to_dict()

        regional_session: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.regional_session, Unset):
            regional_session = self.regional_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_at": expires_at,
                "user": user,
            }
        )
        if regional_session is not UNSET:
            field_dict["regional_session"] = regional_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regional_session import RegionalSession
        from ..models.user import User

        d = dict(src_dict)
        access_token = d.pop("access_token")

        refresh_token = d.pop("refresh_token")

        expires_at = d.pop("expires_at")

        user = User.from_dict(d.pop("user"))

        _regional_session = d.pop("regional_session", UNSET)
        regional_session: Union[Unset, RegionalSession]
        if isinstance(_regional_session, Unset):
            regional_session = UNSET
        else:
            regional_session = RegionalSession.from_dict(_regional_session)

        login_response = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=expires_at,
            user=user,
            regional_session=regional_session,
        )

        login_response.additional_properties = d
        return login_response

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
