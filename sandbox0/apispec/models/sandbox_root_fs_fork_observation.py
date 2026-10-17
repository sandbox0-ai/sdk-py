import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="SandboxRootFSForkObservation")


@_attrs_define
class SandboxRootFSForkObservation:
    """
    Attributes:
        operation_id (str):
        source_sandbox_id (str):
        target_sandbox_id (str):
        source_runtime_generation (int):
        source_filesystem_id (str):
        source_head_generation_id (str):
        target_filesystem_id (str):
        target_head_generation_id (str):
        base_artifact_digest (str):
        source_oci_digest (str):
        writer_epoch (int):
        managed_files_size_bytes (int):
        auto_resume (bool):
        automatic_routes (bool):
        sandbox_created_at (datetime.datetime):
        filesystem_created_at (datetime.datetime):
        observed_at (datetime.datetime):
    """

    operation_id: str
    source_sandbox_id: str
    target_sandbox_id: str
    source_runtime_generation: int
    source_filesystem_id: str
    source_head_generation_id: str
    target_filesystem_id: str
    target_head_generation_id: str
    base_artifact_digest: str
    source_oci_digest: str
    writer_epoch: int
    managed_files_size_bytes: int
    auto_resume: bool
    automatic_routes: bool
    sandbox_created_at: datetime.datetime
    filesystem_created_at: datetime.datetime
    observed_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        source_sandbox_id = self.source_sandbox_id

        target_sandbox_id = self.target_sandbox_id

        source_runtime_generation = self.source_runtime_generation

        source_filesystem_id = self.source_filesystem_id

        source_head_generation_id = self.source_head_generation_id

        target_filesystem_id = self.target_filesystem_id

        target_head_generation_id = self.target_head_generation_id

        base_artifact_digest = self.base_artifact_digest

        source_oci_digest = self.source_oci_digest

        writer_epoch = self.writer_epoch

        managed_files_size_bytes = self.managed_files_size_bytes

        auto_resume = self.auto_resume

        automatic_routes = self.automatic_routes

        sandbox_created_at = self.sandbox_created_at.isoformat()

        filesystem_created_at = self.filesystem_created_at.isoformat()

        observed_at = self.observed_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operation_id": operation_id,
                "source_sandbox_id": source_sandbox_id,
                "target_sandbox_id": target_sandbox_id,
                "source_runtime_generation": source_runtime_generation,
                "source_filesystem_id": source_filesystem_id,
                "source_head_generation_id": source_head_generation_id,
                "target_filesystem_id": target_filesystem_id,
                "target_head_generation_id": target_head_generation_id,
                "base_artifact_digest": base_artifact_digest,
                "source_oci_digest": source_oci_digest,
                "writer_epoch": writer_epoch,
                "managed_files_size_bytes": managed_files_size_bytes,
                "auto_resume": auto_resume,
                "automatic_routes": automatic_routes,
                "sandbox_created_at": sandbox_created_at,
                "filesystem_created_at": filesystem_created_at,
                "observed_at": observed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        source_sandbox_id = d.pop("source_sandbox_id")

        target_sandbox_id = d.pop("target_sandbox_id")

        source_runtime_generation = d.pop("source_runtime_generation")

        source_filesystem_id = d.pop("source_filesystem_id")

        source_head_generation_id = d.pop("source_head_generation_id")

        target_filesystem_id = d.pop("target_filesystem_id")

        target_head_generation_id = d.pop("target_head_generation_id")

        base_artifact_digest = d.pop("base_artifact_digest")

        source_oci_digest = d.pop("source_oci_digest")

        writer_epoch = d.pop("writer_epoch")

        managed_files_size_bytes = d.pop("managed_files_size_bytes")

        auto_resume = d.pop("auto_resume")

        automatic_routes = d.pop("automatic_routes")

        sandbox_created_at = isoparse(d.pop("sandbox_created_at"))

        filesystem_created_at = isoparse(d.pop("filesystem_created_at"))

        observed_at = isoparse(d.pop("observed_at"))

        sandbox_root_fs_fork_observation = cls(
            operation_id=operation_id,
            source_sandbox_id=source_sandbox_id,
            target_sandbox_id=target_sandbox_id,
            source_runtime_generation=source_runtime_generation,
            source_filesystem_id=source_filesystem_id,
            source_head_generation_id=source_head_generation_id,
            target_filesystem_id=target_filesystem_id,
            target_head_generation_id=target_head_generation_id,
            base_artifact_digest=base_artifact_digest,
            source_oci_digest=source_oci_digest,
            writer_epoch=writer_epoch,
            managed_files_size_bytes=managed_files_size_bytes,
            auto_resume=auto_resume,
            automatic_routes=automatic_routes,
            sandbox_created_at=sandbox_created_at,
            filesystem_created_at=filesystem_created_at,
            observed_at=observed_at,
        )

        return sandbox_root_fs_fork_observation
