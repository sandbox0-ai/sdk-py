from enum import Enum


class REPLReadyMode(str, Enum):
    PROMPT_TOKEN = "prompt_token"
    STARTUP_DELAY = "startup_delay"

    def __str__(self) -> str:
        return str(self.value)
