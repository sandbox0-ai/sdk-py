from enum import Enum


class ExecutionSessionWebSocketResizeType(str, Enum):
    RESIZE = "resize"

    def __str__(self) -> str:
        return str(self.value)
