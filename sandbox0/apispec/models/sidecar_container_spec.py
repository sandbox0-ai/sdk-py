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
    from ..models.container_mount_spec import ContainerMountSpec
    from ..models.env_var import EnvVar
    from ..models.probe import Probe
    from ..models.resource_quota import ResourceQuota


T = TypeVar("T", bound="SidecarContainerSpec")


@_attrs_define
class SidecarContainerSpec:
    """
    Attributes:
        name (str):
        image (str):
        resources (ResourceQuota):
        command (Union[Unset, list[str]]):
        args (Union[Unset, list[str]]):
        env (Union[Unset, list['EnvVar']]):
        mounts (Union[Unset, list['ContainerMountSpec']]):
        startup_probe (Union[Unset, Probe]):
    """

    name: str
    image: str
    resources: "ResourceQuota"
    command: Union[Unset, list[str]] = UNSET
    args: Union[Unset, list[str]] = UNSET
    env: Union[Unset, list["EnvVar"]] = UNSET
    mounts: Union[Unset, list["ContainerMountSpec"]] = UNSET
    startup_probe: Union[Unset, "Probe"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        image = self.image

        resources = self.resources.to_dict()

        command: Union[Unset, list[str]] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command

        args: Union[Unset, list[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        env: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for env_item_data in self.env:
                env_item = env_item_data.to_dict()
                env.append(env_item)

        mounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()
                mounts.append(mounts_item)

        startup_probe: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.startup_probe, Unset):
            startup_probe = self.startup_probe.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "image": image,
                "resources": resources,
            }
        )
        if command is not UNSET:
            field_dict["command"] = command
        if args is not UNSET:
            field_dict["args"] = args
        if env is not UNSET:
            field_dict["env"] = env
        if mounts is not UNSET:
            field_dict["mounts"] = mounts
        if startup_probe is not UNSET:
            field_dict["startupProbe"] = startup_probe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.container_mount_spec import ContainerMountSpec
        from ..models.env_var import EnvVar
        from ..models.probe import Probe
        from ..models.resource_quota import ResourceQuota

        d = dict(src_dict)
        name = d.pop("name")

        image = d.pop("image")

        resources = ResourceQuota.from_dict(d.pop("resources"))

        command = cast(list[str], d.pop("command", UNSET))

        args = cast(list[str], d.pop("args", UNSET))

        env = []
        _env = d.pop("env", UNSET)
        for env_item_data in _env or []:
            env_item = EnvVar.from_dict(env_item_data)

            env.append(env_item)

        mounts = []
        _mounts = d.pop("mounts", UNSET)
        for mounts_item_data in _mounts or []:
            mounts_item = ContainerMountSpec.from_dict(mounts_item_data)

            mounts.append(mounts_item)

        _startup_probe = d.pop("startupProbe", UNSET)
        startup_probe: Union[Unset, Probe]
        if isinstance(_startup_probe, Unset):
            startup_probe = UNSET
        else:
            startup_probe = Probe.from_dict(_startup_probe)

        sidecar_container_spec = cls(
            name=name,
            image=image,
            resources=resources,
            command=command,
            args=args,
            env=env,
            mounts=mounts,
            startup_probe=startup_probe,
        )

        sidecar_container_spec.additional_properties = d
        return sidecar_container_spec

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
