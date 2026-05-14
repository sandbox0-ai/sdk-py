from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sandbox_app_service_runtime_type import SandboxAppServiceRuntimeType
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sandbox_app_service_runtime_env_vars import SandboxAppServiceRuntimeEnvVars





T = TypeVar("T", bound="SandboxAppServiceRuntime")



@_attrs_define
class SandboxAppServiceRuntime:
    """ 
        Attributes:
            type_ (SandboxAppServiceRuntimeType):
            command (Union[Unset, list[str]]):
            cwd (Union[Unset, str]):
            env_vars (Union[Unset, SandboxAppServiceRuntimeEnvVars]):
            warm_process_name (Union[Unset, str]):
     """

    type_: SandboxAppServiceRuntimeType
    command: Union[Unset, list[str]] = UNSET
    cwd: Union[Unset, str] = UNSET
    env_vars: Union[Unset, 'SandboxAppServiceRuntimeEnvVars'] = UNSET
    warm_process_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_app_service_runtime_env_vars import SandboxAppServiceRuntimeEnvVars
        type_ = self.type_.value

        command: Union[Unset, list[str]] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command



        cwd = self.cwd

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        warm_process_name = self.warm_process_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if command is not UNSET:
            field_dict["command"] = command
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if warm_process_name is not UNSET:
            field_dict["warm_process_name"] = warm_process_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_app_service_runtime_env_vars import SandboxAppServiceRuntimeEnvVars
        d = dict(src_dict)
        type_ = SandboxAppServiceRuntimeType(d.pop("type"))




        command = cast(list[str], d.pop("command", UNSET))


        cwd = d.pop("cwd", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, SandboxAppServiceRuntimeEnvVars]
        if isinstance(_env_vars,  Unset):
            env_vars = UNSET
        else:
            env_vars = SandboxAppServiceRuntimeEnvVars.from_dict(_env_vars)




        warm_process_name = d.pop("warm_process_name", UNSET)

        sandbox_app_service_runtime = cls(
            type_=type_,
            command=command,
            cwd=cwd,
            env_vars=env_vars,
            warm_process_name=warm_process_name,
        )


        sandbox_app_service_runtime.additional_properties = d
        return sandbox_app_service_runtime

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
