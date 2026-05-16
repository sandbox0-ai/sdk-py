from enum import Enum


class FunctionRuntimeState(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    IDLE = "idle"

    def __str__(self) -> str:
        return str(self.value)
