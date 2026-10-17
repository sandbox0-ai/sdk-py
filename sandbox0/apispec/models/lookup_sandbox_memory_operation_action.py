from enum import Enum


class LookupSandboxMemoryOperationAction(str, Enum):
    PAUSE = "pause"
    RESUME = "resume"

    def __str__(self) -> str:
        return str(self.value)
