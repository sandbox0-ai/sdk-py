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
    from ..models.env_var import EnvVar
    from ..models.probe import Probe
    from ..models.resource_quota import ResourceQuota
    from ..models.security_context import SecurityContext


T = TypeVar("T", bound="SidecarContainerSpec")


@_attrs_define
class SidecarContainerSpec:
    """
    Attributes:
        name (str):
        image (str):
        command (Union[Unset, list[str]]):
        args (Union[Unset, list[str]]):
        env (Union[Unset, list['EnvVar']]):
        resources (Union[Unset, ResourceQuota]):
        security_context (Union[Unset, SecurityContext]):
        readiness_probe (Union[Unset, Probe]):
        liveness_probe (Union[Unset, Probe]):
        startup_probe (Union[Unset, Probe]):
    """

    name: str
    image: str
    command: Union[Unset, list[str]] = UNSET
    args: Union[Unset, list[str]] = UNSET
    env: Union[Unset, list["EnvVar"]] = UNSET
    resources: Union[Unset, "ResourceQuota"] = UNSET
    security_context: Union[Unset, "SecurityContext"] = UNSET
    readiness_probe: Union[Unset, "Probe"] = UNSET
    liveness_probe: Union[Unset, "Probe"] = UNSET
    startup_probe: Union[Unset, "Probe"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        image = self.image

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

        resources: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        security_context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.security_context, Unset):
            security_context = self.security_context.to_dict()

        readiness_probe: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.readiness_probe, Unset):
            readiness_probe = self.readiness_probe.to_dict()

        liveness_probe: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.liveness_probe, Unset):
            liveness_probe = self.liveness_probe.to_dict()

        startup_probe: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.startup_probe, Unset):
            startup_probe = self.startup_probe.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "image": image,
            }
        )
        if command is not UNSET:
            field_dict["command"] = command
        if args is not UNSET:
            field_dict["args"] = args
        if env is not UNSET:
            field_dict["env"] = env
        if resources is not UNSET:
            field_dict["resources"] = resources
        if security_context is not UNSET:
            field_dict["securityContext"] = security_context
        if readiness_probe is not UNSET:
            field_dict["readinessProbe"] = readiness_probe
        if liveness_probe is not UNSET:
            field_dict["livenessProbe"] = liveness_probe
        if startup_probe is not UNSET:
            field_dict["startupProbe"] = startup_probe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.env_var import EnvVar
        from ..models.probe import Probe
        from ..models.resource_quota import ResourceQuota
        from ..models.security_context import SecurityContext

        d = dict(src_dict)
        name = d.pop("name")

        image = d.pop("image")

        command = cast(list[str], d.pop("command", UNSET))

        args = cast(list[str], d.pop("args", UNSET))

        env = []
        _env = d.pop("env", UNSET)
        for env_item_data in _env or []:
            env_item = EnvVar.from_dict(env_item_data)

            env.append(env_item)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, ResourceQuota]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = ResourceQuota.from_dict(_resources)

        _security_context = d.pop("securityContext", UNSET)
        security_context: Union[Unset, SecurityContext]
        if isinstance(_security_context, Unset):
            security_context = UNSET
        else:
            security_context = SecurityContext.from_dict(_security_context)

        _readiness_probe = d.pop("readinessProbe", UNSET)
        readiness_probe: Union[Unset, Probe]
        if isinstance(_readiness_probe, Unset):
            readiness_probe = UNSET
        else:
            readiness_probe = Probe.from_dict(_readiness_probe)

        _liveness_probe = d.pop("livenessProbe", UNSET)
        liveness_probe: Union[Unset, Probe]
        if isinstance(_liveness_probe, Unset):
            liveness_probe = UNSET
        else:
            liveness_probe = Probe.from_dict(_liveness_probe)

        _startup_probe = d.pop("startupProbe", UNSET)
        startup_probe: Union[Unset, Probe]
        if isinstance(_startup_probe, Unset):
            startup_probe = UNSET
        else:
            startup_probe = Probe.from_dict(_startup_probe)

        sidecar_container_spec = cls(
            name=name,
            image=image,
            command=command,
            args=args,
            env=env,
            resources=resources,
            security_context=security_context,
            readiness_probe=readiness_probe,
            liveness_probe=liveness_probe,
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
