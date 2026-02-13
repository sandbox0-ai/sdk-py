from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_type import ProcessType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_cmd_context_request import CreateCMDContextRequest
    from ..models.create_context_request_env_vars import CreateContextRequestEnvVars
    from ..models.create_repl_context_request import CreateREPLContextRequest
    from ..models.pty_size import PTYSize


T = TypeVar("T", bound="CreateContextRequest")


@_attrs_define
class CreateContextRequest:
    """
    Attributes:
        type_ (Union[Unset, ProcessType]):
        repl (Union[Unset, CreateREPLContextRequest]):
        cmd (Union[Unset, CreateCMDContextRequest]):
        wait_until_done (Union[Unset, bool]):
        cwd (Union[Unset, str]):
        env_vars (Union[Unset, CreateContextRequestEnvVars]):
        pty_size (Union[Unset, PTYSize]):
        idle_timeout_sec (Union[Unset, int]):
        ttl_sec (Union[Unset, int]):
    """

    type_: Union[Unset, ProcessType] = UNSET
    repl: Union[Unset, "CreateREPLContextRequest"] = UNSET
    cmd: Union[Unset, "CreateCMDContextRequest"] = UNSET
    wait_until_done: Union[Unset, bool] = UNSET
    cwd: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "CreateContextRequestEnvVars"] = UNSET
    pty_size: Union[Unset, "PTYSize"] = UNSET
    idle_timeout_sec: Union[Unset, int] = UNSET
    ttl_sec: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        repl: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.repl, Unset):
            repl = self.repl.to_dict()

        cmd: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd.to_dict()

        wait_until_done = self.wait_until_done

        cwd = self.cwd

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        pty_size: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pty_size, Unset):
            pty_size = self.pty_size.to_dict()

        idle_timeout_sec = self.idle_timeout_sec

        ttl_sec = self.ttl_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if repl is not UNSET:
            field_dict["repl"] = repl
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if wait_until_done is not UNSET:
            field_dict["wait_until_done"] = wait_until_done
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if pty_size is not UNSET:
            field_dict["pty_size"] = pty_size
        if idle_timeout_sec is not UNSET:
            field_dict["idle_timeout_sec"] = idle_timeout_sec
        if ttl_sec is not UNSET:
            field_dict["ttl_sec"] = ttl_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_cmd_context_request import CreateCMDContextRequest
        from ..models.create_context_request_env_vars import CreateContextRequestEnvVars
        from ..models.create_repl_context_request import CreateREPLContextRequest
        from ..models.pty_size import PTYSize

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ProcessType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProcessType(_type_)

        _repl = d.pop("repl", UNSET)
        repl: Union[Unset, CreateREPLContextRequest]
        if isinstance(_repl, Unset):
            repl = UNSET
        else:
            repl = CreateREPLContextRequest.from_dict(_repl)

        _cmd = d.pop("cmd", UNSET)
        cmd: Union[Unset, CreateCMDContextRequest]
        if isinstance(_cmd, Unset):
            cmd = UNSET
        else:
            cmd = CreateCMDContextRequest.from_dict(_cmd)

        wait_until_done = d.pop("wait_until_done", UNSET)

        cwd = d.pop("cwd", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, CreateContextRequestEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = CreateContextRequestEnvVars.from_dict(_env_vars)

        _pty_size = d.pop("pty_size", UNSET)
        pty_size: Union[Unset, PTYSize]
        if isinstance(_pty_size, Unset):
            pty_size = UNSET
        else:
            pty_size = PTYSize.from_dict(_pty_size)

        idle_timeout_sec = d.pop("idle_timeout_sec", UNSET)

        ttl_sec = d.pop("ttl_sec", UNSET)

        create_context_request = cls(
            type_=type_,
            repl=repl,
            cmd=cmd,
            wait_until_done=wait_until_done,
            cwd=cwd,
            env_vars=env_vars,
            pty_size=pty_size,
            idle_timeout_sec=idle_timeout_sec,
            ttl_sec=ttl_sec,
        )

        create_context_request.additional_properties = d
        return create_context_request

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
