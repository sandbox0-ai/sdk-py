from __future__ import annotations

from sandbox0.apispec.models.container_spec import ContainerSpec
from sandbox0.apispec.models.container_spec_security_class import ContainerSpecSecurityClass
from sandbox0.apispec.models.ephemeral_mount_spec import EphemeralMountSpec
from sandbox0.apispec.models.env_var import EnvVar
from sandbox0.apispec.models.resource_quota import ResourceQuota
from sandbox0.apispec.models.sandbox_network_policy import SandboxNetworkPolicy
from sandbox0.apispec.models.sandbox_template_spec import SandboxTemplateSpec
from sandbox0.apispec.models.sandbox_template_spec_env_vars import SandboxTemplateSpecEnvVars
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.models.template_from_sandbox_create_request import (
    TemplateFromSandboxCreateRequest,
)
from sandbox0.apispec.models.template_from_sandbox_spec_overrides import (
    TemplateFromSandboxSpecOverrides,
)
from sandbox0.apispec.models.template_update_request import TemplateUpdateRequest
from sandbox0.apispec.types import UNSET, Unset


def resources(memory: str) -> ResourceQuota:
    return ResourceQuota(memory=memory)


def container(
    image: str,
    resource_quota: ResourceQuota,
    *,
    env: list[EnvVar] | Unset = UNSET,
    security_class: ContainerSpecSecurityClass | Unset = UNSET,
) -> ContainerSpec:
    return ContainerSpec(
        image=image,
        resources=resource_quota,
        env=env,
        security_class=security_class,
    )


def ephemeral_mount(mount_path: str, size_limit: str) -> EphemeralMountSpec:
    return EphemeralMountSpec(mount_path=mount_path, size_limit=size_limit)


def template_spec(
    main_container: ContainerSpec,
    *,
    description: str | Unset = UNSET,
    display_name: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    ephemeral_mounts: list[EphemeralMountSpec] | Unset = UNSET,
    network: SandboxNetworkPolicy | Unset = UNSET,
    env_vars: SandboxTemplateSpecEnvVars | dict[str, str] | Unset = UNSET,
) -> SandboxTemplateSpec:
    return SandboxTemplateSpec(
        main_container=main_container,
        description=description,
        display_name=display_name,
        tags=tags,
        ephemeral_mounts=ephemeral_mounts,
        network=network,
        env_vars=_template_env_vars(env_vars),
    )


def template_create_request(template_id: str, spec: SandboxTemplateSpec) -> TemplateCreateRequest:
    return TemplateCreateRequest(template_id=template_id, spec=spec)


def template_from_sandbox_create_request(
    template_id: str,
    sandbox_id: str,
    spec_overrides: TemplateFromSandboxSpecOverrides | Unset = UNSET,
) -> TemplateFromSandboxCreateRequest:
    return TemplateFromSandboxCreateRequest(
        template_id=template_id,
        sandbox_id=sandbox_id,
        spec_overrides=spec_overrides,
    )


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
