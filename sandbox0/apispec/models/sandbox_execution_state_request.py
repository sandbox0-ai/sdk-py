from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxExecutionStateRequest")


@_attrs_define
class SandboxExecutionStateRequest:
    """Resume execution-state selection. Conditional memory resume requires all three body fields together with
    Idempotency-Key.

        Attributes:
            memory (Union[Unset, bool]): Require the retained execution image. Missing, incompatible, or failed memory
                restoration remains an error and never falls back to new processes. Omitted or false explicitly selects
                filesystem-only behavior. Default: False.
            expected_runtime_generation (Union[Unset, int]): Exact paused source generation. Zero is valid for a never-run
                memory fork. Requires memory=true, checkpoint_id and Idempotency-Key.
            checkpoint_id (Union[Unset, str]): Exact retained capture operation ID, returned as operation_id by a completed
                conditional memory pause. Requires memory=true, expected_runtime_generation and Idempotency-Key.
    """

    memory: Union[Unset, bool] = False
    expected_runtime_generation: Union[Unset, int] = UNSET
    checkpoint_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        expected_runtime_generation = self.expected_runtime_generation

        checkpoint_id = self.checkpoint_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if memory is not UNSET:
            field_dict["memory"] = memory
        if expected_runtime_generation is not UNSET:
            field_dict["expected_runtime_generation"] = expected_runtime_generation
        if checkpoint_id is not UNSET:
            field_dict["checkpoint_id"] = checkpoint_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memory = d.pop("memory", UNSET)

        expected_runtime_generation = d.pop("expected_runtime_generation", UNSET)

        checkpoint_id = d.pop("checkpoint_id", UNSET)

        sandbox_execution_state_request = cls(
            memory=memory,
            expected_runtime_generation=expected_runtime_generation,
            checkpoint_id=checkpoint_id,
        )

        return sandbox_execution_state_request
