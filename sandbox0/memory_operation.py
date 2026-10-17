from __future__ import annotations

import re
from typing import Optional, TYPE_CHECKING

from sandbox0.apispec.api.sandboxes import lookup_sandbox_memory_operation
from sandbox0.apispec.models.lookup_sandbox_memory_operation_action import LookupSandboxMemoryOperationAction
from sandbox0.apispec.models.sandbox_memory_operation import SandboxMemoryOperation
from sandbox0.apispec.models.success_sandbox_memory_operation_response import SuccessSandboxMemoryOperationResponse
from sandbox0.apispec.types import UNSET
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.client import Client


class ClientMemoryOperationMixin:
    def lookup_sandbox_memory_operation(  # type: ignore[misc]
        self: "Client", sandbox_id: str, *, action: str, expected_runtime_generation: int,
        idempotency_key: str, checkpoint_id: Optional[str] = None, expected_operation_id: Optional[str] = None,
    ) -> SandboxMemoryOperation:
        """Read the original request; no dispatch, retry, or health inference. Current is only a snapshot."""
        resume = action == "resume"
        if (not isinstance(sandbox_id, str) or not sandbox_id or sandbox_id.strip() != sandbox_id
                or action not in ("pause", "resume") or type(expected_runtime_generation) is not int
                or not 0 <= expected_runtime_generation <= 9007199254740991
                or (not resume and expected_runtime_generation == 0) or (resume and expected_runtime_generation == 9007199254740991)
                or not isinstance(idempotency_key, str) or not re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", idempotency_key)
                or (not resume and checkpoint_id is not None)
                or (resume and (not isinstance(checkpoint_id, str) or not re.fullmatch(r"[!-~]{1,256}", checkpoint_id)))
                or (expected_operation_id is not None and (not isinstance(expected_operation_id, str) or not re.fullmatch(r"idem-[a-f0-9]{64}", expected_operation_id)))):
            raise ValueError("invalid memory operation lookup request")
        response = lookup_sandbox_memory_operation.sync_detailed(id=sandbox_id, client=self._api,
            action=LookupSandboxMemoryOperationAction(action), expected_runtime_generation=expected_runtime_generation,
            idempotency_key=idempotency_key, checkpoint_id=checkpoint_id if checkpoint_id is not None else UNSET)
        result = ensure_data(response, SuccessSandboxMemoryOperationResponse)
        if (result.sandbox_id != sandbox_id or result.action != action
                or type(result.from_runtime_generation) is not int or result.from_runtime_generation != expected_runtime_generation
                or not isinstance(result.operation_id, str) or not re.fullmatch(r"idem-[a-f0-9]{64}", result.operation_id)
                or (expected_operation_id is not None and result.operation_id != expected_operation_id)
                or result.checkpoint_id != (checkpoint_id if resume else result.operation_id)
                or type(result.lifecycle_epoch) is not int or not 0 < result.lifecycle_epoch <= 9007199254740991
                or type(result.current) is not bool):
            raise ValueError("memory operation observation does not match request")
        consumes_generation = resume and result.state in ("completed", "failed")
        if ((consumes_generation and (type(result.result_runtime_generation) is not int or result.result_runtime_generation != expected_runtime_generation + 1))
                or (not consumes_generation and result.result_runtime_generation is not UNSET)):
            raise ValueError("invalid memory operation result generation")
        valid = False
        if result.state == "pending":
            valid = not result.current and result.reason is UNSET
        elif result.state == "completed":
            valid = result.reason is UNSET
        elif result.state == "canceled":
            valid = result.reason == ("before_restore" if resume else "before_capture")
        elif result.state == "failed":
            valid = result.reason == ("restore_failed" if resume else "capture_failed") and (resume or not result.current)
        if not valid:
            raise ValueError("invalid memory operation terminal evidence")
        return result
