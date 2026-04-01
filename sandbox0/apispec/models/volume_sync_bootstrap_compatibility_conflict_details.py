from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volume_sync_bootstrap_compatibility_conflict_details_reason import (
    VolumeSyncBootstrapCompatibilityConflictDetailsReason,
)

if TYPE_CHECKING:
    from ..models.volume_sync_compatibility_issue import VolumeSyncCompatibilityIssue
    from ..models.volume_sync_filesystem_capabilities import (
        VolumeSyncFilesystemCapabilities,
    )


T = TypeVar("T", bound="VolumeSyncBootstrapCompatibilityConflictDetails")


@_attrs_define
class VolumeSyncBootstrapCompatibilityConflictDetails:
    """
    Attributes:
        reason (VolumeSyncBootstrapCompatibilityConflictDetailsReason):
        snapshot_id (str):
        capabilities (VolumeSyncFilesystemCapabilities):
        issues (list['VolumeSyncCompatibilityIssue']):
    """

    reason: VolumeSyncBootstrapCompatibilityConflictDetailsReason
    snapshot_id: str
    capabilities: "VolumeSyncFilesystemCapabilities"
    issues: list["VolumeSyncCompatibilityIssue"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason.value

        snapshot_id = self.snapshot_id

        capabilities = self.capabilities.to_dict()

        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "snapshot_id": snapshot_id,
                "capabilities": capabilities,
                "issues": issues,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume_sync_compatibility_issue import (
            VolumeSyncCompatibilityIssue,
        )
        from ..models.volume_sync_filesystem_capabilities import (
            VolumeSyncFilesystemCapabilities,
        )

        d = dict(src_dict)
        reason = VolumeSyncBootstrapCompatibilityConflictDetailsReason(d.pop("reason"))

        snapshot_id = d.pop("snapshot_id")

        capabilities = VolumeSyncFilesystemCapabilities.from_dict(d.pop("capabilities"))

        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = VolumeSyncCompatibilityIssue.from_dict(issues_item_data)

            issues.append(issues_item)

        volume_sync_bootstrap_compatibility_conflict_details = cls(
            reason=reason,
            snapshot_id=snapshot_id,
            capabilities=capabilities,
            issues=issues,
        )

        volume_sync_bootstrap_compatibility_conflict_details.additional_properties = d
        return volume_sync_bootstrap_compatibility_conflict_details

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
