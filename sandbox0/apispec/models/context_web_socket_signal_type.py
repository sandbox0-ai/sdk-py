from enum import Enum


class ContextWebSocketSignalType(str, Enum):
    SIGNAL = "signal"

    def __str__(self) -> str:
        return str(self.value)
