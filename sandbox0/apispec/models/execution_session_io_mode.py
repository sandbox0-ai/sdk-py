from enum import Enum


class ExecutionSessionIOMode(str, Enum):
    PIPES = "pipes"
    PTY = "pty"

    def __str__(self) -> str:
        return str(self.value)
