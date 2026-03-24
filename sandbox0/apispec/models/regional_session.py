from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegionalSession")


@_attrs_define
class RegionalSession:
    """
    Attributes:
        region_id (str):
        token (str):
        expires_at (int):
        regional_gateway_url (Union[None, Unset, str]):
    """

    region_id: str
    token: str
    expires_at: int
    regional_gateway_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_id = self.region_id

        token = self.token

        expires_at = self.expires_at

        regional_gateway_url: Union[None, Unset, str]
        if isinstance(self.regional_gateway_url, Unset):
            regional_gateway_url = UNSET
        else:
            regional_gateway_url = self.regional_gateway_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region_id": region_id,
                "token": token,
                "expires_at": expires_at,
            }
        )
        if regional_gateway_url is not UNSET:
            field_dict["regional_gateway_url"] = regional_gateway_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        region_id = d.pop("region_id")

        token = d.pop("token")

        expires_at = d.pop("expires_at")

        def _parse_regional_gateway_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        regional_gateway_url = _parse_regional_gateway_url(
            d.pop("regional_gateway_url", UNSET)
        )

        regional_session = cls(
            region_id=region_id,
            token=token,
            expires_at=expires_at,
            regional_gateway_url=regional_gateway_url,
        )

        regional_session.additional_properties = d
        return regional_session

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
