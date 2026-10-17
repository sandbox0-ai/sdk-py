from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SandboxRestartFinalCaptureFile")


@_attrs_define
class SandboxRestartFinalCaptureFile:
    """
    Attributes:
        operation_id (str):
        capture_id (str):
        runtime_generation (int):
        mutation_sequence (str):
        size_bytes (int):
        found (bool):
        content (str): Base64 content, at most 4 MiB decoded. Empty when found=false; found=true also permits an empty
            file. Never log or persist this response without owner encryption.
    """

    operation_id: str
    capture_id: str
    runtime_generation: int
    mutation_sequence: str
    size_bytes: int
    found: bool
    content: str

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        capture_id = self.capture_id

        runtime_generation = self.runtime_generation

        mutation_sequence = self.mutation_sequence

        size_bytes = self.size_bytes

        found = self.found

        content = self.content

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operation_id": operation_id,
                "capture_id": capture_id,
                "runtime_generation": runtime_generation,
                "mutation_sequence": mutation_sequence,
                "size_bytes": size_bytes,
                "found": found,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        capture_id = d.pop("capture_id")

        runtime_generation = d.pop("runtime_generation")

        mutation_sequence = d.pop("mutation_sequence")

        size_bytes = d.pop("size_bytes")

        found = d.pop("found")

        content = d.pop("content")

        sandbox_restart_final_capture_file = cls(
            operation_id=operation_id,
            capture_id=capture_id,
            runtime_generation=runtime_generation,
            mutation_sequence=mutation_sequence,
            size_bytes=size_bytes,
            found=found,
            content=content,
        )

        return sandbox_restart_final_capture_file
