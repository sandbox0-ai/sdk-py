from enum import Enum


class ContextWebSocketResizeType(str, Enum):
    RESIZE = "resize"

    def __str__(self) -> str:
        return str(self.value)
