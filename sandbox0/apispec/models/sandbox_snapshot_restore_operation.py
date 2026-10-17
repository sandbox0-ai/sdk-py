import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sandbox_snapshot_restore_operation_reason import (
    SandboxSnapshotRestoreOperationReason,
)
from ..models.sandbox_snapshot_restore_operation_state import (
    SandboxSnapshotRestoreOperationState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_restart_retry_observation import (
        SandboxRestartRetryObservation,
    )


T = TypeVar("T", bound="SandboxSnapshotRestoreOperation")


@_attrs_define
class SandboxSnapshotRestoreOperation:
    """
    Attributes:
        snapshot_id (str): Immutable snapshot selected when the operation was admitted; it may since have expired or
            been deleted.
        snapshot_generation_id (str): Exact snapshot generation fixed at admission.
        discard_process_state (bool):
        id (str):
        sandbox_id (str):
        request_key (str):
        from_runtime_generation (int):
        state (SandboxSnapshotRestoreOperationState): Paused means an admitted paused source awaiting resume; only
            succeeded proves replacement. Failed and superseded are terminal and are never replayed.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        restored_rootfs_generation_id (Union[Unset, str]): Present after the head replacement and cold resume child
            commit together. This alone does not prove the new runtime launched.
        result_runtime_generation (Union[Unset, int]): Present only after committed replacement, even if a later
            lifecycle changes the current runtime.
        reason (Union[Unset, SandboxSnapshotRestoreOperationReason]):
        finished_at (Union[Unset, datetime.datetime]):
        retry (Union[Unset, SandboxRestartRetryObservation]):
    """

    snapshot_id: str
    snapshot_generation_id: str
    discard_process_state: bool
    id: str
    sandbox_id: str
    request_key: str
    from_runtime_generation: int
    state: SandboxSnapshotRestoreOperationState
    created_at: datetime.datetime
    updated_at: datetime.datetime
    restored_rootfs_generation_id: Union[Unset, str] = UNSET
    result_runtime_generation: Union[Unset, int] = UNSET
    reason: Union[Unset, SandboxSnapshotRestoreOperationReason] = UNSET
    finished_at: Union[Unset, datetime.datetime] = UNSET
    retry: Union[Unset, "SandboxRestartRetryObservation"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        snapshot_generation_id = self.snapshot_generation_id

        discard_process_state = self.discard_process_state

        id = self.id

        sandbox_id = self.sandbox_id

        request_key = self.request_key

        from_runtime_generation = self.from_runtime_generation

        state = self.state.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        restored_rootfs_generation_id = self.restored_rootfs_generation_id

        result_runtime_generation = self.result_runtime_generation

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        finished_at: Union[Unset, str] = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        retry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "snapshot_id": snapshot_id,
                "snapshot_generation_id": snapshot_generation_id,
                "discard_process_state": discard_process_state,
                "id": id,
                "sandbox_id": sandbox_id,
                "request_key": request_key,
                "from_runtime_generation": from_runtime_generation,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if restored_rootfs_generation_id is not UNSET:
            field_dict["restored_rootfs_generation_id"] = restored_rootfs_generation_id
        if result_runtime_generation is not UNSET:
            field_dict["result_runtime_generation"] = result_runtime_generation
        if reason is not UNSET:
            field_dict["reason"] = reason
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_restart_retry_observation import (
            SandboxRestartRetryObservation,
        )

        d = dict(src_dict)
        snapshot_id = d.pop("snapshot_id")

        snapshot_generation_id = d.pop("snapshot_generation_id")

        discard_process_state = d.pop("discard_process_state")

        id = d.pop("id")

        sandbox_id = d.pop("sandbox_id")

        request_key = d.pop("request_key")

        from_runtime_generation = d.pop("from_runtime_generation")

        state = SandboxSnapshotRestoreOperationState(d.pop("state"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        restored_rootfs_generation_id = d.pop("restored_rootfs_generation_id", UNSET)

        result_runtime_generation = d.pop("result_runtime_generation", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, SandboxSnapshotRestoreOperationReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = SandboxSnapshotRestoreOperationReason(_reason)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: Union[Unset, datetime.datetime]
        if isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)

        _retry = d.pop("retry", UNSET)
        retry: Union[Unset, SandboxRestartRetryObservation]
        if isinstance(_retry, Unset):
            retry = UNSET
        else:
            retry = SandboxRestartRetryObservation.from_dict(_retry)

        sandbox_snapshot_restore_operation = cls(
            snapshot_id=snapshot_id,
            snapshot_generation_id=snapshot_generation_id,
            discard_process_state=discard_process_state,
            id=id,
            sandbox_id=sandbox_id,
            request_key=request_key,
            from_runtime_generation=from_runtime_generation,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            restored_rootfs_generation_id=restored_rootfs_generation_id,
            result_runtime_generation=result_runtime_generation,
            reason=reason,
            finished_at=finished_at,
            retry=retry,
        )

        return sandbox_snapshot_restore_operation
