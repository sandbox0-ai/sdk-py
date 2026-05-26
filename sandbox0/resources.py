from __future__ import annotations

from dataclasses import dataclass
from typing import Any, BinaryIO, List, Optional, TYPE_CHECKING, Union

from sandbox0.apispec.api.functions import delete_api_v1_functions_id
from sandbox0.apispec.api.functions import get_api_v1_functions
from sandbox0.apispec.api.functions import get_api_v1_functions_id
from sandbox0.apispec.api.functions import get_api_v1_functions_id_revisions
from sandbox0.apispec.api.functions import post_api_v1_functions_deploy
from sandbox0.apispec.api.functions import post_api_v1_functions_id_deploy
from sandbox0.apispec.api.functions import put_api_v1_functions_id
from sandbox0.apispec.api.functions import put_api_v1_functions_id_active_revision
from sandbox0.apispec.api.sandboxes import delete_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id
from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_status
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_pause
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_refresh
from sandbox0.apispec.api.sandboxes import post_api_v1_sandboxes_id_resume
from sandbox0.apispec.api.sandboxes import put_api_v1_sandboxes_id
from sandbox0.apispec.api.sandbox_volumes import delete_api_v1_sandboxvolumes_id
from sandbox0.apispec.api.sandbox_volumes import get_api_v1_sandboxvolumes
from sandbox0.apispec.api.sandbox_volumes import get_api_v1_sandboxvolumes_id
from sandbox0.apispec.api.sandbox_volumes import post_api_v1_sandboxvolumes_id_fork
from sandbox0.apispec.api.sandbox_volumes import post_api_v1_sandboxvolumes
from sandbox0.apispec.api.snapshots import delete_api_v1_sandboxvolumes_id_snapshots_snapshot_id
from sandbox0.apispec.api.snapshots import get_api_v1_sandboxvolumes_id_snapshots
from sandbox0.apispec.api.snapshots import get_api_v1_sandboxvolumes_id_snapshots_snapshot_id
from sandbox0.apispec.api.snapshots import post_api_v1_sandboxvolumes_id_snapshots
from sandbox0.apispec.api.snapshots import post_api_v1_sandboxvolumes_id_snapshots_snapshot_id_restore
from sandbox0.apispec.models.claim_mount_request import ClaimMountRequest
from sandbox0.apispec.models.claim_request import ClaimRequest
from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest
from sandbox0.apispec.models.create_snapshot_request import CreateSnapshotRequest
from sandbox0.apispec.models.file_info import FileInfo
from sandbox0.apispec.models.fork_volume_request import ForkVolumeRequest
from sandbox0.apispec.models.activate_function_revision_request import ActivateFunctionRevisionRequest
from sandbox0.apispec.models.function import Function as APIFunction
from sandbox0.apispec.models.function_deploy_request import FunctionDeployRequest
from sandbox0.apispec.models.function_deploy_result import FunctionDeployResult
from sandbox0.apispec.models.function_revision import FunctionRevision
from sandbox0.apispec.models.function_revision_mount import FunctionRevisionMount
from sandbox0.apispec.models.function_revision_spec import FunctionRevisionSpec
from sandbox0.apispec.models.function_revision_spec_env_vars import FunctionRevisionSpecEnvVars
from sandbox0.apispec.models.function_scale_policy import FunctionScalePolicy
from sandbox0.apispec.models.function_source import FunctionSource
from sandbox0.apispec.models.function_source_type import FunctionSourceType
from sandbox0.apispec.models.function_update_request import FunctionUpdateRequest
from sandbox0.apispec.models.pause_sandbox_response import PauseSandboxResponse
from sandbox0.apispec.models.sandbox_refresh_request import SandboxRefreshRequest
from sandbox0.apispec.models.mount_status import MountStatus
from sandbox0.apispec.models.refresh_response import RefreshResponse
from sandbox0.apispec.models.resume_sandbox_response import ResumeSandboxResponse
from sandbox0.apispec.models.sandbox import Sandbox as APISandbox
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_lifecycle_status import SandboxLifecycleStatus
from sandbox0.apispec.models.sandbox_status import SandboxStatus
from sandbox0.apispec.models.sandbox_summary import SandboxSummary
from sandbox0.apispec.models.sandbox_update_request import SandboxUpdateRequest
from sandbox0.apispec.models.sandbox_volume import SandboxVolume
from sandbox0.apispec.models.sandbox_app_service import SandboxAppService
from sandbox0.apispec.models.sandbox_app_service_health import SandboxAppServiceHealth
from sandbox0.apispec.models.sandbox_app_service_ingress import SandboxAppServiceIngress
from sandbox0.apispec.models.sandbox_app_service_route import SandboxAppServiceRoute
from sandbox0.apispec.models.sandbox_app_service_runtime import SandboxAppServiceRuntime
from sandbox0.apispec.models.sandbox_app_service_runtime_env_vars import SandboxAppServiceRuntimeEnvVars
from sandbox0.apispec.models.sandbox_app_service_runtime_type import SandboxAppServiceRuntimeType
from sandbox0.apispec.models.sandbox_service_function_source import SandboxServiceFunctionSource
from sandbox0.apispec.models.snapshot import Snapshot
from sandbox0.apispec.models.success_claim_response import SuccessClaimResponse
from sandbox0.apispec.models.success_created_response import SuccessCreatedResponse
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_function_deploy_result_response import SuccessFunctionDeployResultResponse
from sandbox0.apispec.models.success_function_list_response import SuccessFunctionListResponse
from sandbox0.apispec.models.success_function_response import SuccessFunctionResponse
from sandbox0.apispec.models.success_function_revision_list_response import SuccessFunctionRevisionListResponse
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_moved_response import SuccessMovedResponse
from sandbox0.apispec.models.success_pause_sandbox_response import SuccessPauseSandboxResponse
from sandbox0.apispec.models.success_refresh_response import SuccessRefreshResponse
from sandbox0.apispec.models.success_resume_sandbox_response import SuccessResumeSandboxResponse
from sandbox0.apispec.models.success_restore_response import SuccessRestoreResponse
from sandbox0.apispec.models.success_sandbox_list_response import SuccessSandboxListResponse
from sandbox0.apispec.models.success_sandbox_response import SuccessSandboxResponse
from sandbox0.apispec.models.success_sandbox_status_response import SuccessSandboxStatusResponse
from sandbox0.apispec.models.success_sandbox_volume_list_response import SuccessSandboxVolumeListResponse
from sandbox0.apispec.models.success_sandbox_volume_response import SuccessSandboxVolumeResponse
from sandbox0.apispec.models.success_snapshot_list_response import SuccessSnapshotListResponse
from sandbox0.apispec.models.success_snapshot_response import SuccessSnapshotResponse
from sandbox0.apispec.models.success_written_response import SuccessWrittenResponse
from sandbox0.apispec.models.volume_file_archive_import_response import VolumeFileArchiveImportResponse
from sandbox0.apispec.types import UNSET
from sandbox0.response import ensure_data, ensure_model
from sandbox0.sandbox_files import FileWatchStream
from sandbox0.sessions import SandboxSession, VolumeSession
from sandbox0.volume_files import (
    delete_volume_file,
    import_volume_archive,
    list_volume_files,
    mkdir_volume_file,
    move_volume_file,
    read_volume_file,
    stat_volume_file,
    upload_volume_directory,
    watch_volume_files,
    write_volume_file,
)

