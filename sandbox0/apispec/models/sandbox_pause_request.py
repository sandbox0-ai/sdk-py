from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxPauseRequest")


@_attrs_define
class SandboxPauseRequest:
    """
    Attributes:
        memory (Union[Unset, bool]): Require retained process memory and execution state. Capture failure never falls
            back to filesystem-only pause. Default: False.
        expected_runtime_generation (Union[Unset, int]): Pause only this source runtime generation. Requires memory=true
            and Idempotency-Key; stale requests never pause a successor.
    """

    memory: Union[Unset, bool] = False
    expected_runtime_generation: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        expected_runtime_generation = self.expected_runtime_generation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if memory is not UNSET:
            field_dict["memory"] = memory
        if expected_runtime_generation is not UNSET:
            field_dict["expected_runtime_generation"] = expected_runtime_generation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memory = d.pop("memory", UNSET)

        expected_runtime_generation = d.pop("expected_runtime_generation", UNSET)

        sandbox_pause_request = cls(
            memory=memory,
            expected_runtime_generation=expected_runtime_generation,
        )

        return sandbox_pause_request
