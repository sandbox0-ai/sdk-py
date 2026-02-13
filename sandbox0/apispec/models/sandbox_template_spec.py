from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.container_spec import ContainerSpec
    from ..models.lifecycle_policy import LifecyclePolicy
    from ..models.pod_spec_override import PodSpecOverride
    from ..models.pool_strategy import PoolStrategy
    from ..models.sandbox_template_spec_env_vars import SandboxTemplateSpecEnvVars
    from ..models.tpl_sandbox_network_policy import TplSandboxNetworkPolicy


T = TypeVar("T", bound="SandboxTemplateSpec")


@_attrs_define
class SandboxTemplateSpec:
    """
    Attributes:
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        main_container (Union[Unset, ContainerSpec]):
        sidecars (Union[Unset, list['ContainerSpec']]):
        pod (Union[Unset, PodSpecOverride]):
        network (Union[Unset, TplSandboxNetworkPolicy]):
        pool (Union[Unset, PoolStrategy]):
        lifecycle (Union[Unset, LifecyclePolicy]):
        env_vars (Union[Unset, SandboxTemplateSpecEnvVars]):
        public (Union[Unset, bool]):
        allowed_teams (Union[Unset, list[str]]):
        runtime_class_name (Union[Unset, str]):
        cluster_id (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    main_container: Union[Unset, "ContainerSpec"] = UNSET
    sidecars: Union[Unset, list["ContainerSpec"]] = UNSET
    pod: Union[Unset, "PodSpecOverride"] = UNSET
    network: Union[Unset, "TplSandboxNetworkPolicy"] = UNSET
    pool: Union[Unset, "PoolStrategy"] = UNSET
    lifecycle: Union[Unset, "LifecyclePolicy"] = UNSET
    env_vars: Union[Unset, "SandboxTemplateSpecEnvVars"] = UNSET
    public: Union[Unset, bool] = UNSET
    allowed_teams: Union[Unset, list[str]] = UNSET
    runtime_class_name: Union[Unset, str] = UNSET
    cluster_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        main_container: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.main_container, Unset):
            main_container = self.main_container.to_dict()

        sidecars: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sidecars, Unset):
            sidecars = []
            for sidecars_item_data in self.sidecars:
                sidecars_item = sidecars_item_data.to_dict()
                sidecars.append(sidecars_item)

        pod: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pod, Unset):
            pod = self.pod.to_dict()

        network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        pool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.to_dict()

        lifecycle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        public = self.public

        allowed_teams: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_teams, Unset):
            allowed_teams = self.allowed_teams

        runtime_class_name = self.runtime_class_name

        cluster_id = self.cluster_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if main_container is not UNSET:
            field_dict["mainContainer"] = main_container
        if sidecars is not UNSET:
            field_dict["sidecars"] = sidecars
        if pod is not UNSET:
            field_dict["pod"] = pod
        if network is not UNSET:
            field_dict["network"] = network
        if pool is not UNSET:
            field_dict["pool"] = pool
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if env_vars is not UNSET:
            field_dict["envVars"] = env_vars
        if public is not UNSET:
            field_dict["public"] = public
        if allowed_teams is not UNSET:
            field_dict["allowedTeams"] = allowed_teams
        if runtime_class_name is not UNSET:
            field_dict["runtimeClassName"] = runtime_class_name
        if cluster_id is not UNSET:
            field_dict["clusterId"] = cluster_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.container_spec import ContainerSpec
        from ..models.lifecycle_policy import LifecyclePolicy
        from ..models.pod_spec_override import PodSpecOverride
        from ..models.pool_strategy import PoolStrategy
        from ..models.sandbox_template_spec_env_vars import SandboxTemplateSpecEnvVars
        from ..models.tpl_sandbox_network_policy import TplSandboxNetworkPolicy

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _main_container = d.pop("mainContainer", UNSET)
        main_container: Union[Unset, ContainerSpec]
        if isinstance(_main_container, Unset):
            main_container = UNSET
        else:
            main_container = ContainerSpec.from_dict(_main_container)

        sidecars = []
        _sidecars = d.pop("sidecars", UNSET)
        for sidecars_item_data in _sidecars or []:
            sidecars_item = ContainerSpec.from_dict(sidecars_item_data)

            sidecars.append(sidecars_item)

        _pod = d.pop("pod", UNSET)
        pod: Union[Unset, PodSpecOverride]
        if isinstance(_pod, Unset):
            pod = UNSET
        else:
            pod = PodSpecOverride.from_dict(_pod)

        _network = d.pop("network", UNSET)
        network: Union[Unset, TplSandboxNetworkPolicy]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = TplSandboxNetworkPolicy.from_dict(_network)

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, PoolStrategy]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = PoolStrategy.from_dict(_pool)

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: Union[Unset, LifecyclePolicy]
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = LifecyclePolicy.from_dict(_lifecycle)

        _env_vars = d.pop("envVars", UNSET)
        env_vars: Union[Unset, SandboxTemplateSpecEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = SandboxTemplateSpecEnvVars.from_dict(_env_vars)

        public = d.pop("public", UNSET)

        allowed_teams = cast(list[str], d.pop("allowedTeams", UNSET))

        runtime_class_name = d.pop("runtimeClassName", UNSET)

        cluster_id = d.pop("clusterId", UNSET)

        sandbox_template_spec = cls(
            description=description,
            display_name=display_name,
            tags=tags,
            main_container=main_container,
            sidecars=sidecars,
            pod=pod,
            network=network,
            pool=pool,
            lifecycle=lifecycle,
            env_vars=env_vars,
            public=public,
            allowed_teams=allowed_teams,
            runtime_class_name=runtime_class_name,
            cluster_id=cluster_id,
        )

        sandbox_template_spec.additional_properties = d
        return sandbox_template_spec

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
