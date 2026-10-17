from __future__ import annotations

import re
from datetime import datetime

from typing import Any, List, Optional, TYPE_CHECKING, Union, TypeVar

from sandbox0.apispec.api.sandboxes import get_sandbox_health
from sandbox0.apispec.models.sandbox_health import SandboxHealth
from sandbox0.apispec.models.success_sandbox_health_response import SuccessSandboxHealthResponse
from sandbox0.apispec.models.sandbox_health_observation_source import SandboxHealthObservationSource
from sandbox0.apispec.models.sandbox_health_observation_state import SandboxHealthObservationState
from sandbox0.apispec.api.sandbox_rootfs import get_sandbox_root_fs_identity
from sandbox0.apispec.models.sandbox_root_fs_identity import SandboxRootFSIdentity
from sandbox0.apispec.models.success_sandbox_root_fs_identity_response import SuccessSandboxRootFSIdentityResponse
from sandbox0.apispec.api.sandboxes import delete_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_status
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_pause
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_refresh
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_resume
from sandbox0.apispec.api.sandboxes import restart_sandbox, get_sandbox_restart_operation, find_sandbox_restart_operation
from sandbox0.apispec.api.sandboxes import restore_sandbox_snapshot, get_sandbox_snapshot_restore_operation, find_sandbox_snapshot_restore_operation
from sandbox0.apispec.models.sandbox_snapshot_restore_request import SandboxSnapshotRestoreRequest
from sandbox0.apispec.models.sandbox_snapshot_restore_operation import SandboxSnapshotRestoreOperation
from sandbox0.apispec.models.success_sandbox_snapshot_restore_operation_response import SuccessSandboxSnapshotRestoreOperationResponse
from sandbox0.apispec.models.sandbox_restart_request import SandboxRestartRequest
from sandbox0.apispec.models.sandbox_restart_operation import SandboxRestartOperation
from sandbox0.apispec.models.success_sandbox_restart_operation_response import SuccessSandboxRestartOperationResponse
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id
from sandbox0.apispec.models.claim_request import ClaimRequest
from sandbox0.apispec.models.claim_response import ClaimResponse
from sandbox0.apispec.models.sandbox_refresh_request import SandboxRefreshRequest
from sandbox0.apispec.models.refresh_response import RefreshResponse
from sandbox0.apispec.models.resume_sandbox_response import ResumeSandboxResponse
from sandbox0.apispec.models.sandbox_execution_state_request import SandboxExecutionStateRequest
from sandbox0.apispec.models.sandbox_pause_request import SandboxPauseRequest
from sandbox0.apispec.models.pause_sandbox_response import PauseSandboxResponse
from sandbox0.apispec.models.sandbox import Sandbox as APISandbox
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_lifecycle_status import SandboxLifecycleStatus
from sandbox0.apispec.models.sandbox_resource_config import SandboxResourceConfig
from sandbox0.apispec.models.sandbox_status import SandboxStatus
from sandbox0.apispec.models.sandbox_summary import SandboxSummary
from sandbox0.apispec.models.sandbox_update_request import SandboxUpdateRequest
from sandbox0.apispec.models.success_claim_response import SuccessClaimResponse
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_pause_sandbox_response import SuccessPauseSandboxResponse
from sandbox0.apispec.models.success_refresh_response import SuccessRefreshResponse
from sandbox0.apispec.models.success_resume_sandbox_response import SuccessResumeSandboxResponse
from sandbox0.apispec.models.success_sandbox_list_response import SuccessSandboxListResponse
from sandbox0.apispec.models.success_sandbox_response import SuccessSandboxResponse
from sandbox0.apispec.models.success_sandbox_status_response import SuccessSandboxStatusResponse
from sandbox0.response import ensure_data, ensure_model
from sandbox0.apispec.types import UNSET

if TYPE_CHECKING:
    from sandbox0.client import Client
    from sandbox0.sandbox import Sandbox


