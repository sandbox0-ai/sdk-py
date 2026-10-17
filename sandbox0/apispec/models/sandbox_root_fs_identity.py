import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sandbox_root_fs_identity_desired_state import (
    SandboxRootFSIdentityDesiredState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxRootFSIdentity")


@_attrs_define
class SandboxRootFSIdentity:
    """
    Attributes:
        sandbox_id (str): Observed sandbox identity.
        runtime_generation (int): Exact runtime generation at observation; zero is possible before first launch.
        lifecycle_epoch (int): Control-plane lifecycle epoch at observation.
        desired_state (SandboxRootFSIdentityDesiredState): Requested lifecycle state, not a guest health result.
        managed_files_size_bytes (int): Assigned external credential projection capacity; zero means legacy layout.
            Capacity is not credential safety evidence.
        filesystem_id (str): Opaque durable filesystem identity.
        head_generation_id (str): Last committed RootFS generation; live uncommitted writes are not represented.
        writer_epoch (int): Durable writer fence epoch; this does not prove a writer is currently alive.
        base_artifact_digest (str): Immutable base artifact digest.
        source_oci_digest (str): Immutable OCI source digest of the committed head.
        has_imported_filesystem (bool): True for retained import ancestry or a head owned by another filesystem. False
            alone never proves pristine or credential-clean history.
        active_lifecycle (bool): A lifecycle transaction was in progress at observation.
        sandbox_created_at (datetime.datetime): Control-plane sandbox creation time.
        filesystem_created_at (datetime.datetime): Durable filesystem creation time.
        observed_at (datetime.datetime): Database statement observation timestamp.
        runtime_compatibility_digest (Union[Unset, str]): Immutable runtime scheduling-class digest from the current
            active slot and matching external launch proof. Omitted during lifecycle transitions or when launch authority is
            absent, stale or mismatched. Binds the admitted runsc version and execution configuration; it is not a live
            Sentry observation or credential-safety attestation.
        retained_runtime_compatibility_digest (Union[Unset, str]): Runtime scheduling class of the exact retained
            external launch for recovery preflight, even after driver or writer lease expiry. Requires matching current
            sandbox generation, filesystem head/writer epoch, consumed writer grant and unreleased active resource lease.
            Omitted when that custody is absent, superseded, retired or transitioning. Does not establish current execution,
            permit ordinary credential access or authorize restart by itself; explicit restart still binds and fences the
            source before final capture.
    """

    sandbox_id: str
    runtime_generation: int
    lifecycle_epoch: int
    desired_state: SandboxRootFSIdentityDesiredState
    managed_files_size_bytes: int
    filesystem_id: str
    head_generation_id: str
    writer_epoch: int
    base_artifact_digest: str
    source_oci_digest: str
    has_imported_filesystem: bool
    active_lifecycle: bool
    sandbox_created_at: datetime.datetime
    filesystem_created_at: datetime.datetime
    observed_at: datetime.datetime
    runtime_compatibility_digest: Union[Unset, str] = UNSET
    retained_runtime_compatibility_digest: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        runtime_generation = self.runtime_generation

        lifecycle_epoch = self.lifecycle_epoch

        desired_state = self.desired_state.value

        managed_files_size_bytes = self.managed_files_size_bytes

        filesystem_id = self.filesystem_id

        head_generation_id = self.head_generation_id

        writer_epoch = self.writer_epoch

        base_artifact_digest = self.base_artifact_digest

        source_oci_digest = self.source_oci_digest

        has_imported_filesystem = self.has_imported_filesystem

        active_lifecycle = self.active_lifecycle

        sandbox_created_at = self.sandbox_created_at.isoformat()

        filesystem_created_at = self.filesystem_created_at.isoformat()

        observed_at = self.observed_at.isoformat()

        runtime_compatibility_digest = self.runtime_compatibility_digest

        retained_runtime_compatibility_digest = (
            self.retained_runtime_compatibility_digest
        )

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "runtime_generation": runtime_generation,
                "lifecycle_epoch": lifecycle_epoch,
                "desired_state": desired_state,
                "managed_files_size_bytes": managed_files_size_bytes,
                "filesystem_id": filesystem_id,
                "head_generation_id": head_generation_id,
                "writer_epoch": writer_epoch,
                "base_artifact_digest": base_artifact_digest,
                "source_oci_digest": source_oci_digest,
                "has_imported_filesystem": has_imported_filesystem,
                "active_lifecycle": active_lifecycle,
                "sandbox_created_at": sandbox_created_at,
                "filesystem_created_at": filesystem_created_at,
                "observed_at": observed_at,
            }
        )
        if runtime_compatibility_digest is not UNSET:
            field_dict["runtime_compatibility_digest"] = runtime_compatibility_digest
        if retained_runtime_compatibility_digest is not UNSET:
            field_dict["retained_runtime_compatibility_digest"] = (
                retained_runtime_compatibility_digest
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        runtime_generation = d.pop("runtime_generation")

        lifecycle_epoch = d.pop("lifecycle_epoch")

        desired_state = SandboxRootFSIdentityDesiredState(d.pop("desired_state"))

        managed_files_size_bytes = d.pop("managed_files_size_bytes")

        filesystem_id = d.pop("filesystem_id")

        head_generation_id = d.pop("head_generation_id")

        writer_epoch = d.pop("writer_epoch")

        base_artifact_digest = d.pop("base_artifact_digest")

        source_oci_digest = d.pop("source_oci_digest")

        has_imported_filesystem = d.pop("has_imported_filesystem")

        active_lifecycle = d.pop("active_lifecycle")

        sandbox_created_at = isoparse(d.pop("sandbox_created_at"))

        filesystem_created_at = isoparse(d.pop("filesystem_created_at"))

        observed_at = isoparse(d.pop("observed_at"))

        runtime_compatibility_digest = d.pop("runtime_compatibility_digest", UNSET)

        retained_runtime_compatibility_digest = d.pop(
            "retained_runtime_compatibility_digest", UNSET
        )

        sandbox_root_fs_identity = cls(
            sandbox_id=sandbox_id,
            runtime_generation=runtime_generation,
            lifecycle_epoch=lifecycle_epoch,
            desired_state=desired_state,
            managed_files_size_bytes=managed_files_size_bytes,
            filesystem_id=filesystem_id,
            head_generation_id=head_generation_id,
            writer_epoch=writer_epoch,
            base_artifact_digest=base_artifact_digest,
            source_oci_digest=source_oci_digest,
            has_imported_filesystem=has_imported_filesystem,
            active_lifecycle=active_lifecycle,
            sandbox_created_at=sandbox_created_at,
            filesystem_created_at=filesystem_created_at,
            observed_at=observed_at,
            runtime_compatibility_digest=runtime_compatibility_digest,
            retained_runtime_compatibility_digest=retained_runtime_compatibility_digest,
        )

        return sandbox_root_fs_identity
