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
    from ..models.ephemeral_mount_spec import EphemeralMountSpec
    from ..models.sandbox_network_policy import SandboxNetworkPolicy
    from ..models.sandbox_template_spec_env_vars import SandboxTemplateSpecEnvVars


T = TypeVar("T", bound="SandboxTemplateSpec")


@_attrs_define
class SandboxTemplateSpec:
    """
    Attributes:
        main_container (ContainerSpec):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        ephemeral_mounts (Union[Unset, list['EphemeralMountSpec']]): Claim-lifetime tmpfs mounts excluded from pause,
            resume, fork, and snapshot RootFS generations.
        network (Union[Unset, SandboxNetworkPolicy]):
        env_vars (Union[Unset, SandboxTemplateSpecEnvVars]):
    """

    main_container: "ContainerSpec"
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    ephemeral_mounts: Union[Unset, list["EphemeralMountSpec"]] = UNSET
    network: Union[Unset, "SandboxNetworkPolicy"] = UNSET
    env_vars: Union[Unset, "SandboxTemplateSpecEnvVars"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_container = self.main_container.to_dict()

        description = self.description

        display_name = self.display_name

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        ephemeral_mounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ephemeral_mounts, Unset):
            ephemeral_mounts = []
            for ephemeral_mounts_item_data in self.ephemeral_mounts:
                ephemeral_mounts_item = ephemeral_mounts_item_data.to_dict()
                ephemeral_mounts.append(ephemeral_mounts_item)

        network: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mainContainer": main_container,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if ephemeral_mounts is not UNSET:
            field_dict["ephemeralMounts"] = ephemeral_mounts
        if network is not UNSET:
            field_dict["network"] = network
        if env_vars is not UNSET:
            field_dict["envVars"] = env_vars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.container_spec import ContainerSpec
        from ..models.ephemeral_mount_spec import EphemeralMountSpec
        from ..models.sandbox_network_policy import SandboxNetworkPolicy
        from ..models.sandbox_template_spec_env_vars import SandboxTemplateSpecEnvVars

        d = dict(src_dict)
        main_container = ContainerSpec.from_dict(d.pop("mainContainer"))

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        ephemeral_mounts = []
        _ephemeral_mounts = d.pop("ephemeralMounts", UNSET)
        for ephemeral_mounts_item_data in _ephemeral_mounts or []:
            ephemeral_mounts_item = EphemeralMountSpec.from_dict(
                ephemeral_mounts_item_data
            )

            ephemeral_mounts.append(ephemeral_mounts_item)

        _network = d.pop("network", UNSET)
        network: Union[Unset, SandboxNetworkPolicy]
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = SandboxNetworkPolicy.from_dict(_network)

        _env_vars = d.pop("envVars", UNSET)
        env_vars: Union[Unset, SandboxTemplateSpecEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = SandboxTemplateSpecEnvVars.from_dict(_env_vars)

        sandbox_template_spec = cls(
            main_container=main_container,
            description=description,
            display_name=display_name,
            tags=tags,
            ephemeral_mounts=ephemeral_mounts,
            network=network,
            env_vars=env_vars,
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
