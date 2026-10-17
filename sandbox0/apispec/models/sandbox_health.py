import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sandbox_health_desired_state import SandboxHealthDesiredState

if TYPE_CHECKING:
    from ..models.sandbox_health_observation import SandboxHealthObservation
    from ..models.sandbox_runtime_health import SandboxRuntimeHealth
    from ..models.sandbox_storage_health import SandboxStorageHealth


T = TypeVar("T", bound="SandboxHealth")


@_attrs_define
class SandboxHealth:
    """
    Attributes:
        sandbox_id (str):
        runtime_generation (int):
        lifecycle_epoch (int):
        desired_state (SandboxHealthDesiredState):
        active_lifecycle (bool):
        observed_at (datetime.datetime): Latest regional authority snapshot time; individual checks retain their own
            observation time.
        runtime (SandboxRuntimeHealth):
        execution (SandboxHealthObservation):
        terminal (SandboxHealthObservation):
        storage (SandboxStorageHealth):
    """

    sandbox_id: str
    runtime_generation: int
    lifecycle_epoch: int
    desired_state: SandboxHealthDesiredState
    active_lifecycle: bool
    observed_at: datetime.datetime
    runtime: "SandboxRuntimeHealth"
    execution: "SandboxHealthObservation"
    terminal: "SandboxHealthObservation"
    storage: "SandboxStorageHealth"

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        runtime_generation = self.runtime_generation

        lifecycle_epoch = self.lifecycle_epoch

        desired_state = self.desired_state.value

        active_lifecycle = self.active_lifecycle

        observed_at = self.observed_at.isoformat()

        runtime = self.runtime.to_dict()

        execution = self.execution.to_dict()

        terminal = self.terminal.to_dict()

        storage = self.storage.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "runtime_generation": runtime_generation,
                "lifecycle_epoch": lifecycle_epoch,
                "desired_state": desired_state,
                "active_lifecycle": active_lifecycle,
                "observed_at": observed_at,
                "runtime": runtime,
                "execution": execution,
                "terminal": terminal,
                "storage": storage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_health_observation import SandboxHealthObservation
        from ..models.sandbox_runtime_health import SandboxRuntimeHealth
        from ..models.sandbox_storage_health import SandboxStorageHealth

        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        runtime_generation = d.pop("runtime_generation")

        lifecycle_epoch = d.pop("lifecycle_epoch")

        desired_state = SandboxHealthDesiredState(d.pop("desired_state"))

        active_lifecycle = d.pop("active_lifecycle")

        observed_at = isoparse(d.pop("observed_at"))

        runtime = SandboxRuntimeHealth.from_dict(d.pop("runtime"))

        execution = SandboxHealthObservation.from_dict(d.pop("execution"))

        terminal = SandboxHealthObservation.from_dict(d.pop("terminal"))

        storage = SandboxStorageHealth.from_dict(d.pop("storage"))

        sandbox_health = cls(
            sandbox_id=sandbox_id,
            runtime_generation=runtime_generation,
            lifecycle_epoch=lifecycle_epoch,
            desired_state=desired_state,
            active_lifecycle=active_lifecycle,
            observed_at=observed_at,
            runtime=runtime,
            execution=execution,
            terminal=terminal,
            storage=storage,
        )

        return sandbox_health
