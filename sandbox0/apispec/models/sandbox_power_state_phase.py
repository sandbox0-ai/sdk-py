from enum import Enum

class SandboxPowerStatePhase(str, Enum):
    PAUSING = "pausing"
    RESUMING = "resuming"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
