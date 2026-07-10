from enum import Enum


class ExecutionSessionDesiredState(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
