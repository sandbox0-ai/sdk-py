import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sandbox_lifecycle_status import SandboxLifecycleStatus

T = TypeVar("T", bound="RebaseSandboxRootFSResponse")


@_attrs_define
class RebaseSandboxRootFSResponse:
    """
    Attributes:
        sandbox_id (str):
        generation_id (str):
        base_artifact_digest (str):
        rollback_expires_at (datetime.datetime):
        status (SandboxLifecycleStatus):
    """

    sandbox_id: str
    generation_id: str
    base_artifact_digest: str
    rollback_expires_at: datetime.datetime
    status: SandboxLifecycleStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        generation_id = self.generation_id

        base_artifact_digest = self.base_artifact_digest

        rollback_expires_at = self.rollback_expires_at.isoformat()

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "generation_id": generation_id,
                "base_artifact_digest": base_artifact_digest,
                "rollback_expires_at": rollback_expires_at,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        generation_id = d.pop("generation_id")

        base_artifact_digest = d.pop("base_artifact_digest")

        rollback_expires_at = isoparse(d.pop("rollback_expires_at"))

        status = SandboxLifecycleStatus(d.pop("status"))

        rebase_sandbox_root_fs_response = cls(
            sandbox_id=sandbox_id,
            generation_id=generation_id,
            base_artifact_digest=base_artifact_digest,
            rollback_expires_at=rollback_expires_at,
            status=status,
        )

        rebase_sandbox_root_fs_response.additional_properties = d
        return rebase_sandbox_root_fs_response

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
