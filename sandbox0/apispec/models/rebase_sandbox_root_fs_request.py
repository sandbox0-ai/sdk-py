from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RebaseSandboxRootFSRequest")


@_attrs_define
class RebaseSandboxRootFSRequest:
    """
    Attributes:
        target_base_artifact_digest (str): Canonical SHA-256 digest of an already-attested immutable RootFS Base
            artifact.
        rollback_ttl (Union[Unset, int]): Rollback retention in seconds. Defaults to 86400 seconds and cannot exceed
            seven days.
    """

    target_base_artifact_digest: str
    rollback_ttl: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_base_artifact_digest = self.target_base_artifact_digest

        rollback_ttl = self.rollback_ttl

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target_base_artifact_digest": target_base_artifact_digest,
            }
        )
        if rollback_ttl is not UNSET:
            field_dict["rollback_ttl"] = rollback_ttl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_base_artifact_digest = d.pop("target_base_artifact_digest")

        rollback_ttl = d.pop("rollback_ttl", UNSET)

        rebase_sandbox_root_fs_request = cls(
            target_base_artifact_digest=target_base_artifact_digest,
            rollback_ttl=rollback_ttl,
        )

        return rebase_sandbox_root_fs_request
