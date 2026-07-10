from enum import Enum


class ExecutionSessionWebSocketInputType(str, Enum):
    INPUT = "input"

    def __str__(self) -> str:
        return str(self.value)
