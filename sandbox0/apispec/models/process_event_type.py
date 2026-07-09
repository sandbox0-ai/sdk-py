from enum import Enum


class ProcessEventType(str, Enum):
    CURSOR_LOST = "cursor_lost"
    ERROR = "error"
    HTTP_REQUEST = "http.request"
    HTTP_RESPONSE = "http.response"
    PROCESS_CRASHED = "process.crashed"
    PROCESS_EXITED = "process.exited"
    PROCESS_STARTED = "process.started"
    PROCESS_STOPPED = "process.stopped"
    PTY_INPUT = "pty.input"
    PTY_OUTPUT = "pty.output"
    STDERR_CHUNK = "stderr.chunk"
    STDERR_LINE = "stderr.line"
    STDIN_WRITE = "stdin.write"
    STDOUT_CHUNK = "stdout.chunk"
    STDOUT_LINE = "stdout.line"
    WEBSOCKET_CLOSE = "websocket.close"
    WEBSOCKET_MESSAGE = "websocket.message"
    WEBSOCKET_OPEN = "websocket.open"

    def __str__(self) -> str:
        return str(self.value)
