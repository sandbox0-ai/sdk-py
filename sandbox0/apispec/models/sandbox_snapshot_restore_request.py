from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SandboxSnapshotRestoreRequest")


@_attrs_define
class SandboxSnapshotRestoreRequest:
    """
    Attributes:
        expected_runtime_generation (int):
        snapshot_id (str):
        snapshot_generation_id (str):
        discard_process_state (bool): Explicit acknowledgement that old processes end and the selected snapshot replaces
            the current writable RootFS.
    """

    expected_runtime_generation: int
    snapshot_id: str
    snapshot_generation_id: str
    discard_process_state: bool

    def to_dict(self) -> dict[str, Any]:
        expected_runtime_generation = self.expected_runtime_generation

        snapshot_id = self.snapshot_id

        snapshot_generation_id = self.snapshot_generation_id

        discard_process_state = self.discard_process_state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expected_runtime_generation": expected_runtime_generation,
                "snapshot_id": snapshot_id,
                "snapshot_generation_id": snapshot_generation_id,
                "discard_process_state": discard_process_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_runtime_generation = d.pop("expected_runtime_generation")

        snapshot_id = d.pop("snapshot_id")

        snapshot_generation_id = d.pop("snapshot_generation_id")

        discard_process_state = d.pop("discard_process_state")

        sandbox_snapshot_restore_request = cls(
            expected_runtime_generation=expected_runtime_generation,
            snapshot_id=snapshot_id,
            snapshot_generation_id=snapshot_generation_id,
            discard_process_state=discard_process_state,
        )

        return sandbox_snapshot_restore_request
