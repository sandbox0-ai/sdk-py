from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_session_restart_policy import ExecutionSessionRestartPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionRestartSpec")


@_attrs_define
class ExecutionSessionRestartSpec:
    """
    Attributes:
        policy (Union[Unset, ExecutionSessionRestartPolicy]):
        max_restarts (Union[Unset, int]):  Default: 5.
        window_seconds (Union[Unset, int]):  Default: 60.
        initial_backoff_ms (Union[Unset, int]):  Default: 250.
        max_backoff_ms (Union[Unset, int]):  Default: 5000.
    """

    policy: Union[Unset, ExecutionSessionRestartPolicy] = UNSET
    max_restarts: Union[Unset, int] = 5
    window_seconds: Union[Unset, int] = 60
    initial_backoff_ms: Union[Unset, int] = 250
    max_backoff_ms: Union[Unset, int] = 5000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: Union[Unset, str] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        max_restarts = self.max_restarts

        window_seconds = self.window_seconds

        initial_backoff_ms = self.initial_backoff_ms

        max_backoff_ms = self.max_backoff_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if max_restarts is not UNSET:
            field_dict["max_restarts"] = max_restarts
        if window_seconds is not UNSET:
            field_dict["window_seconds"] = window_seconds
        if initial_backoff_ms is not UNSET:
            field_dict["initial_backoff_ms"] = initial_backoff_ms
        if max_backoff_ms is not UNSET:
            field_dict["max_backoff_ms"] = max_backoff_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ExecutionSessionRestartPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ExecutionSessionRestartPolicy(_policy)

        max_restarts = d.pop("max_restarts", UNSET)

        window_seconds = d.pop("window_seconds", UNSET)

        initial_backoff_ms = d.pop("initial_backoff_ms", UNSET)

        max_backoff_ms = d.pop("max_backoff_ms", UNSET)

        execution_session_restart_spec = cls(
            policy=policy,
            max_restarts=max_restarts,
            window_seconds=window_seconds,
            initial_backoff_ms=initial_backoff_ms,
            max_backoff_ms=max_backoff_ms,
        )

        execution_session_restart_spec.additional_properties = d
        return execution_session_restart_spec

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
