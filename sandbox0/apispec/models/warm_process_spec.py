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

from ..models.warm_process_spec_type import WarmProcessSpecType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_probe_set import SandboxProbeSet
    from ..models.warm_process_spec_env_vars import WarmProcessSpecEnvVars


T = TypeVar("T", bound="WarmProcessSpec")


@_attrs_define
class WarmProcessSpec:
    """
    Attributes:
        type_ (WarmProcessSpecType):
        name (Union[Unset, str]):
        alias (Union[Unset, str]):
        command (Union[Unset, list[str]]):
        cwd (Union[Unset, str]):
        env_vars (Union[Unset, WarmProcessSpecEnvVars]):
        probes (Union[Unset, SandboxProbeSet]):
    """

    type_: WarmProcessSpecType
    name: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    command: Union[Unset, list[str]] = UNSET
    cwd: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "WarmProcessSpecEnvVars"] = UNSET
    probes: Union[Unset, "SandboxProbeSet"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        alias = self.alias

        command: Union[Unset, list[str]] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command

        cwd = self.cwd

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        probes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.probes, Unset):
            probes = self.probes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if alias is not UNSET:
            field_dict["alias"] = alias
        if command is not UNSET:
            field_dict["command"] = command
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if env_vars is not UNSET:
            field_dict["envVars"] = env_vars
        if probes is not UNSET:
            field_dict["probes"] = probes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_probe_set import SandboxProbeSet
        from ..models.warm_process_spec_env_vars import WarmProcessSpecEnvVars

        d = dict(src_dict)
        type_ = WarmProcessSpecType(d.pop("type"))

        name = d.pop("name", UNSET)

        alias = d.pop("alias", UNSET)

        command = cast(list[str], d.pop("command", UNSET))

        cwd = d.pop("cwd", UNSET)

        _env_vars = d.pop("envVars", UNSET)
        env_vars: Union[Unset, WarmProcessSpecEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = WarmProcessSpecEnvVars.from_dict(_env_vars)

        _probes = d.pop("probes", UNSET)
        probes: Union[Unset, SandboxProbeSet]
        if isinstance(_probes, Unset):
            probes = UNSET
        else:
            probes = SandboxProbeSet.from_dict(_probes)

        warm_process_spec = cls(
            type_=type_,
            name=name,
            alias=alias,
            command=command,
            cwd=cwd,
            env_vars=env_vars,
            probes=probes,
        )

        warm_process_spec.additional_properties = d
        return warm_process_spec

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
