from enum import Enum


class ProcessType(str, Enum):
    CMD = "cmd"
    REPL = "repl"

    def __str__(self) -> str:
        return str(self.value)
