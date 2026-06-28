from enum import Enum


class ContextWebSocketOutputSource(str, Enum):
    PTY = "pty"
    STDERR = "stderr"
    STDOUT = "stdout"

    def __str__(self) -> str:
        return str(self.value)
