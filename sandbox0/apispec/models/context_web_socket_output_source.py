from enum import Enum


class ContextWebSocketOutputSource(str, Enum):
    PROMPT = "prompt"
    STDERR = "stderr"
    STDOUT = "stdout"

    def __str__(self) -> str:
        return str(self.value)
