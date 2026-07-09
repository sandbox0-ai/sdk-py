from enum import Enum


class ProcessChannelKind(str, Enum):
    HTTP = "http"
    PTY = "pty"
    STDIO = "stdio"
    WEBSOCKET = "websocket"

    def __str__(self) -> str:
        return str(self.value)
