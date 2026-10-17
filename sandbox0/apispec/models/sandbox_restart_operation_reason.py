from enum import Enum


class SandboxRestartOperationReason(str, Enum):
    PAUSE_ABORTED = "pause_aborted"
    RESUME_ABORTED = "resume_aborted"
    SOURCE_CHANGED = "source_changed"

    def __str__(self) -> str:
        return str(self.value)
