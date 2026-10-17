from enum import Enum


class SandboxMemoryOperationReason(str, Enum):
    BEFORE_CAPTURE = "before_capture"
    BEFORE_RESTORE = "before_restore"
    CAPTURE_FAILED = "capture_failed"
    RESTORE_FAILED = "restore_failed"

    def __str__(self) -> str:
        return str(self.value)
