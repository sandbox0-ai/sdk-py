import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sandbox_restart_final_capture_state import SandboxRestartFinalCaptureState
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxRestartFinalCapture")


@_attrs_define
class SandboxRestartFinalCapture:
    """
    Attributes:
        operation_id (str):
        sandbox_id (str):
        from_runtime_generation (int):
        state (SandboxRestartFinalCaptureState):
        capture_id (Union[Unset, str]): Opaque immutable stopped-source identity, absent only while pending. No
            credential-content digest.
        stopped_at (Union[Unset, datetime.datetime]):
        receipt_id (Union[Unset, str]): Committed owner receipt, present only after acknowledgement.
    """

    operation_id: str
    sandbox_id: str
    from_runtime_generation: int
    state: SandboxRestartFinalCaptureState
    capture_id: Union[Unset, str] = UNSET
    stopped_at: Union[Unset, datetime.datetime] = UNSET
    receipt_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        sandbox_id = self.sandbox_id

        from_runtime_generation = self.from_runtime_generation

        state = self.state.value

        capture_id = self.capture_id

        stopped_at: Union[Unset, str] = UNSET
        if not isinstance(self.stopped_at, Unset):
            stopped_at = self.stopped_at.isoformat()

        receipt_id = self.receipt_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operation_id": operation_id,
                "sandbox_id": sandbox_id,
                "from_runtime_generation": from_runtime_generation,
                "state": state,
            }
        )
        if capture_id is not UNSET:
            field_dict["capture_id"] = capture_id
        if stopped_at is not UNSET:
            field_dict["stopped_at"] = stopped_at
        if receipt_id is not UNSET:
            field_dict["receipt_id"] = receipt_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operation_id")

        sandbox_id = d.pop("sandbox_id")

        from_runtime_generation = d.pop("from_runtime_generation")

        state = SandboxRestartFinalCaptureState(d.pop("state"))

        capture_id = d.pop("capture_id", UNSET)

        _stopped_at = d.pop("stopped_at", UNSET)
        stopped_at: Union[Unset, datetime.datetime]
        if isinstance(_stopped_at, Unset):
            stopped_at = UNSET
        else:
            stopped_at = isoparse(_stopped_at)

        receipt_id = d.pop("receipt_id", UNSET)

        sandbox_restart_final_capture = cls(
            operation_id=operation_id,
            sandbox_id=sandbox_id,
            from_runtime_generation=from_runtime_generation,
            state=state,
            capture_id=capture_id,
            stopped_at=stopped_at,
            receipt_id=receipt_id,
        )

        return sandbox_restart_final_capture
