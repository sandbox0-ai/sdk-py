from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..models.sandbox_memory_operation_action import SandboxMemoryOperationAction
from ..models.sandbox_memory_operation_reason import SandboxMemoryOperationReason
from ..models.sandbox_memory_operation_state import SandboxMemoryOperationState
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxMemoryOperation")


@_attrs_define
class SandboxMemoryOperation:
    """
    Attributes:
        sandbox_id (str):
        operation_id (str): Authenticated caller request ID, never the internal restore worker operation ID.
        checkpoint_id (str):
        action (SandboxMemoryOperationAction):
        from_runtime_generation (int):
        lifecycle_epoch (int): Original operation epoch. Bind subsequent current-identity checks to this epoch; current
            is only a read snapshot.
        state (SandboxMemoryOperationState):
        current (bool): Whether this terminal result still matches the owner snapshot. False for pending and capture
            failure. Never a new lease or execution authorization.
        result_runtime_generation (Union[Unset, int]): Present only for completed or physically resolved failed resume;
            equals source plus one in both cases.
        reason (Union[Unset, SandboxMemoryOperationReason]): Present only for canceled or failed. A failed capture never
            attests that the source survived.
    """

    sandbox_id: str
    operation_id: str
    checkpoint_id: str
    action: SandboxMemoryOperationAction
    from_runtime_generation: int
    lifecycle_epoch: int
    state: SandboxMemoryOperationState
    current: bool
    result_runtime_generation: Union[Unset, int] = UNSET
    reason: Union[Unset, SandboxMemoryOperationReason] = UNSET

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        operation_id = self.operation_id

        checkpoint_id = self.checkpoint_id

        action = self.action.value

        from_runtime_generation = self.from_runtime_generation

        lifecycle_epoch = self.lifecycle_epoch

        state = self.state.value

        current = self.current

        result_runtime_generation = self.result_runtime_generation

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "operation_id": operation_id,
                "checkpoint_id": checkpoint_id,
                "action": action,
                "from_runtime_generation": from_runtime_generation,
                "lifecycle_epoch": lifecycle_epoch,
                "state": state,
                "current": current,
            }
        )
        if result_runtime_generation is not UNSET:
            field_dict["result_runtime_generation"] = result_runtime_generation
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        operation_id = d.pop("operation_id")

        checkpoint_id = d.pop("checkpoint_id")

        action = SandboxMemoryOperationAction(d.pop("action"))

        from_runtime_generation = d.pop("from_runtime_generation")

        lifecycle_epoch = d.pop("lifecycle_epoch")

        state = SandboxMemoryOperationState(d.pop("state"))

        current = d.pop("current")

        result_runtime_generation = d.pop("result_runtime_generation", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, SandboxMemoryOperationReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = SandboxMemoryOperationReason(_reason)

        sandbox_memory_operation = cls(
            sandbox_id=sandbox_id,
            operation_id=operation_id,
            checkpoint_id=checkpoint_id,
            action=action,
            from_runtime_generation=from_runtime_generation,
            lifecycle_epoch=lifecycle_epoch,
            state=state,
            current=current,
            result_runtime_generation=result_runtime_generation,
            reason=reason,
        )

        return sandbox_memory_operation
