from enum import Enum


class WarmProcessSpecType(str, Enum):
    CMD = "cmd"
    REPL = "repl"

    def __str__(self) -> str:
        return str(self.value)
