from enum import Enum


class ExecutionSessionWebSocketSignalType(str, Enum):
    SIGNAL = "signal"

    def __str__(self) -> str:
        return str(self.value)
