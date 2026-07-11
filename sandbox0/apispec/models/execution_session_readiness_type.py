from enum import Enum


class ExecutionSessionReadinessType(str, Enum):
    DELAY = "delay"
    OUTPUT = "output"
    PROCESS = "process"

    def __str__(self) -> str:
        return str(self.value)
