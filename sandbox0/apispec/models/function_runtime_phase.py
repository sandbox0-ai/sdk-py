from enum import Enum


class FunctionRuntimePhase(str, Enum):
    DISABLED = "disabled"
    DRAINING = "draining"
    FAILED = "failed"
    IDLE = "idle"
    PROVISIONING = "provisioning"
    READY = "ready"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)
