from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_power_state_desired import SandboxPowerStateDesired
from ..models.sandbox_power_state_observed import SandboxPowerStateObserved
from ..models.sandbox_power_state_phase import SandboxPowerStatePhase

T = TypeVar("T", bound="SandboxPowerState")


@_attrs_define
class SandboxPowerState:
    """
    Attributes:
        desired (SandboxPowerStateDesired):
        desired_generation (int):
        observed (SandboxPowerStateObserved):
        observed_generation (int):
        phase (SandboxPowerStatePhase):
    """

    desired: SandboxPowerStateDesired
    desired_generation: int
    observed: SandboxPowerStateObserved
    observed_generation: int
    phase: SandboxPowerStatePhase
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        desired = self.desired.value

        desired_generation = self.desired_generation

        observed = self.observed.value

        observed_generation = self.observed_generation

        phase = self.phase.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "desired": desired,
                "desired_generation": desired_generation,
                "observed": observed,
                "observed_generation": observed_generation,
                "phase": phase,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        desired = SandboxPowerStateDesired(d.pop("desired"))

        desired_generation = d.pop("desired_generation")

        observed = SandboxPowerStateObserved(d.pop("observed"))

        observed_generation = d.pop("observed_generation")

        phase = SandboxPowerStatePhase(d.pop("phase"))

        sandbox_power_state = cls(
            desired=desired,
            desired_generation=desired_generation,
            observed=observed,
            observed_generation=observed_generation,
            phase=phase,
        )

        sandbox_power_state.additional_properties = d
        return sandbox_power_state

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
