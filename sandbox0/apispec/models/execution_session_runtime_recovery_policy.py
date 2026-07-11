from enum import Enum


class ExecutionSessionRuntimeRecoveryPolicy(str, Enum):
    RESTART = "restart"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
