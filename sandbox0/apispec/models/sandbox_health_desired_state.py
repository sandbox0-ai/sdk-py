from enum import Enum


class SandboxHealthDesiredState(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    TERMINATED = "terminated"

    def __str__(self) -> str:
        return str(self.value)
