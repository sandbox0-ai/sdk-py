from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_session_desired_state import ExecutionSessionDesiredState
from ..models.execution_session_runtime_recovery_policy import (
    ExecutionSessionRuntimeRecoveryPolicy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_session_restart_spec import ExecutionSessionRestartSpec


T = TypeVar("T", bound="ExecutionSessionLifecycleSpec")


@_attrs_define
class ExecutionSessionLifecycleSpec:
    """
    Attributes:
        desired_state (Union[Unset, ExecutionSessionDesiredState]):
        restart (Union[Unset, ExecutionSessionRestartSpec]):
        runtime_recovery (Union[Unset, ExecutionSessionRuntimeRecoveryPolicy]):
        idle_timeout_seconds (Union[Unset, int]):
        max_lifetime_seconds (Union[Unset, int]):
        stop_grace_period_seconds (Union[Unset, int]):  Default: 10.
    """

    desired_state: Union[Unset, ExecutionSessionDesiredState] = UNSET
    restart: Union[Unset, "ExecutionSessionRestartSpec"] = UNSET
    runtime_recovery: Union[Unset, ExecutionSessionRuntimeRecoveryPolicy] = UNSET
    idle_timeout_seconds: Union[Unset, int] = UNSET
    max_lifetime_seconds: Union[Unset, int] = UNSET
    stop_grace_period_seconds: Union[Unset, int] = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desired_state: Union[Unset, str] = UNSET
        if not isinstance(self.desired_state, Unset):
            desired_state = self.desired_state.value

        restart: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        runtime_recovery: Union[Unset, str] = UNSET
        if not isinstance(self.runtime_recovery, Unset):
            runtime_recovery = self.runtime_recovery.value

        idle_timeout_seconds = self.idle_timeout_seconds

        max_lifetime_seconds = self.max_lifetime_seconds

        stop_grace_period_seconds = self.stop_grace_period_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if desired_state is not UNSET:
            field_dict["desired_state"] = desired_state
        if restart is not UNSET:
            field_dict["restart"] = restart
        if runtime_recovery is not UNSET:
            field_dict["runtime_recovery"] = runtime_recovery
        if idle_timeout_seconds is not UNSET:
            field_dict["idle_timeout_seconds"] = idle_timeout_seconds
        if max_lifetime_seconds is not UNSET:
            field_dict["max_lifetime_seconds"] = max_lifetime_seconds
        if stop_grace_period_seconds is not UNSET:
            field_dict["stop_grace_period_seconds"] = stop_grace_period_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_session_restart_spec import ExecutionSessionRestartSpec

        d = dict(src_dict)
        _desired_state = d.pop("desired_state", UNSET)
        desired_state: Union[Unset, ExecutionSessionDesiredState]
        if isinstance(_desired_state, Unset):
            desired_state = UNSET
        else:
            desired_state = ExecutionSessionDesiredState(_desired_state)

        _restart = d.pop("restart", UNSET)
        restart: Union[Unset, ExecutionSessionRestartSpec]
        if isinstance(_restart, Unset):
            restart = UNSET
        else:
            restart = ExecutionSessionRestartSpec.from_dict(_restart)

        _runtime_recovery = d.pop("runtime_recovery", UNSET)
        runtime_recovery: Union[Unset, ExecutionSessionRuntimeRecoveryPolicy]
        if isinstance(_runtime_recovery, Unset):
            runtime_recovery = UNSET
        else:
            runtime_recovery = ExecutionSessionRuntimeRecoveryPolicy(_runtime_recovery)

        idle_timeout_seconds = d.pop("idle_timeout_seconds", UNSET)

        max_lifetime_seconds = d.pop("max_lifetime_seconds", UNSET)

        stop_grace_period_seconds = d.pop("stop_grace_period_seconds", UNSET)

        execution_session_lifecycle_spec = cls(
            desired_state=desired_state,
            restart=restart,
            runtime_recovery=runtime_recovery,
            idle_timeout_seconds=idle_timeout_seconds,
            max_lifetime_seconds=max_lifetime_seconds,
            stop_grace_period_seconds=stop_grace_period_seconds,
        )

        execution_session_lifecycle_spec.additional_properties = d
        return execution_session_lifecycle_spec

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
