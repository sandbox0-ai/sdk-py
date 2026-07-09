from enum import Enum


class ProcessRestartSpecPolicy(str, Enum):
    NEVER = "never"

    def __str__(self) -> str:
        return str(self.value)
