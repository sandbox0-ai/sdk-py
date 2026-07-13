from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_audit_actor_kind import SandboxAuditActorKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxAuditActor")


@_attrs_define
class SandboxAuditActor:
    """
    Attributes:
        kind (SandboxAuditActorKind):
        id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        api_key_id (Union[Unset, str]):
        auth_method (Union[Unset, str]):
    """

    kind: SandboxAuditActorKind
    id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    api_key_id: Union[Unset, str] = UNSET
    auth_method: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        id = self.id

        user_id = self.user_id

        api_key_id = self.api_key_id

        auth_method = self.auth_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if api_key_id is not UNSET:
            field_dict["api_key_id"] = api_key_id
        if auth_method is not UNSET:
            field_dict["auth_method"] = auth_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = SandboxAuditActorKind(d.pop("kind"))

        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        api_key_id = d.pop("api_key_id", UNSET)

        auth_method = d.pop("auth_method", UNSET)

        sandbox_audit_actor = cls(
            kind=kind,
            id=id,
            user_id=user_id,
            api_key_id=api_key_id,
            auth_method=auth_method,
        )

        sandbox_audit_actor.additional_properties = d
        return sandbox_audit_actor

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
