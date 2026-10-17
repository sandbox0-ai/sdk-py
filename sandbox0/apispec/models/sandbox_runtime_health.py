from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sandbox_health_observation import SandboxHealthObservation


T = TypeVar("T", bound="SandboxRuntimeHealth")


@_attrs_define
class SandboxRuntimeHealth:
    """
    Attributes:
        launch_authority (SandboxHealthObservation):
        liveness (SandboxHealthObservation):
    """

    launch_authority: "SandboxHealthObservation"
    liveness: "SandboxHealthObservation"

    def to_dict(self) -> dict[str, Any]:
        launch_authority = self.launch_authority.to_dict()

        liveness = self.liveness.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "launch_authority": launch_authority,
                "liveness": liveness,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_health_observation import SandboxHealthObservation

        d = dict(src_dict)
        launch_authority = SandboxHealthObservation.from_dict(d.pop("launch_authority"))

        liveness = SandboxHealthObservation.from_dict(d.pop("liveness"))

        sandbox_runtime_health = cls(
            launch_authority=launch_authority,
            liveness=liveness,
        )

        return sandbox_runtime_health
