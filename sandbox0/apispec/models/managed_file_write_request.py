from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ManagedFileWriteRequest")


@_attrs_define
class ManagedFileWriteRequest:
    """
    Attributes:
        expected_mutation_sequence (str): Canonical decimal uint64 platform mutation counter. It is not a content hash
            and does not change on native guest writes.
        content (str): Base64-encoded file bytes, at most 4 MiB decoded. Empty content is permitted.
    """

    expected_mutation_sequence: str
    content: str

    def to_dict(self) -> dict[str, Any]:
        expected_mutation_sequence = self.expected_mutation_sequence

        content = self.content

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expected_mutation_sequence": expected_mutation_sequence,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_mutation_sequence = d.pop("expected_mutation_sequence")

        content = d.pop("content")

        managed_file_write_request = cls(
            expected_mutation_sequence=expected_mutation_sequence,
            content=content,
        )

        return managed_file_write_request
