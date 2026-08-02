import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefreshResponse")


@_attrs_define
class RefreshResponse:
    """
    Attributes:
        sandbox_id (str):
        expires_at (Union[None, Unset, datetime.datetime]): Soft expiration timestamp. Omitted or null means disabled or
            not set.
        hard_expires_at (Union[None, Unset, datetime.datetime]): Hard expiration timestamp. Omitted or null means
            disabled or not set.
    """

    sandbox_id: str
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    hard_expires_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        hard_expires_at: Union[None, Unset, str]
        if isinstance(self.hard_expires_at, Unset):
            hard_expires_at = UNSET
        elif isinstance(self.hard_expires_at, datetime.datetime):
            hard_expires_at = self.hard_expires_at.isoformat()
        else:
            hard_expires_at = self.hard_expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if hard_expires_at is not UNSET:
            field_dict["hard_expires_at"] = hard_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        def _parse_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_hard_expires_at(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hard_expires_at_type_0 = isoparse(data)

                return hard_expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        hard_expires_at = _parse_hard_expires_at(d.pop("hard_expires_at", UNSET))

        refresh_response = cls(
            sandbox_id=sandbox_id,
            expires_at=expires_at,
            hard_expires_at=hard_expires_at,
        )

        refresh_response.additional_properties = d
        return refresh_response

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
