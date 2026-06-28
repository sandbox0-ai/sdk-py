from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_app_service import SandboxAppService
    from ..models.sandbox_network_policy import SandboxNetworkPolicy
    from ..models.sandbox_resource_config import SandboxResourceConfig
    from ..models.sandbox_update_config_env_vars import SandboxUpdateConfigEnvVars


T = TypeVar("T", bound="SandboxUpdateConfig")


@_attrs_define
class SandboxUpdateConfig:
    """Subset of SandboxConfig fields that can be updated at runtime without restarting the sandbox.
    Note: env_vars only affect new processes. webhook is not included as it requires restart.

        Attributes:
            env_vars (Union[Unset, SandboxUpdateConfigEnvVars]): Sandbox-level environment variables used as defaults for
                new procd-managed
                processes. Omitting this field preserves the existing environment map; passing
                an empty object clears it.
            resources (Union[Unset, SandboxResourceConfig]): Instance-level sandbox resource override. Sandbox0 exposes
                memory only and derives CPU from the platform memory-per-CPU ratio.
            ttl (Union[Unset, int]): Runtime soft time-to-live in seconds. When it expires, Sandbox0 checkpoints the
                writable rootfs, pauses the sandbox, and releases runtime compute while preserving durable sandbox state.
            hard_ttl (Union[Unset, int]): Sandbox hard time-to-live in seconds. When it expires, Sandbox0 deletes the
                sandbox identity and durable state, including paused rootfs checkpoints.
            network (Union[Unset, SandboxNetworkPolicy]):
            auto_resume (Union[Unset, bool]): Sandbox-level resume gate for paused sandboxes. When false, any inbound
                request
                (API or public exposure) must not auto resume the sandbox.
                 Default: True.
            services (Union[Unset, list['SandboxAppService']]):
    """

    env_vars: Union[Unset, "SandboxUpdateConfigEnvVars"] = UNSET
    resources: Union[Unset, "SandboxResourceConfig"] = UNSET
    ttl: Union[Unset, int] = UNSET
    hard_ttl: Union[Unset, int] = UNSET
    network: Union[Unset, "SandboxNetworkPolicy"] = UNSET
    auto_resume: Union[Unset, bool] = True
    services: Union[Unset, list["SandboxAppService"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        resources: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        ttl = self.ttl

        hard_ttl = self.hard_ttl

        network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        auto_resume = self.auto_resume

        services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if resources is not UNSET:
            field_dict["resources"] = resources
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if hard_ttl is not UNSET:
            field_dict["hard_ttl"] = hard_ttl
        if network is not UNSET:
            field_dict["network"] = network
        if auto_resume is not UNSET:
            field_dict["auto_resume"] = auto_resume
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_app_service import SandboxAppService
        from ..models.sandbox_network_policy import SandboxNetworkPolicy
        from ..models.sandbox_resource_config import SandboxResourceConfig
        from ..models.sandbox_update_config_env_vars import SandboxUpdateConfigEnvVars

        d = dict(src_dict)
        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, SandboxUpdateConfigEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = SandboxUpdateConfigEnvVars.from_dict(_env_vars)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, SandboxResourceConfig]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = SandboxResourceConfig.from_dict(_resources)

        ttl = d.pop("ttl", UNSET)

        hard_ttl = d.pop("hard_ttl", UNSET)

        _network = d.pop("network", UNSET)
        network: Union[Unset, SandboxNetworkPolicy]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = SandboxNetworkPolicy.from_dict(_network)

        auto_resume = d.pop("auto_resume", UNSET)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = SandboxAppService.from_dict(services_item_data)

            services.append(services_item)

        sandbox_update_config = cls(
            env_vars=env_vars,
            resources=resources,
            ttl=ttl,
            hard_ttl=hard_ttl,
            network=network,
            auto_resume=auto_resume,
            services=services,
        )

        sandbox_update_config.additional_properties = d
        return sandbox_update_config

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
