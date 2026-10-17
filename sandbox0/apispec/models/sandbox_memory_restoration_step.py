from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SandboxMemoryRestorationStep")


@_attrs_define
class SandboxMemoryRestorationStep:
    """
    Attributes:
        operation_id (str):
        capture_operation_id (str):
        from_runtime_generation (int):
        to_runtime_generation (int):
        restore_id (str): Opaque committed restore identity, never an execution grant.
        managed_files_size_bytes (int): Zero for a legacy image without managed-file projection. Nonzero means the exact
            projected backing was required by the restored assignment.
    """

    operation_id: str
    capture_operation_id: str
    from_runtime_generation: int
    to_runtime_generation: int
    restore_id: str
    managed_files_size_bytes: int

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        capture_operation_id = self.capture_operation_id

        from_runtime_generation = self.from_runtime_generation

        to_runtime_generation = self.to_runtime_generation

        restore_id = self.restore_id

        managed_files_size_bytes = self.managed_files_size_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operation_id": operation_id,
                "capture_operation_id": capture_operation_id,
                "from_runtime_generation": from_runtime_generation,
                "to_runtime_generation": to_runtime_generation,
                "restore_id": restore_id,
                "managed_files_size_bytes": managed_files_size_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        capture_operation_id = d.pop("capture_operation_id")

        from_runtime_generation = d.pop("from_runtime_generation")

        to_runtime_generation = d.pop("to_runtime_generation")

        restore_id = d.pop("restore_id")

        managed_files_size_bytes = d.pop("managed_files_size_bytes")

        sandbox_memory_restoration_step = cls(
            operation_id=operation_id,
            capture_operation_id=capture_operation_id,
            from_runtime_generation=from_runtime_generation,
            to_runtime_generation=to_runtime_generation,
            restore_id=restore_id,
            managed_files_size_bytes=managed_files_size_bytes,
        )

        return sandbox_memory_restoration_step
