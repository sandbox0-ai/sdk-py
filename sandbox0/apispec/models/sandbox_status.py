from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxStatus")


@_attrs_define
class SandboxStatus:
    """
    Attributes:
        sandbox_id (Union[Unset, str]):
        template_id (Union[Unset, str]):
        team_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        pod_name (Union[Unset, str]):
        status (Union[Unset, str]):
        claimed_at (Union[Unset, str]):
        expires_at (Union[Unset, str]):
        created_at (Union[Unset, str]):
    """

    sandbox_id: Union[Unset, str] = UNSET
    template_id: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    pod_name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    claimed_at: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        template_id = self.template_id

        team_id = self.team_id

        user_id = self.user_id

        pod_name = self.pod_name

        status = self.status

        claimed_at = self.claimed_at

        expires_at = self.expires_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if pod_name is not UNSET:
            field_dict["pod_name"] = pod_name
        if status is not UNSET:
            field_dict["status"] = status
        if claimed_at is not UNSET:
            field_dict["claimed_at"] = claimed_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id", UNSET)

        template_id = d.pop("template_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        user_id = d.pop("user_id", UNSET)

        pod_name = d.pop("pod_name", UNSET)

        status = d.pop("status", UNSET)

        claimed_at = d.pop("claimed_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        created_at = d.pop("created_at", UNSET)

        sandbox_status = cls(
            sandbox_id=sandbox_id,
            template_id=template_id,
            team_id=team_id,
            user_id=user_id,
            pod_name=pod_name,
            status=status,
            claimed_at=claimed_at,
            expires_at=expires_at,
            created_at=created_at,
        )

        sandbox_status.additional_properties = d
        return sandbox_status

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
