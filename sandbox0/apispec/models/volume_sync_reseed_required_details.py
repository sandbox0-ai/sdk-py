from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volume_sync_reseed_required_details_reason import (
    VolumeSyncReseedRequiredDetailsReason,
)

T = TypeVar("T", bound="VolumeSyncReseedRequiredDetails")


@_attrs_define
class VolumeSyncReseedRequiredDetails:
    """
    Attributes:
        reason (VolumeSyncReseedRequiredDetailsReason):
        retained_after_seq (int):
        head_seq (int):
    """

    reason: VolumeSyncReseedRequiredDetailsReason
    retained_after_seq: int
    head_seq: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        retained_after_seq = self.retained_after_seq

        head_seq = self.head_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "retained_after_seq": retained_after_seq,
                "head_seq": head_seq,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = VolumeSyncReseedRequiredDetailsReason(d.pop("reason"))

        retained_after_seq = d.pop("retained_after_seq")

        head_seq = d.pop("head_seq")

        volume_sync_reseed_required_details = cls(
            reason=reason,
            retained_after_seq=retained_after_seq,
            head_seq=head_seq,
        )

        volume_sync_reseed_required_details.additional_properties = d
        return volume_sync_reseed_required_details

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
