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
    from ..models.public_gateway_config import PublicGatewayConfig
    from ..models.sandbox_app_service import SandboxAppService
    from ..models.sandbox_config_env_vars import SandboxConfigEnvVars
    from ..models.sandbox_network_policy import SandboxNetworkPolicy
    from ..models.webhook_config import WebhookConfig


T = TypeVar("T", bound="SandboxConfig")


@_attrs_define
class SandboxConfig:
    """
    Attributes:
        env_vars (Union[Unset, SandboxConfigEnvVars]):
        ttl (Union[Unset, int]):
        hard_ttl (Union[Unset, int]):
        network (Union[Unset, SandboxNetworkPolicy]):
        webhook (Union[Unset, WebhookConfig]): Per-sandbox webhook configuration. Sandbox0 delivers webhook events at
            least once and consumers should deduplicate by event_id. For sandbox lifecycle events, procd persists signed
            delivery records to a manager-owned SandboxVolume outside the workspace before dispatch; manager also emits
            sandbox.deleted during pod deletion cleanup.
        auto_resume (Union[Unset, bool]): Sandbox-level resume gate for paused sandboxes. When false, any inbound
            request
            (API or public exposure) must not auto resume the sandbox.
             Default: True.
        services (Union[Unset, list['SandboxAppService']]):
        public_gateway (Union[Unset, PublicGatewayConfig]):
    """

    env_vars: Union[Unset, "SandboxConfigEnvVars"] = UNSET
    ttl: Union[Unset, int] = UNSET
    hard_ttl: Union[Unset, int] = UNSET
    network: Union[Unset, "SandboxNetworkPolicy"] = UNSET
    webhook: Union[Unset, "WebhookConfig"] = UNSET
    auto_resume: Union[Unset, bool] = True
    services: Union[Unset, list["SandboxAppService"]] = UNSET
    public_gateway: Union[Unset, "PublicGatewayConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        ttl = self.ttl

        hard_ttl = self.hard_ttl

        network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        webhook: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.webhook, Unset):
            webhook = self.webhook.to_dict()

        auto_resume = self.auto_resume

        services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        public_gateway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.public_gateway, Unset):
            public_gateway = self.public_gateway.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if hard_ttl is not UNSET:
            field_dict["hard_ttl"] = hard_ttl
        if network is not UNSET:
            field_dict["network"] = network
        if webhook is not UNSET:
            field_dict["webhook"] = webhook
        if auto_resume is not UNSET:
            field_dict["auto_resume"] = auto_resume
        if services is not UNSET:
            field_dict["services"] = services
        if public_gateway is not UNSET:
            field_dict["public_gateway"] = public_gateway

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_gateway_config import PublicGatewayConfig
        from ..models.sandbox_app_service import SandboxAppService
        from ..models.sandbox_config_env_vars import SandboxConfigEnvVars
        from ..models.sandbox_network_policy import SandboxNetworkPolicy
        from ..models.webhook_config import WebhookConfig

        d = dict(src_dict)
        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, SandboxConfigEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = SandboxConfigEnvVars.from_dict(_env_vars)

        ttl = d.pop("ttl", UNSET)

        hard_ttl = d.pop("hard_ttl", UNSET)

        _network = d.pop("network", UNSET)
        network: Union[Unset, SandboxNetworkPolicy]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = SandboxNetworkPolicy.from_dict(_network)

        _webhook = d.pop("webhook", UNSET)
        webhook: Union[Unset, WebhookConfig]
        if isinstance(_webhook, Unset):
            webhook = UNSET
        else:
            webhook = WebhookConfig.from_dict(_webhook)

        auto_resume = d.pop("auto_resume", UNSET)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = SandboxAppService.from_dict(services_item_data)

            services.append(services_item)

        _public_gateway = d.pop("public_gateway", UNSET)
        public_gateway: Union[Unset, PublicGatewayConfig]
        if isinstance(_public_gateway, Unset):
            public_gateway = UNSET
        else:
            public_gateway = PublicGatewayConfig.from_dict(_public_gateway)

        sandbox_config = cls(
            env_vars=env_vars,
            ttl=ttl,
            hard_ttl=hard_ttl,
            network=network,
            webhook=webhook,
            auto_resume=auto_resume,
            services=services,
            public_gateway=public_gateway,
        )

        sandbox_config.additional_properties = d
        return sandbox_config

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
