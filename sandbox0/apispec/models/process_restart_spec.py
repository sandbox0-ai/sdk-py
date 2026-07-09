from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_restart_spec_policy import ProcessRestartSpecPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessRestartSpec")


@_attrs_define
class ProcessRestartSpec:
    """
    Attributes:
        policy (Union[Unset, ProcessRestartSpecPolicy]):
        max_restarts (Union[Unset, int]):
    """

    policy: Union[Unset, ProcessRestartSpecPolicy] = UNSET
    max_restarts: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy: Union[Unset, str] = UNSET
        if not isinstance(self.policy, Unset):
            policy = self.policy.value

        max_restarts = self.max_restarts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if max_restarts is not UNSET:
            field_dict["max_restarts"] = max_restarts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _policy = d.pop("policy", UNSET)
        policy: Union[Unset, ProcessRestartSpecPolicy]
        if isinstance(_policy, Unset):
            policy = UNSET
        else:
            policy = ProcessRestartSpecPolicy(_policy)

        max_restarts = d.pop("max_restarts", UNSET)

        process_restart_spec = cls(
            policy=policy,
            max_restarts=max_restarts,
        )

        process_restart_spec.additional_properties = d
        return process_restart_spec

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
