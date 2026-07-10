from enum import Enum


class ExecutionSessionRestartPolicy(str, Enum):
    ALWAYS = "always"
    NEVER = "never"
    ON_FAILURE = "on_failure"

    def __str__(self) -> str:
        return str(self.value)