if TYPE_CHECKING:
    from sandbox0.client import Client
    from sandbox0.sandbox import Sandbox


class Sandboxes:
    def __init__(self, client: "Client") -> None:
        self._client = client

    def claim(
        self,
        template: str,
        config: Optional[SandboxConfig] = None,
        mounts: Optional[list[ClaimMountRequest]] = None,
    ) -> "Sandbox":
        request = ClaimRequest(template=template)
        if config is not None:
            request.config = config
        if mounts is not None:
            request.mounts = mounts
        resp = post_api_v1_sandboxes.sync_detailed(client=self._client.api, body=request)
        data = ensure_data(resp, SuccessClaimResponse)
        from sandbox0.sandbox import Sandbox

        bootstrap_mounts: list[MountStatus] = []
        if data.bootstrap_mounts.__class__.__name__ != "Unset":
            bootstrap_mounts = list(data.bootstrap_mounts)

        return Sandbox(
            id=data.sandbox_id,
            client=self._client,
            template=data.template,
            cluster_id=None if data.cluster_id.__class__.__name__ == "Unset" else data.cluster_id,
            pod_name=data.pod_name,
            status=data.status,
            bootstrap_mounts=bootstrap_mounts,
        )

    def open(
        self,
        template: str,
        config: Optional[SandboxConfig] = None,
        mounts: Optional[list[ClaimMountRequest]] = None,
    ) -> SandboxSession:
        sandbox = self.claim(
            template,
            config=config,
            mounts=mounts,
        )
        return SandboxSession(sandbox, closer=lambda: None if self.delete(sandbox.id) else None)

    def get(self, sandbox_id: str) -> APISandbox:
        resp = get_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxResponse)

    def update(self, sandbox_id: str, request: SandboxUpdateRequest) -> APISandbox:
        resp = put_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api, body=request)
        return ensure_data(resp, SuccessSandboxResponse)

    def delete(self, sandbox_id: str) -> SuccessMessageResponse:
        resp = delete_api_v1_sandboxes_id.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_model(resp, SuccessMessageResponse)

    def status(self, sandbox_id: str) -> SandboxStatus:
        resp = get_api_v1_sandboxes_id_status.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxStatusResponse)

    def pause(self, sandbox_id: str) -> PauseSandboxResponse:
        resp = post_api_v1_sandboxes_id_pause.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessPauseSandboxResponse)

    def resume(self, sandbox_id: str) -> ResumeSandboxResponse:
        resp = post_api_v1_sandboxes_id_resume.sync_detailed(id=sandbox_id, client=self._client.api)
        return ensure_data(resp, SuccessResumeSandboxResponse)

    def refresh(self, sandbox_id: str, request: Optional[SandboxRefreshRequest] = None) -> RefreshResponse:
        body = request if request is not None else SandboxRefreshRequest()
        resp = post_api_v1_sandboxes_id_refresh.sync_detailed(id=sandbox_id, client=self._client.api, body=body)
        return ensure_data(resp, SuccessRefreshResponse)

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


