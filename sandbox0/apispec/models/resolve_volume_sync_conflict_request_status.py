from enum import Enum


class ResolveVolumeSyncConflictRequestStatus(str, Enum):
    IGNORED = "ignored"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
