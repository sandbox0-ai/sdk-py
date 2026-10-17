import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.sandbox_memory_restoration_step import SandboxMemoryRestorationStep


T = TypeVar("T", bound="SandboxMemoryRestoration")


@_attrs_define
class SandboxMemoryRestoration:
    """
    Attributes:
        sandbox_id (str):
        runtime_generation (int):
        runtime_compatibility_digest (str):
        filesystem_id (str):
        steps (list['SandboxMemoryRestorationStep']): Oldest to newest contiguous memory restorations. Capture
            generation can precede failed restore attempts; do not infer from generation + 1. Bind the first capture
            generation to owned publication/session history.
        observed_at (datetime.datetime):
    """

    sandbox_id: str
    runtime_generation: int
    runtime_compatibility_digest: str
    filesystem_id: str
    steps: list["SandboxMemoryRestorationStep"]
    observed_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        runtime_generation = self.runtime_generation

        runtime_compatibility_digest = self.runtime_compatibility_digest

        filesystem_id = self.filesystem_id

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        observed_at = self.observed_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "runtime_generation": runtime_generation,
                "runtime_compatibility_digest": runtime_compatibility_digest,
                "filesystem_id": filesystem_id,
                "steps": steps,
                "observed_at": observed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_memory_restoration_step import (
            SandboxMemoryRestorationStep,
        )

        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        runtime_generation = d.pop("runtime_generation")

        runtime_compatibility_digest = d.pop("runtime_compatibility_digest")

        filesystem_id = d.pop("filesystem_id")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = SandboxMemoryRestorationStep.from_dict(steps_item_data)

            steps.append(steps_item)

        observed_at = isoparse(d.pop("observed_at"))

        sandbox_memory_restoration = cls(
            sandbox_id=sandbox_id,
            runtime_generation=runtime_generation,
            runtime_compatibility_digest=runtime_compatibility_digest,
            filesystem_id=filesystem_id,
            steps=steps,
            observed_at=observed_at,
        )

        return sandbox_memory_restoration
