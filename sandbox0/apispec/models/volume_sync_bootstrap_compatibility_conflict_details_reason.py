from enum import Enum


class VolumeSyncBootstrapCompatibilityConflictDetailsReason(str, Enum):
    NAMESPACE_INCOMPATIBLE = "namespace_incompatible"

    def __str__(self) -> str:
        return str(self.value)
