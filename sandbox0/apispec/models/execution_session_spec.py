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
    from ..models.execution_session_event_retention_spec import (
        ExecutionSessionEventRetentionSpec,
    )
    from ..models.execution_session_io_spec import ExecutionSessionIOSpec
    from ..models.execution_session_lifecycle_spec import ExecutionSessionLifecycleSpec
    from ..models.execution_session_readiness_spec import ExecutionSessionReadinessSpec
    from ..models.execution_session_scope_spec import ExecutionSessionScopeSpec
    from ..models.execution_session_spec_env import ExecutionSessionSpecEnv


T = TypeVar("T", bound="ExecutionSessionSpec")


@_attrs_define
class ExecutionSessionSpec:
    """Generic process-backed session specification. The supervisor does not interpret application protocols.

    Attributes:
        command (list[str]):
        name (Union[Unset, str]):
        cwd (Union[Unset, str]):
        env (Union[Unset, ExecutionSessionSpecEnv]):
        io (Union[Unset, ExecutionSessionIOSpec]):
        lifecycle (Union[Unset, ExecutionSessionLifecycleSpec]):
        readiness (Union[Unset, ExecutionSessionReadinessSpec]):
        event_retention (Union[Unset, ExecutionSessionEventRetentionSpec]):
        execution_scope (Union[Unset, ExecutionSessionScopeSpec]): Declares how descendants of this trusted supervisor
            process expose a
            logical execution scope. The runtime reads only the named environment
            variable and never exports the descendant process environment.
    """

    command: list[str]
    name: Union[Unset, str] = UNSET
    cwd: Union[Unset, str] = UNSET
    env: Union[Unset, "ExecutionSessionSpecEnv"] = UNSET
    io: Union[Unset, "ExecutionSessionIOSpec"] = UNSET
    lifecycle: Union[Unset, "ExecutionSessionLifecycleSpec"] = UNSET
    readiness: Union[Unset, "ExecutionSessionReadinessSpec"] = UNSET
    event_retention: Union[Unset, "ExecutionSessionEventRetentionSpec"] = UNSET
    execution_scope: Union[Unset, "ExecutionSessionScopeSpec"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        name = self.name

        cwd = self.cwd

        env: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        io: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.io, Unset):
            io = self.io.to_dict()

        lifecycle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.to_dict()

        readiness: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.readiness, Unset):
            readiness = self.readiness.to_dict()

        event_retention: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_retention, Unset):
            event_retention = self.event_retention.to_dict()

        execution_scope: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.execution_scope, Unset):
            execution_scope = self.execution_scope.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if env is not UNSET:
            field_dict["env"] = env
        if io is not UNSET:
            field_dict["io"] = io
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if readiness is not UNSET:
            field_dict["readiness"] = readiness
        if event_retention is not UNSET:
            field_dict["event_retention"] = event_retention
        if execution_scope is not UNSET:
            field_dict["execution_scope"] = execution_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_session_event_retention_spec import (
            ExecutionSessionEventRetentionSpec,
        )
        from ..models.execution_session_io_spec import ExecutionSessionIOSpec
        from ..models.execution_session_lifecycle_spec import (
            ExecutionSessionLifecycleSpec,
        )
        from ..models.execution_session_readiness_spec import (
            ExecutionSessionReadinessSpec,
        )
        from ..models.execution_session_scope_spec import ExecutionSessionScopeSpec
        from ..models.execution_session_spec_env import ExecutionSessionSpecEnv

        d = dict(src_dict)
        command = cast(list[str], d.pop("command"))

        name = d.pop("name", UNSET)

        cwd = d.pop("cwd", UNSET)

        _env = d.pop("env", UNSET)
        env: Union[Unset, ExecutionSessionSpecEnv]
        if isinstance(_env, Unset):
            env = UNSET
        else:
            env = ExecutionSessionSpecEnv.from_dict(_env)

        _io = d.pop("io", UNSET)
        io: Union[Unset, ExecutionSessionIOSpec]
        if isinstance(_io, Unset):
            io = UNSET
        else:
            io = ExecutionSessionIOSpec.from_dict(_io)

        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: Union[Unset, ExecutionSessionLifecycleSpec]
        if isinstance(_lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = ExecutionSessionLifecycleSpec.from_dict(_lifecycle)

        _readiness = d.pop("readiness", UNSET)
        readiness: Union[Unset, ExecutionSessionReadinessSpec]
        if isinstance(_readiness, Unset):
            readiness = UNSET
        else:
            readiness = ExecutionSessionReadinessSpec.from_dict(_readiness)

        _event_retention = d.pop("event_retention", UNSET)
        event_retention: Union[Unset, ExecutionSessionEventRetentionSpec]
        if isinstance(_event_retention, Unset):
            event_retention = UNSET
        else:
            event_retention = ExecutionSessionEventRetentionSpec.from_dict(
                _event_retention
            )

        _execution_scope = d.pop("execution_scope", UNSET)
        execution_scope: Union[Unset, ExecutionSessionScopeSpec]
        if isinstance(_execution_scope, Unset):
            execution_scope = UNSET
        else:
            execution_scope = ExecutionSessionScopeSpec.from_dict(_execution_scope)

        execution_session_spec = cls(
            command=command,
            name=name,
            cwd=cwd,
            env=env,
            io=io,
            lifecycle=lifecycle,
            readiness=readiness,
            event_retention=event_retention,
            execution_scope=execution_scope,
        )

        execution_session_spec.additional_properties = d
        return execution_session_spec

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
