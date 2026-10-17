from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SandboxRestartRequest")


@_attrs_define
class SandboxRestartRequest:
    """
    Attributes:
        expected_runtime_generation (int): Exact observed source runtime generation. Zero is allowed for a never-run
            paused sandbox. A changed source requires a new explicit request, never an automatic retry with a fresh
            generation.
    """

    expected_runtime_generation: int

    def to_dict(self) -> dict[str, Any]:
        expected_runtime_generation = self.expected_runtime_generation

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expected_runtime_generation": expected_runtime_generation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_runtime_generation = d.pop("expected_runtime_generation")

        sandbox_restart_request = cls(
            expected_runtime_generation=expected_runtime_generation,
        )

        return sandbox_restart_request
