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
  from ..models.sandbox_function import SandboxFunction





T = TypeVar("T", bound="SandboxAppServiceRuntime")



@_attrs_define
class SandboxAppServiceRuntime:
    """ 
        Attributes:
            type_ (SandboxAppServiceRuntimeType): Runtime strategy for restarting a service process.
            command (Union[Unset, list[str]]): Process argv used when type is cmd.
            cwd (Union[Unset, str]):
            env_vars (Union[Unset, SandboxAppServiceRuntimeEnvVars]):
            function (Union[Unset, SandboxFunction]): Function code executed by procd for a sandbox service request.
                cluster-gateway owns public ingress and carries this source to procd.
     """

    type_: SandboxAppServiceRuntimeType
    command: Union[Unset, list[str]] = UNSET
    cwd: Union[Unset, str] = UNSET
    env_vars: Union[Unset, 'SandboxAppServiceRuntimeEnvVars'] = UNSET
    function: Union[Unset, 'SandboxFunction'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_app_service_runtime_env_vars import SandboxAppServiceRuntimeEnvVars
        from ..models.sandbox_function import SandboxFunction
        type_ = self.type_.value

        command: Union[Unset, list[str]] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command



        cwd = self.cwd

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        function: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.function, Unset):
            function = self.function.to_dict()


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
        if function is not UNSET:
            field_dict["function"] = function

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_app_service_runtime_env_vars import SandboxAppServiceRuntimeEnvVars
        from ..models.sandbox_function import SandboxFunction
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




        _function = d.pop("function", UNSET)
        function: Union[Unset, SandboxFunction]
        if isinstance(_function,  Unset):
            function = UNSET
        else:
            function = SandboxFunction.from_dict(_function)




        sandbox_app_service_runtime = cls(
            type_=type_,
            command=command,
            cwd=cwd,
            env_vars=env_vars,
            function=function,
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
