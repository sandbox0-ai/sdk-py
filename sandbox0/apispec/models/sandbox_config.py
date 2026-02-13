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
    from ..models.exposed_port_config import ExposedPortConfig
    from ..models.sandbox_config_env_vars import SandboxConfigEnvVars
    from ..models.tpl_sandbox_network_policy import TplSandboxNetworkPolicy
    from ..models.webhook_config import WebhookConfig


T = TypeVar("T", bound="SandboxConfig")


@_attrs_define
class SandboxConfig:
    """
    Attributes:
        env_vars (Union[Unset, SandboxConfigEnvVars]):
        ttl (Union[Unset, int]):
        hard_ttl (Union[Unset, int]):
        network (Union[Unset, TplSandboxNetworkPolicy]):
        webhook (Union[Unset, WebhookConfig]):
        auto_resume (Union[Unset, bool]): Sandbox-level resume gate for paused sandboxes. When false, any inbound
            request
            (API or public exposure) must not auto resume the sandbox.
             Default: False.
        exposed_ports (Union[Unset, list['ExposedPortConfig']]):
    """

    env_vars: Union[Unset, "SandboxConfigEnvVars"] = UNSET
    ttl: Union[Unset, int] = UNSET
    hard_ttl: Union[Unset, int] = UNSET
    network: Union[Unset, "TplSandboxNetworkPolicy"] = UNSET
    webhook: Union[Unset, "WebhookConfig"] = UNSET
    auto_resume: Union[Unset, bool] = False
    exposed_ports: Union[Unset, list["ExposedPortConfig"]] = UNSET
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

        exposed_ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.exposed_ports, Unset):
            exposed_ports = []
            for exposed_ports_item_data in self.exposed_ports:
                exposed_ports_item = exposed_ports_item_data.to_dict()
                exposed_ports.append(exposed_ports_item)

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
        if exposed_ports is not UNSET:
            field_dict["exposed_ports"] = exposed_ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exposed_port_config import ExposedPortConfig
        from ..models.sandbox_config_env_vars import SandboxConfigEnvVars
        from ..models.tpl_sandbox_network_policy import TplSandboxNetworkPolicy
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
        network: Union[Unset, TplSandboxNetworkPolicy]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = TplSandboxNetworkPolicy.from_dict(_network)

        _webhook = d.pop("webhook", UNSET)
        webhook: Union[Unset, WebhookConfig]
        if isinstance(_webhook, Unset):
            webhook = UNSET
        else:
            webhook = WebhookConfig.from_dict(_webhook)

        auto_resume = d.pop("auto_resume", UNSET)

        exposed_ports = []
        _exposed_ports = d.pop("exposed_ports", UNSET)
        for exposed_ports_item_data in _exposed_ports or []:
            exposed_ports_item = ExposedPortConfig.from_dict(exposed_ports_item_data)

            exposed_ports.append(exposed_ports_item)

        sandbox_config = cls(
            env_vars=env_vars,
            ttl=ttl,
            hard_ttl=hard_ttl,
            network=network,
            webhook=webhook,
            auto_resume=auto_resume,
            exposed_ports=exposed_ports,
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