class ClientSandboxesMixin:
    _api: Any

    def claim_sandbox(  # type: ignore[misc]
        self: "Client",
        template: str,
        config: Optional[SandboxConfig] = None,
        memory: Optional[str] = None,
    ) -> "Sandbox":
        if memory is not None:
            resources = SandboxResourceConfig(memory=memory)
            if config is None:
                config = SandboxConfig(resources=resources)
            else:
                config_data = config.to_dict()
                config_data["resources"] = resources.to_dict()
                config = SandboxConfig.from_dict(config_data)
        request = ClaimRequest(template=template, config=config) if config is not None else ClaimRequest(template=template)
        resp = post_api_v1_sandboxes.sync_detailed(client=self._api, body=request)
        data = ensure_data(resp, SuccessClaimResponse)
        from sandbox0.sandbox import Sandbox

        return Sandbox(
            id=data.sandbox_id,
            client=self,
            template=data.template,
            cluster_id=None if data.cluster_id.__class__.__name__ == "Unset" else data.cluster_id,
            runtime_id=data.runtime_id,
            status=data.status,
        )

    def get_sandbox_health(self: "Client", sandbox_id: str) -> SandboxHealth:  # type: ignore[misc]
        """Read independent observations; guest evidence is advisory. Never resumes or restarts."""
        if not isinstance(sandbox_id, str) or not sandbox_id or sandbox_id.strip() != sandbox_id:
            raise ValueError("invalid sandbox identity")
        response = get_sandbox_health.sync_detailed(id=sandbox_id, client=self._api)
        health = ensure_data(response, SuccessSandboxHealthResponse)
        if (health.sandbox_id != sandbox_id or
            any(type(value) is not int or value < 0 or value > 2**63-1 for value in
                (health.runtime_generation, health.lifecycle_epoch)) or
            type(health.active_lifecycle) is not bool or not _health_time_valid(health.observed_at)):
            raise ValueError("invalid sandbox health observation")
        for check in (health.runtime.launch_authority, health.runtime.liveness, health.execution,
                      health.terminal, health.storage.identity, health.storage.writer_authority, health.storage.io):
            if check.source == SandboxHealthObservationSource.NONE:
                if check.state != SandboxHealthObservationState.UNKNOWN or check.observed_at is not None:
                    raise ValueError("invalid unobserved sandbox health")
            elif not _health_time_valid(check.observed_at):
                raise ValueError("missing sandbox health observation time")
        return health

    def get_sandbox_rootfs_identity(self: "Client", sandbox_id: str) -> SandboxRootFSIdentity:  # type: ignore[misc]
        """Read external provenance without waking a guest; this is not a safety attestation."""
        if not isinstance(sandbox_id, str) or not sandbox_id or sandbox_id.strip() != sandbox_id:
            raise ValueError("invalid sandbox identity")
        response = get_sandbox_root_fs_identity.sync_detailed(id=sandbox_id, client=self._api)
        identity = ensure_data(response, SuccessSandboxRootFSIdentityResponse)
        if (identity.sandbox_id != sandbox_id or
            any(type(value) is not int or value < 0 or value > 2**63-1 for value in
                (identity.runtime_generation, identity.lifecycle_epoch, identity.writer_epoch, identity.managed_files_size_bytes)) or
            any(not isinstance(value, str) or not value for value in
                (identity.filesystem_id, identity.head_generation_id, identity.base_artifact_digest, identity.source_oci_digest)) or
            type(identity.has_imported_filesystem) is not bool or type(identity.active_lifecycle) is not bool):
            raise ValueError("invalid external RootFS identity")
        for digest in (identity.runtime_compatibility_digest, identity.retained_runtime_compatibility_digest):
            if digest is not UNSET and (
                not isinstance(digest, str) or re.fullmatch(r"sha256:[a-f0-9]{64}", digest) is None or
                identity.desired_state.value != "active" or identity.active_lifecycle or identity.runtime_generation <= 0
            ):
                raise ValueError("invalid external runtime compatibility")
        return identity

    def get_sandbox(self: "Client", sandbox_id: str) -> APISandbox:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._api)
        return ensure_data(resp, SuccessSandboxResponse)

    def update_sandbox(self: "Client", sandbox_id: str, request: SandboxUpdateRequest) -> APISandbox:  # type: ignore[misc]
        resp = put_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._api, body=request)
        return ensure_data(resp, SuccessSandboxResponse)

    def delete_sandbox(self: "Client", sandbox_id: str) -> SuccessMessageResponse:  # type: ignore[misc]
        resp = delete_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._api)
        return ensure_model(resp, SuccessMessageResponse)

    def status_sandbox(self: "Client", sandbox_id: str) -> SandboxStatus:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_status.sync_detailed(id=sandbox_id, client=self._api)
        return ensure_data(resp, SuccessSandboxStatusResponse)

    def restore_sandbox_snapshot(self: "Client", sandbox_id: str, *, expected_runtime_generation: int, snapshot_id: str, snapshot_generation_id: str, discard_process_state: bool, idempotency_key: str) -> SandboxSnapshotRestoreOperation:  # type: ignore[misc]
        """Restore the selected snapshot and end processes; retain all inputs after uncertainty."""
        _validate_restart_generation(expected_runtime_generation)
        if not 0 < expected_runtime_generation < 9007199254740991 or discard_process_state is not True:
            raise ValueError("explicit process discard and safe source generation required")
        _validate_snapshot_restore_identity(snapshot_id)
        _validate_snapshot_restore_identity(snapshot_generation_id)
        _validate_restart_key(idempotency_key)
        response = restore_sandbox_snapshot.sync_detailed(id=sandbox_id, client=self._api,
            body=SandboxSnapshotRestoreRequest(expected_runtime_generation=expected_runtime_generation, snapshot_id=snapshot_id, snapshot_generation_id=snapshot_generation_id, discard_process_state=discard_process_state), idempotency_key=idempotency_key)
        operation = _validate_snapshot_restore_receipt(ensure_data(response, SuccessSandboxSnapshotRestoreOperationResponse), sandbox_id)
        if operation.request_key != idempotency_key or operation.from_runtime_generation != expected_runtime_generation or operation.snapshot_id != snapshot_id or operation.snapshot_generation_id != snapshot_generation_id:
            raise ValueError("snapshot restore receipt does not match request")
        return operation

    def get_sandbox_snapshot_restore_operation(self: "Client", sandbox_id: str, operation_id: str) -> SandboxSnapshotRestoreOperation:  # type: ignore[misc]
        """Read a historical receipt independently of guest health."""
        if not _RESTART_ID.fullmatch(operation_id):
            raise ValueError("invalid snapshot restore operation ID")
        response = get_sandbox_snapshot_restore_operation.sync_detailed(id=sandbox_id, operation_id=operation_id, client=self._api)
        operation = _validate_snapshot_restore_receipt(ensure_data(response, SuccessSandboxSnapshotRestoreOperationResponse), sandbox_id)
        if operation.id != operation_id:
            raise ValueError("snapshot restore receipt does not match operation")
        return operation

    def find_sandbox_snapshot_restore_operation(self: "Client", sandbox_id: str, request_key: str) -> SandboxSnapshotRestoreOperation:  # type: ignore[misc]
        """Recover a lost acknowledgement without submitting a mutation."""
        _validate_restart_key(request_key)
        response = find_sandbox_snapshot_restore_operation.sync_detailed(id=sandbox_id, request_key=request_key, client=self._api)
        operation = _validate_snapshot_restore_receipt(ensure_data(response, SuccessSandboxSnapshotRestoreOperationResponse), sandbox_id)
        if operation.request_key != request_key:
            raise ValueError("snapshot restore receipt does not match request key")
        return operation

    def restart_sandbox(self: "Client", sandbox_id: str, *, expected_runtime_generation: int, idempotency_key: str) -> SandboxRestartOperation:  # type: ignore[misc]
        """Explicitly end processes. Reuse both inputs after an uncertain response."""
        _validate_restart_generation(expected_runtime_generation)
        _validate_restart_key(idempotency_key)
        response = restart_sandbox.sync_detailed(id=sandbox_id, client=self._api,
            body=SandboxRestartRequest(expected_runtime_generation=expected_runtime_generation), idempotency_key=idempotency_key)
        operation = _validate_restart_receipt(ensure_data(response, SuccessSandboxRestartOperationResponse), sandbox_id)
        if operation.request_key != idempotency_key or operation.from_runtime_generation != expected_runtime_generation:
            raise ValueError("restart receipt does not match request")
        return operation

    def get_sandbox_restart_operation(self: "Client", sandbox_id: str, operation_id: str) -> SandboxRestartOperation:  # type: ignore[misc]
        """Read a historical receipt independently of guest health."""
        if not _RESTART_ID.fullmatch(operation_id):
            raise ValueError("invalid restart operation ID")
        response = get_sandbox_restart_operation.sync_detailed(id=sandbox_id, operation_id=operation_id, client=self._api)
        operation = _validate_restart_receipt(ensure_data(response, SuccessSandboxRestartOperationResponse), sandbox_id)
        if operation.id != operation_id:
            raise ValueError("restart receipt does not match operation")
        return operation

    def find_sandbox_restart_operation(self: "Client", sandbox_id: str, request_key: str) -> SandboxRestartOperation:  # type: ignore[misc]
        """Recover a lost acknowledgement without submitting a mutation."""
        _validate_restart_key(request_key)
        response = find_sandbox_restart_operation.sync_detailed(id=sandbox_id, request_key=request_key, client=self._api)
        operation = _validate_restart_receipt(ensure_data(response, SuccessSandboxRestartOperationResponse), sandbox_id)
        if operation.request_key != request_key:
            raise ValueError("restart receipt does not match request key")
        return operation

    def pause_sandbox(self: "Client", sandbox_id: str, *, memory: bool = False) -> PauseSandboxResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_pause.sync_detailed(id=sandbox_id, client=self._api, body=SandboxPauseRequest(memory=memory))
        return ensure_data(resp, SuccessPauseSandboxResponse)

    def pause_sandbox_memory_for_operation(self: "Client", sandbox_id: str, *, expected_runtime_generation: int, idempotency_key: str) -> PauseSandboxResponse:  # type: ignore[misc]
        """Bind memory pause to one generation; retain both inputs after an uncertain reply."""
        if (type(expected_runtime_generation) is not int or not 0 < expected_runtime_generation <= 9007199254740991
                or not isinstance(idempotency_key, str) or not re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", idempotency_key)):
            raise ValueError("invalid conditional memory pause generation or idempotency key")
        response = post_api_v1_sandboxes_id_pause.sync_detailed(id=sandbox_id, client=self._api,
            idempotency_key=idempotency_key, body=SandboxPauseRequest(memory=True, expected_runtime_generation=expected_runtime_generation))
        result = ensure_data(response, SuccessPauseSandboxResponse)
        if (result.sandbox_id != sandbox_id or type(result.runtime_generation) is not int or result.runtime_generation != expected_runtime_generation
                or not isinstance(result.operation_id, str) or not re.fullmatch(r"idem-[a-f0-9]{64}", result.operation_id)
                or type(result.paused) is not bool):
            raise ValueError("conditional memory pause response does not match request")
        return result

    def resume_sandbox(self: "Client", sandbox_id: str, *, memory: bool = False) -> ResumeSandboxResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_resume.sync_detailed(id=sandbox_id, client=self._api, body=SandboxExecutionStateRequest(memory=memory))
        return ensure_data(resp, SuccessResumeSandboxResponse)

    def resume_sandbox_memory_for_operation(self: "Client", sandbox_id: str, *, expected_runtime_generation: int, checkpoint_id: str, idempotency_key: str) -> ResumeSandboxResponse:  # type: ignore[misc]
        """Restore one retained checkpoint; retain all inputs after an uncertain reply."""
        if (type(expected_runtime_generation) is not int or not 0 <= expected_runtime_generation < 9007199254740991
                or not isinstance(checkpoint_id, str) or not re.fullmatch(r"[!-~]{1,256}", checkpoint_id)
                or not isinstance(idempotency_key, str) or not re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", idempotency_key)):
            raise ValueError("invalid conditional memory resume generation, checkpoint or idempotency key")
        response = post_api_v1_sandboxes_id_resume.sync_detailed(id=sandbox_id, client=self._api, idempotency_key=idempotency_key,
            body=SandboxExecutionStateRequest(memory=True, expected_runtime_generation=expected_runtime_generation, checkpoint_id=checkpoint_id))
        result = ensure_data(response, SuccessResumeSandboxResponse)
        if (result.sandbox_id != sandbox_id or result.resumed is not True or result.checkpoint_id != checkpoint_id
                or type(result.from_runtime_generation) is not int or result.from_runtime_generation != expected_runtime_generation
                or type(result.runtime_generation) is not int or result.runtime_generation != expected_runtime_generation + 1
                or not isinstance(result.operation_id, str) or not re.fullmatch(r"idem-[a-f0-9]{64}", result.operation_id)):
            raise ValueError("conditional memory resume response does not match request")
        return result

    def refresh_sandbox(self: "Client", sandbox_id: str, request: Optional[SandboxRefreshRequest] = None) -> RefreshResponse:  # type: ignore[misc]
        body = request if request is not None else SandboxRefreshRequest()
        resp = post_api_v1_sandboxes_id_refresh.sync_detailed(id=sandbox_id, client=self._api, body=body)
        return ensure_data(resp, SuccessRefreshResponse)

    def list_sandboxes(  # type: ignore[misc]
        self: "Client",
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
            client=self._api,
            status=status_enum,
            template_id=template_id,
            paused=paused,
            limit=limit,
            offset=offset,
        )
        data = ensure_data(resp, SuccessSandboxListResponse)
        return data.sandboxes

_RESTART_ID = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")

def _validate_restart_key(key: str) -> None:
    if not isinstance(key, str) or not re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", key):
        raise ValueError("invalid restart request key")

def _validate_restart_generation(generation: int) -> None:
    if type(generation) is not int or generation < 0 or generation >= 2**63 - 1:
        raise ValueError("invalid restart generation")

_RecoveryOperation = TypeVar("_RecoveryOperation", SandboxRestartOperation, SandboxSnapshotRestoreOperation)

def _validate_restart_receipt(operation: _RecoveryOperation, sandbox_id: str) -> _RecoveryOperation:
    _validate_restart_generation(operation.from_runtime_generation)
    _validate_restart_key(operation.request_key)
    if operation.sandbox_id != sandbox_id or not _RESTART_ID.fullmatch(operation.id):
        raise ValueError("invalid restart receipt")
    if operation.state == "succeeded":
        if type(operation.result_runtime_generation) is not int or operation.result_runtime_generation != operation.from_runtime_generation + 1:
            raise ValueError("invalid restart result generation")
    elif operation.result_runtime_generation is not UNSET:
        raise ValueError("uncommitted restart result generation")
    return operation


def _health_time_valid(value: object) -> bool:
    return isinstance(value, datetime) and value.tzinfo is not None and value.utcoffset() is not None


def _validate_snapshot_restore_identity(value: object) -> None:
    if not isinstance(value, str) or not value or value.strip() != value or len(value.encode("utf-8")) > 512 or "\0" in value:
        raise ValueError("invalid snapshot identity")


def _validate_snapshot_restore_receipt(operation: SandboxSnapshotRestoreOperation, sandbox_id: str) -> SandboxSnapshotRestoreOperation:
    _validate_restart_receipt(operation, sandbox_id)
    _validate_snapshot_restore_identity(operation.snapshot_id)
    _validate_snapshot_restore_identity(operation.snapshot_generation_id)
    if operation.discard_process_state is not True or not 0 < operation.from_runtime_generation < 9007199254740991:
        raise ValueError("invalid snapshot restore receipt")
    if operation.restored_rootfs_generation_id is not UNSET:
        _validate_snapshot_restore_identity(operation.restored_rootfs_generation_id)
    if operation.state in ("resuming", "succeeded") and not isinstance(operation.restored_rootfs_generation_id, str):
        raise ValueError("restored head receipt missing")
    return operation
