from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SandboxRestartFinalCaptureAcknowledgement")


@_attrs_define
class SandboxRestartFinalCaptureAcknowledgement:
    """
    Attributes:
        capture_id (str):
        receipt_id (str):
    """

    capture_id: str
    receipt_id: str

    def to_dict(self) -> dict[str, Any]:
        capture_id = self.capture_id

        receipt_id = self.receipt_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "capture_id": capture_id,
                "receipt_id": receipt_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        capture_id = d.pop("capture_id")

        receipt_id = d.pop("receipt_id")

        sandbox_restart_final_capture_acknowledgement = cls(
            capture_id=capture_id,
            receipt_id=receipt_id,
        )

        return sandbox_restart_final_capture_acknowledgement
