from __future__ import annotations

from sandbox0.apispec.models.container_spec import ContainerSpec
from sandbox0.apispec.models.env_var import EnvVar
from sandbox0.apispec.models.lifecycle_policy import LifecyclePolicy
from sandbox0.apispec.models.pod_spec_override import PodSpecOverride
from sandbox0.apispec.models.pool_strategy import PoolStrategy
from sandbox0.apispec.models.resource_quota import ResourceQuota
from sandbox0.apispec.models.sandbox_network_policy import SandboxNetworkPolicy
from sandbox0.apispec.models.sandbox_template_spec import SandboxTemplateSpec
from sandbox0.apispec.models.sandbox_template_spec_env_vars import SandboxTemplateSpecEnvVars
from sandbox0.apispec.models.security_context import SecurityContext
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.models.template_update_request import TemplateUpdateRequest
from sandbox0.apispec.models.warm_process_spec import WarmProcessSpec
from sandbox0.apispec.models.warm_process_spec_env_vars import WarmProcessSpecEnvVars
from sandbox0.apispec.models.warm_process_spec_type import WarmProcessSpecType
from sandbox0.apispec.types import UNSET, Unset


def resources(cpu: str, memory: str) -> ResourceQuota:
    return ResourceQuota(cpu=cpu, memory=memory)


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


def warm_process(
    type_: WarmProcessSpecType,
    *,
    alias: str | Unset = UNSET,
    command: list[str] | Unset = UNSET,
    cwd: str | Unset = UNSET,
    env_vars: WarmProcessSpecEnvVars | dict[str, str] | Unset = UNSET,
) -> WarmProcessSpec:
    return WarmProcessSpec(
        type_=type_,
        alias=alias,
        command=command,
        cwd=cwd,
        env_vars=_warm_process_env_vars(env_vars),
    )


def template_spec(
    main_container: ContainerSpec,
    *,
    description: str | Unset = UNSET,
    display_name: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    warm_processes: list[WarmProcessSpec] | Unset = UNSET,
    pod: PodSpecOverride | Unset = UNSET,
    network: SandboxNetworkPolicy | Unset = UNSET,
    pool: PoolStrategy | Unset = UNSET,
    lifecycle: LifecyclePolicy | Unset = UNSET,
    env_vars: SandboxTemplateSpecEnvVars | dict[str, str] | Unset = UNSET,
    public: bool | Unset = UNSET,
    allowed_teams: list[str] | Unset = UNSET,
    cluster_id: str | Unset = UNSET,
) -> SandboxTemplateSpec:
    return SandboxTemplateSpec(
        main_container=main_container,
        description=description,
        display_name=display_name,
        tags=tags,
        warm_processes=warm_processes,
        pod=pod,
        network=network,
        pool=pool,
        lifecycle=lifecycle,
        env_vars=_template_env_vars(env_vars),
        public=public,
        allowed_teams=allowed_teams,
        cluster_id=cluster_id,
    )


def template_create_request(template_id: str, spec: SandboxTemplateSpec) -> TemplateCreateRequest:
    return TemplateCreateRequest(template_id=template_id, spec=spec)


def template_update_request(spec: SandboxTemplateSpec) -> TemplateUpdateRequest:
    return TemplateUpdateRequest(spec=spec)


def _template_env_vars(
    env_vars: SandboxTemplateSpecEnvVars | dict[str, str] | Unset,
) -> SandboxTemplateSpecEnvVars | Unset:
    if isinstance(env_vars, Unset):
        return UNSET
    if isinstance(env_vars, SandboxTemplateSpecEnvVars):
        return env_vars
    return SandboxTemplateSpecEnvVars.from_dict(env_vars)


def _warm_process_env_vars(
    env_vars: WarmProcessSpecEnvVars | dict[str, str] | Unset,
) -> WarmProcessSpecEnvVars | Unset:
    if isinstance(env_vars, Unset):
        return UNSET
    if isinstance(env_vars, WarmProcessSpecEnvVars):
        return env_vars
    return WarmProcessSpecEnvVars.from_dict(env_vars)
