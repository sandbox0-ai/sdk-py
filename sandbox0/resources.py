from __future__ import annotations

import time
import re
from typing import Any, Callable, List, Optional, TYPE_CHECKING, Union

from sandbox0.apispec.api.sandboxes import delete_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_status
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_pause
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_refresh
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_resume
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id
from sandbox0.apispec.api.sandbox_rootfs import (
    delete_api_v1_sandbox_rootfs_snapshots_snapshot_id,
)
from sandbox0.apispec.api.sandbox_rootfs import (
    get_api_v1_sandbox_rootfs_snapshots_snapshot_id,
)
from sandbox0.apispec.api.sandbox_rootfs import get_api_v1_sandboxes_id_snapshots
from sandbox0.apispec.api.sandbox_rootfs import get_sandbox_root_fs_fork
from sandbox0.apispec.api.sandbox_rootfs import launch_sandbox_root_fs_fork, get_sandbox_root_fs_fork_launch
from sandbox0.apispec.models.sandbox_root_fs_fork_launch import SandboxRootFSForkLaunch
from sandbox0.apispec.models.sandbox_root_fs_fork_launch_request import SandboxRootFSForkLaunchRequest
from sandbox0.apispec.models.success_sandbox_root_fs_fork_launch_response import SuccessSandboxRootFSForkLaunchResponse
from sandbox0.fork_launch import validate_input as validate_fork_launch_input, validate_receipt as validate_fork_launch_receipt
from sandbox0.apispec.models.sandbox_root_fs_fork_observation import SandboxRootFSForkObservation
from sandbox0.apispec.models.success_sandbox_root_fs_fork_observation_response import SuccessSandboxRootFSForkObservationResponse
from sandbox0.apispec.api.sandbox_rootfs import post_api_v1_sandboxes_id_fork
from sandbox0.apispec.api.sandbox_rootfs import post_api_v1_sandboxes_id_rootfs_restore
from sandbox0.apispec.api.sandbox_rootfs import post_api_v1_sandboxes_id_snapshots
from sandbox0.apispec.api.sandbox_rootfs import capture_sandbox_root_fs_snapshot, get_captured_sandbox_root_fs_snapshot
from sandbox0.apispec.models.capture_sandbox_root_fs_snapshot_request import CaptureSandboxRootFSSnapshotRequest
from sandbox0.apispec.api.sandbox_rootfs import put_api_v1_sandboxes_id_rootfs_rebase
from sandbox0.apispec.models.claim_request import ClaimRequest
from sandbox0.apispec.models.create_sandbox_root_fs_snapshot_request import (
    CreateSandboxRootFSSnapshotRequest,
)
from sandbox0.apispec.models.fork_sandbox_request import ForkSandboxRequest
from sandbox0.apispec.models.fork_sandbox_response import ForkSandboxResponse
from sandbox0.apispec.models.sandbox_execution_state_request import SandboxExecutionStateRequest
from sandbox0.apispec.models.sandbox_pause_request import SandboxPauseRequest
from sandbox0.apispec.models.pause_sandbox_response import PauseSandboxResponse
from sandbox0.apispec.models.sandbox_snapshot_restore_operation import SandboxSnapshotRestoreOperation
from sandbox0.apispec.models.sandbox_restart_operation import SandboxRestartOperation
from sandbox0.apispec.models.sandbox_restart_final_capture import SandboxRestartFinalCapture
from sandbox0.apispec.models.sandbox_memory_restoration import SandboxMemoryRestoration
from sandbox0.apispec.models.sandbox_memory_operation import SandboxMemoryOperation
from sandbox0.restart_final_capture import RestartFinalCaptureFile
from sandbox0.apispec.models.sandbox_root_fs_identity import SandboxRootFSIdentity
from sandbox0.apispec.models.sandbox_health import SandboxHealth
from sandbox0.apispec.models.rebase_sandbox_root_fs_request import (
    RebaseSandboxRootFSRequest,
)
from sandbox0.apispec.models.rebase_sandbox_root_fs_response import (
    RebaseSandboxRootFSResponse,
)
from sandbox0.apispec.models.sandbox_refresh_request import SandboxRefreshRequest
from sandbox0.apispec.models.refresh_response import RefreshResponse
from sandbox0.apispec.models.restore_sandbox_root_fs_request import (
    RestoreSandboxRootFSRequest,
)
from sandbox0.apispec.models.restore_sandbox_root_fs_response import (
    RestoreSandboxRootFSResponse,
)
from sandbox0.apispec.models.resume_sandbox_response import ResumeSandboxResponse
from sandbox0.apispec.models.sandbox import Sandbox as APISandbox
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_lifecycle_status import SandboxLifecycleStatus
from sandbox0.apispec.models.sandbox_resource_config import SandboxResourceConfig
from sandbox0.apispec.models.sandbox_root_fs_snapshot import SandboxRootFSSnapshot
from sandbox0.apispec.models.sandbox_status import SandboxStatus
from sandbox0.apispec.models.sandbox_summary import SandboxSummary
from sandbox0.apispec.models.sandbox_update_request import SandboxUpdateRequest
from sandbox0.apispec.models.success_claim_response import SuccessClaimResponse
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_pause_sandbox_response import (
    SuccessPauseSandboxResponse,
)
from sandbox0.apispec.models.success_rebase_sandbox_root_fs_response import (
    SuccessRebaseSandboxRootFSResponse,
)
from sandbox0.apispec.models.success_fork_sandbox_response import (
    SuccessForkSandboxResponse,
)
from sandbox0.apispec.models.success_refresh_response import SuccessRefreshResponse
from sandbox0.apispec.models.success_restore_sandbox_root_fs_response import (
    SuccessRestoreSandboxRootFSResponse,
)
from sandbox0.apispec.models.success_resume_sandbox_response import (
    SuccessResumeSandboxResponse,
)
from sandbox0.apispec.models.success_sandbox_root_fs_snapshot_list_response import (
    SuccessSandboxRootFSSnapshotListResponse,
)
from sandbox0.apispec.models.success_sandbox_root_fs_snapshot_response import (
    SuccessSandboxRootFSSnapshotResponse,
)
from sandbox0.apispec.models.success_sandbox_list_response import (
    SuccessSandboxListResponse,
)
from sandbox0.apispec.models.success_sandbox_response import SuccessSandboxResponse
from sandbox0.apispec.models.success_sandbox_status_response import (
    SuccessSandboxStatusResponse,
)
from sandbox0.apispec.types import UNSET, Unset
from sandbox0.response import ensure_data, ensure_model
from sandbox0.errors import SandboxWaitTimeoutError, SandboxLifecycleFailedError
from sandbox0.sessions import SandboxSession

