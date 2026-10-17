import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sandbox_root_fs_fork_launch_lifecycle_epoch import (
    SandboxRootFSForkLaunchLifecycleEpoch,
)
from ..models.sandbox_root_fs_fork_launch_runtime_generation import (
    SandboxRootFSForkLaunchRuntimeGeneration,
)
from ..models.sandbox_root_fs_fork_launch_state import SandboxRootFSForkLaunchState
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxRootFSForkLaunch")


@_attrs_define
class SandboxRootFSForkLaunch:
    """
    Attributes:
        operation_id (str):
        sandbox_id (str):
        fork_operation_id (str):
        filesystem_id (str):
        head_generation_id (str):
        writer_epoch (int): Original pre-admission writer epoch, not a current writer lease
        lifecycle_epoch (SandboxRootFSForkLaunchLifecycleEpoch):
        runtime_generation (SandboxRootFSForkLaunchRuntimeGeneration): Zero while pending or aborted; one when completed
        state (SandboxRootFSForkLaunchState):
        current (bool):
        launch_digest (Union[Unset, str]): Present only for completed history; digest of retained external launch proof
        completed_at (Union[Unset, datetime.datetime]): Present only for completed history
    """

    operation_id: str
    sandbox_id: str
    fork_operation_id: str
    filesystem_id: str
    head_generation_id: str
    writer_epoch: int
    lifecycle_epoch: SandboxRootFSForkLaunchLifecycleEpoch
    runtime_generation: SandboxRootFSForkLaunchRuntimeGeneration
    state: SandboxRootFSForkLaunchState
    current: bool
    launch_digest: Union[Unset, str] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        sandbox_id = self.sandbox_id

        fork_operation_id = self.fork_operation_id

        filesystem_id = self.filesystem_id

        head_generation_id = self.head_generation_id

        writer_epoch = self.writer_epoch

        lifecycle_epoch = self.lifecycle_epoch.value

        runtime_generation = self.runtime_generation.value

        state = self.state.value

        current = self.current

        launch_digest = self.launch_digest

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operation_id": operation_id,
                "sandbox_id": sandbox_id,
                "fork_operation_id": fork_operation_id,
                "filesystem_id": filesystem_id,
                "head_generation_id": head_generation_id,
                "writer_epoch": writer_epoch,
                "lifecycle_epoch": lifecycle_epoch,
                "runtime_generation": runtime_generation,
                "state": state,
                "current": current,
            }
        )
        if launch_digest is not UNSET:
            field_dict["launch_digest"] = launch_digest
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        sandbox_id = d.pop("sandbox_id")

        fork_operation_id = d.pop("fork_operation_id")

        filesystem_id = d.pop("filesystem_id")

        head_generation_id = d.pop("head_generation_id")

        writer_epoch = d.pop("writer_epoch")

        lifecycle_epoch = SandboxRootFSForkLaunchLifecycleEpoch(
            d.pop("lifecycle_epoch")
        )

        runtime_generation = SandboxRootFSForkLaunchRuntimeGeneration(
            d.pop("runtime_generation")
        )

        state = SandboxRootFSForkLaunchState(d.pop("state"))

        current = d.pop("current")

        launch_digest = d.pop("launch_digest", UNSET)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        sandbox_root_fs_fork_launch = cls(
            operation_id=operation_id,
            sandbox_id=sandbox_id,
            fork_operation_id=fork_operation_id,
            filesystem_id=filesystem_id,
            head_generation_id=head_generation_id,
            writer_epoch=writer_epoch,
            lifecycle_epoch=lifecycle_epoch,
            runtime_generation=runtime_generation,
            state=state,
            current=current,
            launch_digest=launch_digest,
            completed_at=completed_at,
        )

        return sandbox_root_fs_fork_launch
