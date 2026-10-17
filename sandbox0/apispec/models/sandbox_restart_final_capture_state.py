from enum import Enum


class SandboxRestartFinalCaptureState(str, Enum):
    ACKNOWLEDGED = "acknowledged"
    PENDING = "pending"
    RELEASED = "released"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
