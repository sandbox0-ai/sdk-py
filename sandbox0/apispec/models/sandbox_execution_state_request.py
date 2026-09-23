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
    """
    Attributes:
        memory (Union[Unset, bool]): Explicitly preserve or restore process memory and execution state. Omitted or false
            retains the existing filesystem-only behavior. Memory failures are reported without a cold fallback. Default:
            False.
    """

    memory: Union[Unset, bool] = False

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if memory is not UNSET:
            field_dict["memory"] = memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memory = d.pop("memory", UNSET)

        sandbox_execution_state_request = cls(
            memory=memory,
        )

        return sandbox_execution_state_request
