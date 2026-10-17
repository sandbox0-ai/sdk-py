from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_files_state_guest_path import ManagedFilesStateGuestPath

T = TypeVar("T", bound="ManagedFileReadResponse")


@_attrs_define
class ManagedFileReadResponse:
    """
    Attributes:
        runtime_generation (int):
        mutation_sequence (str): Canonical decimal uint64 platform mutation counter. It is not a content hash and does
            not change on native guest writes.
        size_bytes (int): Capacity of this runtime's node-owned noswap tmpfs; excluded from durable RootFS.
        guest_path (ManagedFilesStateGuestPath): Initial guest bind path. Guest pivot or mount changes do not redirect
            platform writes.
        content (str): Base64-encoded file bytes, at most 4 MiB decoded. Treat as sensitive and do not log.
    """

    runtime_generation: int
    mutation_sequence: str
    size_bytes: int
    guest_path: ManagedFilesStateGuestPath
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runtime_generation = self.runtime_generation

        mutation_sequence = self.mutation_sequence

        size_bytes = self.size_bytes

        guest_path = self.guest_path.value

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runtime_generation": runtime_generation,
                "mutation_sequence": mutation_sequence,
                "size_bytes": size_bytes,
                "guest_path": guest_path,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        runtime_generation = d.pop("runtime_generation")

        mutation_sequence = d.pop("mutation_sequence")

        size_bytes = d.pop("size_bytes")

        guest_path = ManagedFilesStateGuestPath(d.pop("guest_path"))

        content = d.pop("content")

        managed_file_read_response = cls(
            runtime_generation=runtime_generation,
            mutation_sequence=mutation_sequence,
            size_bytes=size_bytes,
            guest_path=guest_path,
            content=content,
        )

        managed_file_read_response.additional_properties = d
        return managed_file_read_response

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
