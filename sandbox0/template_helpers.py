from __future__ import annotations

from sandbox0.apispec.models.container_mount_spec import ContainerMountSpec
from sandbox0.apispec.models.container_spec import ContainerSpec
from sandbox0.apispec.models.env_var import EnvVar
from sandbox0.apispec.models.lifecycle_policy import LifecyclePolicy
from sandbox0.apispec.models.pod_spec_override import PodSpecOverride
from sandbox0.apispec.models.pool_strategy import PoolStrategy
from sandbox0.apispec.models.probe import Probe
from sandbox0.apispec.models.resource_quota import ResourceQuota
from sandbox0.apispec.models.sandbox_network_policy import SandboxNetworkPolicy
from sandbox0.apispec.models.sandbox_template_spec import SandboxTemplateSpec
from sandbox0.apispec.models.shared_volume_spec import SharedVolumeSpec
from sandbox0.apispec.models.sidecar_container_spec import SidecarContainerSpec
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.models.template_update_request import TemplateUpdateRequest
from sandbox0.apispec.models.security_context import SecurityContext
from sandbox0.apispec.types import UNSET, Unset


def resources(cpu: str, memory: str) -> ResourceQuota:
    return ResourceQuota(cpu=cpu, memory=memory)


def mount(name: str, mount_path: str) -> ContainerMountSpec:
    return ContainerMountSpec(name=name, mount_path=mount_path)


def container(
    image: str,
    resource_quota: ResourceQuota,
    *,
    image_pull_policy: str | Unset = UNSET,
    env: list[EnvVar] | Unset = UNSET,
    security_context: SecurityContext | Unset = UNSET,
) -> ContainerSpec:
    return ContainerSpec(
        image=image,
        resources=resource_quota,
        image_pull_policy=image_pull_policy,
        env=env,
        security_context=security_context,
    )


def sidecar(
    name: str,
    image: str,
    resource_quota: ResourceQuota,
    *,
    command: list[str] | Unset = UNSET,
    args: list[str] | Unset = UNSET,
    env: list[EnvVar] | Unset = UNSET,
    mounts: list[ContainerMountSpec] | Unset = UNSET,
    startup_probe: Probe | Unset = UNSET,
) -> SidecarContainerSpec:
    return SidecarContainerSpec(
        name=name,
        image=image,
        resources=resource_quota,
        command=command,
        args=args,
        env=env,
        mounts=mounts,
        startup_probe=startup_probe,
    )


def shared_volume(
    name: str,
    mount_path: str,
    *,
    sandbox_volume_id: str | Unset = UNSET,
    cache_size: str | Unset = UNSET,
    prefetch: int | Unset = UNSET,
    buffer_size: str | Unset = UNSET,
    writeback: bool | Unset = UNSET,
) -> SharedVolumeSpec:
    return SharedVolumeSpec(
        name=name,
        sandbox_volume_id=sandbox_volume_id,
        mount_path=mount_path,
        cache_size=cache_size,
        prefetch=prefetch,
        buffer_size=buffer_size,
        writeback=writeback,
    )


def template_spec(
    main_container: ContainerSpec,
    *,
    description: str | Unset = UNSET,
    display_name: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    sidecars: list[SidecarContainerSpec] | Unset = UNSET,
    shared_volumes: list[SharedVolumeSpec] | Unset = UNSET,
    pod: PodSpecOverride | Unset = UNSET,
    network: SandboxNetworkPolicy | Unset = UNSET,
    pool: PoolStrategy | Unset = UNSET,
    lifecycle: LifecyclePolicy | Unset = UNSET,
    env_vars: dict[str, str] | Unset = UNSET,
    public: bool | Unset = UNSET,
    allowed_teams: list[str] | Unset = UNSET,
    cluster_id: str | Unset = UNSET,
) -> SandboxTemplateSpec:
    return SandboxTemplateSpec(
        main_container=main_container,
        description=description,
        display_name=display_name,
        tags=tags,
        sidecars=sidecars,
        shared_volumes=shared_volumes,
        pod=pod,
        network=network,
        pool=pool,
        lifecycle=lifecycle,
        env_vars=env_vars,
        public=public,
        allowed_teams=allowed_teams,
        cluster_id=cluster_id,
    )


def template_create_request(template_id: str, spec: SandboxTemplateSpec) -> TemplateCreateRequest:
    return TemplateCreateRequest(template_id=template_id, spec=spec)


def template_update_request(spec: SandboxTemplateSpec) -> TemplateUpdateRequest:
    return TemplateUpdateRequest(spec=spec)
