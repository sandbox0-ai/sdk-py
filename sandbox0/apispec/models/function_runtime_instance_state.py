from enum import Enum


class FunctionRuntimeInstanceState(str, Enum):
    DRAINING = "draining"
    FAILED = "failed"
    READY = "ready"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)