@dataclass
class FunctionSnapshotMount:
    snapshot_id: str
    mount_path: str


@dataclass
class FunctionServiceSpec:
    port: int
    id: str = "app"
    display_name: Optional[str] = None
    command: Optional[list[str]] = None
    cwd: Optional[str] = None
    env_vars: Optional[dict[str, str]] = None
    warm_process_name: Optional[str] = None
    health_path: Optional[str] = None
    routes: Optional[list[SandboxAppServiceRoute]] = None


@dataclass
class FunctionDeploySpec:
    template: str
    service: FunctionServiceSpec
    name: Optional[str] = None
    slug: Optional[str] = None
    mounts: Optional[list[FunctionSnapshotMount]] = None
    env_vars: Optional[dict[str, str]] = None
    scale: Optional[FunctionScalePolicy] = None
    activate: Optional[bool] = None


@dataclass
class FunctionDeployOptions:
    name: Optional[str] = None
    slug: Optional[str] = None
    scale: Optional[FunctionScalePolicy] = None
    activate: Optional[bool] = None


class Functions:
    def __init__(self, client: "Client") -> None:
        self._client = client

    def deploy(self, spec: FunctionDeploySpec) -> FunctionDeployResult:
        return self.deploy_request(function_deploy_request_from_spec(spec))

    def deploy_request(self, request: FunctionDeployRequest) -> FunctionDeployResult:
        resp = post_api_v1_functions_deploy.sync_detailed(client=self._client.api, body=request)
        return ensure_data(resp, SuccessFunctionDeployResultResponse)

    def deploy_revision(self, function_id: str, spec: FunctionDeploySpec) -> FunctionDeployResult:
        return self.deploy_revision_request(function_id, function_deploy_request_from_spec(spec))

    def deploy_revision_request(self, function_id: str, request: FunctionDeployRequest) -> FunctionDeployResult:
        resp = post_api_v1_functions_id_deploy.sync_detailed(
            id=function_id,
            client=self._client.api,
            body=request,
        )
        return ensure_data(resp, SuccessFunctionDeployResultResponse)

    def deploy_from_sandbox_service(
        self,
        sandbox_id: str,
        service_id: str,
        options: Optional[FunctionDeployOptions] = None,
    ) -> FunctionDeployResult:
        options = options or FunctionDeployOptions()
        request = FunctionDeployRequest(
            name=options.name or UNSET,  # type: ignore[arg-type]
            slug=options.slug or UNSET,  # type: ignore[arg-type]
            scale=options.scale or UNSET,  # type: ignore[arg-type]
            activate=options.activate if options.activate is not None else True,
            source=FunctionSource(
                type_=FunctionSourceType.SANDBOX_SERVICE,
                sandbox_service=SandboxServiceFunctionSource(
                    sandbox_id=sandbox_id,
                    service_id=service_id,
                ),
            ),
        )
        return self.deploy_request(request)

    def list(self) -> list[APIFunction]:
        resp = get_api_v1_functions.sync_detailed(client=self._client.api)
        data = ensure_data(resp, SuccessFunctionListResponse)
        return list(data.functions)

    def get(self, function_id: str) -> APIFunction:
        resp = get_api_v1_functions_id.sync_detailed(id=function_id, client=self._client.api)
        return ensure_data(resp, SuccessFunctionResponse)

    def update(self, function_id: str, request: FunctionUpdateRequest) -> APIFunction:
        resp = put_api_v1_functions_id.sync_detailed(
            id=function_id,
            client=self._client.api,
            body=request,
        )
        return ensure_data(resp, SuccessFunctionResponse)

    def delete(self, function_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_functions_id.sync_detailed(id=function_id, client=self._client.api)
        return ensure_model(resp, SuccessDeletedResponse)

    def revisions(self, function_id: str) -> list[FunctionRevision]:
        resp = get_api_v1_functions_id_revisions.sync_detailed(id=function_id, client=self._client.api)
        data = ensure_data(resp, SuccessFunctionRevisionListResponse)
        return list(data.revisions)

    def activate_revision(self, function_id: str, revision_id: str) -> FunctionDeployResult:
        resp = put_api_v1_functions_id_active_revision.sync_detailed(
            id=function_id,
            client=self._client.api,
            body=ActivateFunctionRevisionRequest(revision_id=revision_id),
        )
        return ensure_data(resp, SuccessFunctionDeployResultResponse)


def function_deploy_request_from_spec(spec: FunctionDeploySpec) -> FunctionDeployRequest:
    if not spec.template:
        raise ValueError("function template is required")
    mounts = []
    for mount in spec.mounts or []:
        if not mount.snapshot_id or not mount.mount_path:
            raise ValueError("function mount requires snapshot_id and mount_path")
        mounts.append(
            FunctionRevisionMount(
                snapshot_id=mount.snapshot_id,
                mount_path=mount.mount_path,
                read_only=True,
            )
        )

    revision_spec = FunctionRevisionSpec(
        template=spec.template,
        service=function_service_from_spec(spec.service),
        mounts=mounts,
        env_vars=_function_revision_env_vars(spec.env_vars),
    )
    return FunctionDeployRequest(
        name=spec.name or UNSET,  # type: ignore[arg-type]
        slug=spec.slug or UNSET,  # type: ignore[arg-type]
        scale=spec.scale or UNSET,  # type: ignore[arg-type]
        activate=spec.activate if spec.activate is not None else True,
        source=FunctionSource(type_=FunctionSourceType.SNAPSHOT),
        spec=revision_spec,
    )


def function_service_from_spec(spec: FunctionServiceSpec) -> SandboxAppService:
    if spec.port <= 0:
        raise ValueError("function service port is required")
    service = SandboxAppService(
        id=spec.id or "app",
        display_name=spec.display_name or UNSET,  # type: ignore[arg-type]
        port=spec.port,
        runtime=function_runtime_from_spec(spec),
        ingress=SandboxAppServiceIngress(public=True, routes=spec.routes or UNSET),  # type: ignore[arg-type]
        health_check=SandboxAppServiceHealth(path=spec.health_path) if spec.health_path else UNSET,  # type: ignore[arg-type]
    )
    return service


def function_runtime_from_spec(spec: FunctionServiceSpec) -> SandboxAppServiceRuntime:
    if spec.command:
        return SandboxAppServiceRuntime(
            type_=SandboxAppServiceRuntimeType.CMD,
            command=list(spec.command),
            cwd=spec.cwd or UNSET,  # type: ignore[arg-type]
            env_vars=_function_runtime_env_vars(spec.env_vars),
        )
    if spec.warm_process_name:
        return SandboxAppServiceRuntime(
            type_=SandboxAppServiceRuntimeType.WARM_PROCESS,
            warm_process_name=spec.warm_process_name,
        )
    raise ValueError("function service command or warm_process_name is required")


def _function_revision_env_vars(values: Optional[dict[str, str]]) -> Union[FunctionRevisionSpecEnvVars, Any]:
    if values is None:
        return UNSET
    return FunctionRevisionSpecEnvVars.from_dict(dict(values))


def _function_runtime_env_vars(values: Optional[dict[str, str]]) -> Union[SandboxAppServiceRuntimeEnvVars, Any]:
    if values is None:
        return UNSET
    return SandboxAppServiceRuntimeEnvVars.from_dict(dict(values))


class Volumes:
    def __init__(self, client: "Client") -> None:
        self._client = client

    def create(self, request: CreateSandboxVolumeRequest) -> SandboxVolume:
        resp = post_api_v1_sandboxvolumes.sync_detailed(client=self._client.api, body=request)
        return ensure_data(resp, SuccessSandboxVolumeResponse)

    def open(self, request: CreateSandboxVolumeRequest) -> VolumeSession:
        volume = self.create(request)
        return VolumeSession(volume, closer=lambda: None if self.delete(volume.id) else None)

    def list(self) -> List[SandboxVolume]:
        resp = get_api_v1_sandboxvolumes.sync_detailed(client=self._client.api)
        data = ensure_data(resp, SuccessSandboxVolumeListResponse)
        return data

    def get(self, volume_id: str) -> SandboxVolume:
        resp = get_api_v1_sandboxvolumes_id.sync_detailed(id=volume_id, client=self._client.api)
        return ensure_data(resp, SuccessSandboxVolumeResponse)

    def delete(self, volume_id: str, *, force: bool = False) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandboxvolumes_id.sync_detailed(
            id=volume_id,
            client=self._client.api,
            force=force,
        )
        return ensure_model(resp, SuccessDeletedResponse)

    def fork(self, volume_id: str, request: Optional[ForkVolumeRequest] = None) -> SandboxVolume:
        body = request if request is not None else ForkVolumeRequest()
        resp = post_api_v1_sandboxvolumes_id_fork.sync_detailed(id=volume_id, client=self._client.api, body=body)
        return ensure_data(resp, SuccessSandboxVolumeResponse)

    def create_snapshot(self, volume_id: str, request: CreateSnapshotRequest) -> Snapshot:
        resp = post_api_v1_sandboxvolumes_id_snapshots.sync_detailed(id=volume_id, client=self._client.api, body=request)
        return ensure_data(resp, SuccessSnapshotResponse)

    def list_snapshots(self, volume_id: str) -> List[Snapshot]:
        resp = get_api_v1_sandboxvolumes_id_snapshots.sync_detailed(id=volume_id, client=self._client.api)
        data = ensure_data(resp, SuccessSnapshotListResponse)
        return data

    def get_snapshot(self, volume_id: str, snapshot_id: str) -> Snapshot:
        resp = get_api_v1_sandboxvolumes_id_snapshots_snapshot_id.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_data(resp, SuccessSnapshotResponse)

    def delete_snapshot(self, volume_id: str, snapshot_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandboxvolumes_id_snapshots_snapshot_id.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_model(resp, SuccessDeletedResponse)

    def restore_snapshot(self, volume_id: str, snapshot_id: str) -> SuccessRestoreResponse:
        resp = post_api_v1_sandboxvolumes_id_snapshots_snapshot_id_restore.sync_detailed(
            id=volume_id,
            snapshot_id=snapshot_id,
            client=self._client.api,
        )
        return ensure_model(resp, SuccessRestoreResponse)

    def read_file(self, volume_id: str, path: str) -> bytes:
        return read_volume_file(self._client, volume_id, path)

    def stat_file(self, volume_id: str, path: str) -> FileInfo:
        return stat_volume_file(self._client, volume_id, path)

    def list_files(self, volume_id: str, path: str) -> List[FileInfo]:
        return list_volume_files(self._client, volume_id, path)

    def write_file(self, volume_id: str, path: str, data: bytes) -> SuccessWrittenResponse:
        return write_volume_file(self._client, volume_id, path, data)

    def import_archive(
        self,
        volume_id: str,
        path: str,
        archive: Union[bytes, BinaryIO],
    ) -> VolumeFileArchiveImportResponse:
        return import_volume_archive(self._client, volume_id, path, archive)

    def upload_directory(self, volume_id: str, local_path: str, remote_path: str) -> VolumeFileArchiveImportResponse:
        return upload_volume_directory(self._client, volume_id, local_path, remote_path)

    def mkdir(self, volume_id: str, path: str, recursive: bool = False) -> SuccessCreatedResponse:
        return mkdir_volume_file(self._client, volume_id, path, recursive)

    def delete_file(self, volume_id: str, path: str) -> SuccessDeletedResponse:
        return delete_volume_file(self._client, volume_id, path)

    def move_file(self, volume_id: str, source: str, destination: str) -> SuccessMovedResponse:
        return move_volume_file(self._client, volume_id, source, destination)

    def watch_files(self, volume_id: str, path: str, recursive: bool = False) -> FileWatchStream:
        return watch_volume_files(self._client, volume_id, path, recursive)
