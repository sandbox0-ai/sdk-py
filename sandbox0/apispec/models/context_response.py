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
    from ..models.context_response_env_vars import ContextResponseEnvVars


T = TypeVar("T", bound="ContextResponse")


@_attrs_define
class ContextResponse:
    """
    Attributes:
        id (str):
        type_ (ProcessType):
        running (bool):
        paused (bool):
        created_at (str):
        alias (Union[Unset, str]): Alias for the REPL or CLI tool (e.g., python, node, bash, redis-cli)
        cwd (Union[Unset, str]):
        env_vars (Union[Unset, ContextResponseEnvVars]):
        output_raw (Union[Unset, str]): Raw PTY output for CMD contexts with wait=true, may contain terminal control
            characters
    """

    id: str
    type_: ProcessType
    running: bool
    paused: bool
    created_at: str
    alias: Union[Unset, str] = UNSET
    cwd: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "ContextResponseEnvVars"] = UNSET
    output_raw: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        running = self.running

        paused = self.paused

        created_at = self.created_at

        alias = self.alias

        cwd = self.cwd

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        output_raw = self.output_raw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "running": running,
                "paused": paused,
                "created_at": created_at,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if output_raw is not UNSET:
            field_dict["output_raw"] = output_raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_response_env_vars import ContextResponseEnvVars

        d = dict(src_dict)
        id = d.pop("id")

        type_ = ProcessType(d.pop("type"))

        running = d.pop("running")

        paused = d.pop("paused")

        created_at = d.pop("created_at")

        alias = d.pop("alias", UNSET)

        cwd = d.pop("cwd", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, ContextResponseEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ContextResponseEnvVars.from_dict(_env_vars)

        output_raw = d.pop("output_raw", UNSET)

        context_response = cls(
            id=id,
            type_=type_,
            running=running,
            paused=paused,
            created_at=created_at,
            alias=alias,
            cwd=cwd,
            env_vars=env_vars,
            output_raw=output_raw,
        )

        context_response.additional_properties = d
        return context_response

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
