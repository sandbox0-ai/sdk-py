from enum import Enum


class SandboxMemoryOperationAction(str, Enum):
    PAUSE = "pause"
    RESUME = "resume"

    def __str__(self) -> str:
        return str(self.value)