if TYPE_CHECKING:
    from sandbox0.client import Client
    from sandbox0.sandbox import Sandbox


def _sandbox_config_with_memory(config: Optional[SandboxConfig], memory: Optional[str]) -> Optional[SandboxConfig]:
    if memory is None:
        return config
    resources = SandboxResourceConfig(memory=memory)
    if config is None:
        return SandboxConfig(resources=resources)
    data = config.to_dict()
    data["resources"] = resources.to_dict()
    return SandboxConfig.from_dict(data)


class Sandboxes:
    def __init__(self, client: "Client") -> None:
        self._client = client

    def claim(
        self,
        template: str,
        config: Optional[SandboxConfig] = None,
        snapshot_id: Optional[str] = None,
        memory: Optional[str] = None,
    ) -> "Sandbox":
        request = ClaimRequest(template=template)
        config = _sandbox_config_with_memory(config, memory)
        if config is not None:
            request.config = config
        if snapshot_id is not None:
            request.snapshot_id = snapshot_id
        resp = post_api_v1_sandboxes.sync_detailed(client=self._client.api, body=request)
        data = ensure_data(resp, SuccessClaimResponse)
        from sandbox0.sandbox import Sandbox

        return Sandbox(
            id=data.sandbox_id,
            client=self._client,
            template=data.template,
            cluster_id=None if data.cluster_id.__class__.__name__ == "Unset" else data.cluster_id,
            runtime_id=data.runtime_id,
            status=data.status,
        )

    def open(
        self,
        template: str,
        config: Optional[SandboxConfig] = None,
        snapshot_id: Optional[str] = None,
        memory: Optional[str] = None,
    ) -> SandboxSession:
        sandbox = self.claim(
            template,
            config=config,
            snapshot_id=snapshot_id,
            memory=memory,
        )
        return SandboxSession(sandbox, closer=lambda: None if self.delete(sandbox.id) else None)

    def get(self, sandbox_id: str) -> APISandbox:
        resp = get_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxResponse)

    def wait_for_lifecycle(
        self,
        sandbox_id: str,
        predicate: Callable[[APISandbox], bool],
        *,
        timeout_sec: float = 60.0,
        poll_interval_sec: float = 0.5,
    ) -> APISandbox:
        """Poll committed sandbox details until ``predicate`` matches."""
        if timeout_sec < 0:
            raise ValueError("timeout_sec cannot be negative")
        if poll_interval_sec <= 0:
            raise ValueError("poll_interval_sec must be positive")

        started_at = time.monotonic()
        last_sandbox: Optional[APISandbox] = None
        while True:
            last_sandbox = self.get(sandbox_id)
            if predicate(last_sandbox):
                return last_sandbox

            remaining = timeout_sec - (time.monotonic() - started_at)
            if remaining <= 0:
                raise SandboxWaitTimeoutError(
                    sandbox_id=sandbox_id,
                    timeout_sec=timeout_sec,
                    last_sandbox=last_sandbox,
                )
            time.sleep(min(poll_interval_sec, remaining))

    def update(self, sandbox_id: str, request: SandboxUpdateRequest) -> APISandbox:
        resp = put_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api, body=request)
        return ensure_data(resp, SuccessSandboxResponse)

    def delete(self, sandbox_id: str) -> SuccessMessageResponse:
        resp = delete_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_model(resp, SuccessMessageResponse)

    def status(self, sandbox_id: str) -> SandboxStatus:
        resp = get_api_v1_sandboxes_id_status.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxStatusResponse)

    def get_health(self, sandbox_id: str) -> SandboxHealth:
        return self._client.get_sandbox_health(sandbox_id)

    def lookup_memory_operation(self, sandbox_id: str, *, action: str, expected_runtime_generation: int,
            idempotency_key: str, checkpoint_id: Optional[str] = None, expected_operation_id: Optional[str] = None) -> SandboxMemoryOperation:
        return self._client.lookup_sandbox_memory_operation(sandbox_id, action=action,
            expected_runtime_generation=expected_runtime_generation, idempotency_key=idempotency_key,
            checkpoint_id=checkpoint_id, expected_operation_id=expected_operation_id)

    def get_memory_restoration(self, sandbox_id: str, runtime_generation: int) -> SandboxMemoryRestoration:
        return self._client.get_sandbox_memory_restoration(sandbox_id, runtime_generation)

    def get_rootfs_identity(self, sandbox_id: str) -> SandboxRootFSIdentity:
        return self._client.get_sandbox_rootfs_identity(sandbox_id)

    def get_snapshot_restore_final_capture(self, sandbox_id: str, operation_id: str) -> SandboxRestartFinalCapture:
        return self._client.get_sandbox_snapshot_restore_final_capture(sandbox_id, operation_id)

    def read_snapshot_restore_final_capture_file(self, sandbox_id: str, operation_id: str, capture_id: str, namespace: str, name: str) -> RestartFinalCaptureFile:
        return self._client.read_sandbox_snapshot_restore_final_capture_file(sandbox_id, operation_id, capture_id, namespace, name)

    def acknowledge_snapshot_restore_final_capture(self, sandbox_id: str, operation_id: str, capture_id: str, receipt_id: str) -> SandboxRestartFinalCapture:
        return self._client.acknowledge_sandbox_snapshot_restore_final_capture(sandbox_id, operation_id, capture_id, receipt_id)

    def get_restart_final_capture(self, sandbox_id: str, operation_id: str) -> SandboxRestartFinalCapture:
        return self._client.get_sandbox_restart_final_capture(sandbox_id, operation_id)

    def read_restart_final_capture_file(self, sandbox_id: str, operation_id: str, capture_id: str, namespace: str, name: str) -> RestartFinalCaptureFile:
        return self._client.read_sandbox_restart_final_capture_file(sandbox_id, operation_id, capture_id, namespace, name)

    def acknowledge_restart_final_capture(self, sandbox_id: str, operation_id: str, capture_id: str, receipt_id: str) -> SandboxRestartFinalCapture:
        return self._client.acknowledge_sandbox_restart_final_capture(sandbox_id, operation_id, capture_id, receipt_id)

    def restore_snapshot(self, sandbox_id: str, *, expected_runtime_generation: int, snapshot_id: str, snapshot_generation_id: str, discard_process_state: bool, idempotency_key: str) -> SandboxSnapshotRestoreOperation:
        return self._client.restore_sandbox_snapshot(sandbox_id, expected_runtime_generation=expected_runtime_generation, snapshot_id=snapshot_id, snapshot_generation_id=snapshot_generation_id, discard_process_state=discard_process_state, idempotency_key=idempotency_key)

    def get_snapshot_restore_operation(self, sandbox_id: str, operation_id: str) -> SandboxSnapshotRestoreOperation:
        return self._client.get_sandbox_snapshot_restore_operation(sandbox_id, operation_id)

    def find_snapshot_restore_operation(self, sandbox_id: str, request_key: str) -> SandboxSnapshotRestoreOperation:
        return self._client.find_sandbox_snapshot_restore_operation(sandbox_id, request_key)

    def restart(self, sandbox_id: str, *, expected_runtime_generation: int, idempotency_key: str) -> SandboxRestartOperation:
        return self._client.restart_sandbox(sandbox_id, expected_runtime_generation=expected_runtime_generation, idempotency_key=idempotency_key)

    def get_restart_operation(self, sandbox_id: str, operation_id: str) -> SandboxRestartOperation:
        return self._client.get_sandbox_restart_operation(sandbox_id, operation_id)

    def find_restart_operation(self, sandbox_id: str, request_key: str) -> SandboxRestartOperation:
        return self._client.find_sandbox_restart_operation(sandbox_id, request_key)

    def pause(self, sandbox_id: str, *, memory: bool = False) -> PauseSandboxResponse:
        resp = post_api_v1_sandboxes_id_pause.sync_detailed(id=sandbox_id, client=self._client.api, body=SandboxPauseRequest(memory=memory))
        return ensure_data(resp, SuccessPauseSandboxResponse)

    def pause_memory_for_operation(self, sandbox_id: str, *, expected_runtime_generation: int, idempotency_key: str) -> PauseSandboxResponse:
        return self._client.pause_sandbox_memory_for_operation(sandbox_id, expected_runtime_generation=expected_runtime_generation, idempotency_key=idempotency_key)

    def pause_and_wait(
        self,
        sandbox_id: str,
        *,
        memory: bool = False,
        timeout_sec: float = 60.0,
        poll_interval_sec: float = 0.5,
    ) -> APISandbox:
        """Request a pause and wait for its durable checkpoint to commit."""
        self.pause(sandbox_id, memory=memory)
        sandbox = self.wait_for_lifecycle(
            sandbox_id,
            lambda sandbox: (sandbox.status == SandboxLifecycleStatus.PAUSED and sandbox.paused)
            or (memory and sandbox.status == SandboxLifecycleStatus.FAILED),
            timeout_sec=timeout_sec,
            poll_interval_sec=poll_interval_sec,
        )
        if memory and sandbox.status == SandboxLifecycleStatus.FAILED:
            raise SandboxLifecycleFailedError(sandbox_id, "memory pause", sandbox)
        return sandbox

    def resume(self, sandbox_id: str, *, memory: bool = False) -> ResumeSandboxResponse:
        resp = post_api_v1_sandboxes_id_resume.sync_detailed(id=sandbox_id, client=self._client.api, body=SandboxExecutionStateRequest(memory=memory))
        return ensure_data(resp, SuccessResumeSandboxResponse)

    def resume_memory_for_operation(self, sandbox_id: str, *, expected_runtime_generation: int, checkpoint_id: str, idempotency_key: str) -> ResumeSandboxResponse:
        return self._client.resume_sandbox_memory_for_operation(sandbox_id, expected_runtime_generation=expected_runtime_generation, checkpoint_id=checkpoint_id, idempotency_key=idempotency_key)

    def resume_and_wait(
        self,
        sandbox_id: str,
        *,
        memory: bool = False,
        timeout_sec: float = 60.0,
        poll_interval_sec: float = 0.5,
    ) -> APISandbox:
        """Request a resume and wait for the committed running generation."""
        before = self.get(sandbox_id)
        self.resume(sandbox_id, memory=memory)
        minimum_generation = before.runtime_generation
        if before.paused or before.status == SandboxLifecycleStatus.PAUSED:
            minimum_generation += 1
        sandbox = self.wait_for_lifecycle(
            sandbox_id,
            lambda sandbox: sandbox.runtime_generation >= minimum_generation and (
                (sandbox.status == SandboxLifecycleStatus.RUNNING and not sandbox.paused)
                or (memory and sandbox.status == SandboxLifecycleStatus.FAILED)
            ),
            timeout_sec=timeout_sec,
            poll_interval_sec=poll_interval_sec,
        )
        if memory and sandbox.status == SandboxLifecycleStatus.FAILED:
            raise SandboxLifecycleFailedError(sandbox_id, "memory resume", sandbox)
        return sandbox

    def refresh(self, sandbox_id: str, request: Optional[SandboxRefreshRequest] = None) -> RefreshResponse:
        body = request if request is not None else SandboxRefreshRequest()
        resp = post_api_v1_sandboxes_id_refresh.sync_detailed(id=sandbox_id, client=self._client.api, body=body)
        return ensure_data(resp, SuccessRefreshResponse)

    def create_rootfs_snapshot(
        self,
        sandbox_id: str,
        request: Optional[CreateSandboxRootFSSnapshotRequest] = None,
    ) -> SandboxRootFSSnapshot:
        body = request if request is not None else CreateSandboxRootFSSnapshotRequest()
        resp = post_api_v1_sandboxes_id_snapshots.sync_detailed(id=sandbox_id, client=self._client.api, body=body)
        return ensure_data(resp, SuccessSandboxRootFSSnapshotResponse)

    def capture_rootfs_snapshot(
        self, sandbox_id: str, request: CaptureSandboxRootFSSnapshotRequest, *, idempotency_key: str,
    ) -> SandboxRootFSSnapshot:
        """One conditional capture; retain the same key and metadata on uncertainty."""
        generation = request.expected_runtime_generation
        if (not sandbox_id or type(generation) is not int or not 1 <= generation <= 9007199254740991
                or not isinstance(idempotency_key, str) or re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", idempotency_key) is None):
            raise ValueError("conditional snapshot requires a source, positive safe generation and canonical key")
        response = capture_sandbox_root_fs_snapshot.sync_detailed(
            id=sandbox_id, client=self._client.api, body=request, idempotency_key=idempotency_key,
        )
        snapshot = ensure_data(response, SuccessSandboxRootFSSnapshotResponse)
        if not snapshot.id or snapshot.sandbox_id != sandbox_id:
            raise ValueError("conditional snapshot returned mismatched identity")
        return snapshot

    def get_captured_rootfs_snapshot(
        self, sandbox_id: str, *, expected_runtime_generation: int, idempotency_key: str,
    ) -> SandboxRootFSSnapshot:
        """Read only the original receipt; absent/pending outcomes never authorize replacement."""
        if (not sandbox_id or type(expected_runtime_generation) is not int or not 1 <= expected_runtime_generation <= 9007199254740991
                or not isinstance(idempotency_key, str) or re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", idempotency_key) is None):
            raise ValueError("snapshot observation requires a source, positive safe generation and canonical key")
        response = get_captured_sandbox_root_fs_snapshot.sync_detailed(
            id=sandbox_id, client=self._client.api, expected_runtime_generation=expected_runtime_generation, idempotency_key=idempotency_key,
        )
        snapshot = ensure_data(response, SuccessSandboxRootFSSnapshotResponse)
        if not snapshot.id or snapshot.sandbox_id != sandbox_id:
            raise ValueError("snapshot observation returned mismatched identity")
        return snapshot

    def get_rootfs_fork(
        self, sandbox_id: str, *, expected_runtime_generation: int, idempotency_key: str,
    ) -> SandboxRootFSForkObservation:
        """Read original fork provenance without retry, submission or state reservation."""
        if (not sandbox_id or type(expected_runtime_generation) is not int or not 0 <= expected_runtime_generation <= 9007199254740991
                or not isinstance(idempotency_key, str) or re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", idempotency_key) is None):
            raise ValueError("fork observation requires a source, nonnegative safe generation and canonical key")
        response = get_sandbox_root_fs_fork.sync_detailed(
            id=sandbox_id, client=self._client.api, expected_runtime_generation=expected_runtime_generation, idempotency_key=idempotency_key,
        )
        r = ensure_data(response, SuccessSandboxRootFSForkObservationResponse)
        if (r.source_sandbox_id != sandbox_id or type(r.source_runtime_generation) is not int or r.source_runtime_generation != expected_runtime_generation
                or r.target_sandbox_id == sandbox_id or r.target_filesystem_id != r.target_sandbox_id
                or any(not isinstance(v, str) or not v for v in [r.operation_id, r.target_sandbox_id, r.source_filesystem_id, r.source_head_generation_id, r.target_head_generation_id, r.base_artifact_digest, r.source_oci_digest])
                or type(r.writer_epoch) is not int or not 1 <= r.writer_epoch <= 9007199254740991
                or type(r.managed_files_size_bytes) is not int or not 0 <= r.managed_files_size_bytes <= 9007199254740991
                or type(r.auto_resume) is not bool or type(r.automatic_routes) is not bool):
            raise ValueError("fork observation returned mismatched identity")
        return r

    def launch_rootfs_fork(
        self, sandbox_id: str, *, fork_operation_id: str, filesystem_id: str, head_generation_id: str,
        writer_epoch: int, idempotency_key: str, expected_operation_id: Optional[str] = None,
    ) -> SandboxRootFSForkLaunch:
        """Submit one conditional first launch; never retry, wait or fall back to resume."""
        validate_fork_launch_input(sandbox_id, fork_operation_id, filesystem_id, head_generation_id, writer_epoch, idempotency_key, expected_operation_id)
        response = launch_sandbox_root_fs_fork.sync_detailed(
            id=sandbox_id, client=self._client.api, idempotency_key=idempotency_key,
            body=SandboxRootFSForkLaunchRequest(fork_operation_id=fork_operation_id, filesystem_id=filesystem_id, head_generation_id=head_generation_id, writer_epoch=writer_epoch),
        )
        r = validate_fork_launch_receipt(ensure_data(response, SuccessSandboxRootFSForkLaunchResponse), response.content,
                                        sandbox_id, fork_operation_id, filesystem_id, head_generation_id, writer_epoch, expected_operation_id)
        if response.status_code == 202 and r.state != "pending":
            raise ValueError("accepted fork launch returned terminal evidence")
        return r

    def get_rootfs_fork_launch(
        self, sandbox_id: str, *, fork_operation_id: str, filesystem_id: str, head_generation_id: str,
        writer_epoch: int, idempotency_key: str, expected_operation_id: Optional[str] = None,
    ) -> SandboxRootFSForkLaunch:
        """Read original launch history, including current=False, without submitting work."""
        validate_fork_launch_input(sandbox_id, fork_operation_id, filesystem_id, head_generation_id, writer_epoch, idempotency_key, expected_operation_id)
        response = get_sandbox_root_fs_fork_launch.sync_detailed(
            id=sandbox_id, client=self._client.api, idempotency_key=idempotency_key, fork_operation_id=fork_operation_id,
            filesystem_id=filesystem_id, head_generation_id=head_generation_id, writer_epoch=writer_epoch,
        )
        return validate_fork_launch_receipt(ensure_data(response, SuccessSandboxRootFSForkLaunchResponse), response.content,
                                           sandbox_id, fork_operation_id, filesystem_id, head_generation_id, writer_epoch, expected_operation_id)

    def list_rootfs_snapshots(self, sandbox_id: str) -> List[SandboxRootFSSnapshot]:
        resp = get_api_v1_sandboxes_id_snapshots.sync_detailed(id=sandbox_id, client=self._client.api)
        data = ensure_data(resp, SuccessSandboxRootFSSnapshotListResponse)
        return data.snapshots

    def get_rootfs_snapshot(self, snapshot_id: str) -> SandboxRootFSSnapshot:
        resp = get_api_v1_sandbox_rootfs_snapshots_snapshot_id.sync_detailed(
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_data(resp, SuccessSandboxRootFSSnapshotResponse)

    def delete_rootfs_snapshot(self, snapshot_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandbox_rootfs_snapshots_snapshot_id.sync_detailed(
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_model(resp, SuccessDeletedResponse)

    def restore_rootfs(
        self,
        sandbox_id: str,
        request: RestoreSandboxRootFSRequest,
    ) -> RestoreSandboxRootFSResponse:
        resp = post_api_v1_sandboxes_id_rootfs_restore.sync_detailed(
            id=sandbox_id,
            client=self._client.api,
            body=request,
        )
        return ensure_data(resp, SuccessRestoreSandboxRootFSResponse)

    def rebase_rootfs(
        self,
        sandbox_id: str,
        request: RebaseSandboxRootFSRequest,
    ) -> RebaseSandboxRootFSResponse:
        resp = put_api_v1_sandboxes_id_rootfs_rebase.sync_detailed(
            id=sandbox_id,
            client=self._client.api,
            body=request,
        )
        return ensure_data(resp, SuccessRebaseSandboxRootFSResponse)

    def fork(
        self,
        sandbox_id: str,
        request: Optional[ForkSandboxRequest] = None,
        *,
        idempotency_key: Optional[str] = None,
    ) -> ForkSandboxResponse:
        body = request if request is not None else ForkSandboxRequest()
        generation = body.expected_runtime_generation
        conditional = not isinstance(generation, Unset)
        if conditional and (type(generation) is not int or generation < 0 or generation > 9007199254740991 or (body.memory is True and generation == 9007199254740991)):
            raise ValueError("invalid expected runtime generation for fork")
        if (body.memory is True or conditional) and (not idempotency_key or not idempotency_key.strip() or len(idempotency_key.encode("utf-8")) > 255):
            raise ValueError("conditional or memory fork requires a stable idempotency_key of at most 255 bytes")
        resp = post_api_v1_sandboxes_id_fork.sync_detailed(
            id=sandbox_id,
            client=self._client.api,
            body=body,
            idempotency_key=idempotency_key if idempotency_key is not None else UNSET,
        )
        return ensure_data(resp, SuccessForkSandboxResponse)

    def list(
        self,
        *,
        status: Union[SandboxLifecycleStatus, str] = UNSET,  # type: ignore[assignment]
        template_id: str = UNSET,  # type: ignore[assignment]
        paused: bool = UNSET,  # type: ignore[assignment]
        limit: int = 50,
        offset: int = 0,
    ) -> List[SandboxSummary]:
        status_enum: Union[SandboxLifecycleStatus, Any] = UNSET
        if status != UNSET:
            if isinstance(status, str):
                status_enum = SandboxLifecycleStatus(status)
            else:
                status_enum = status
        resp = get_api_v1_sandboxes.sync_detailed(
            client=self._client.api,
            status=status_enum,
            template_id=template_id,
            paused=paused,
            limit=limit,
            offset=offset,
        )
        data = ensure_data(resp, SuccessSandboxListResponse)
        return data.sandboxes

    def sandbox(self, sandbox_id: str) -> "Sandbox":
        from sandbox0.sandbox import Sandbox

        return Sandbox(id=sandbox_id, client=self._client)
