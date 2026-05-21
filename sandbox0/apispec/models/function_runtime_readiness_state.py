from enum import Enum

class FunctionRuntimeReadinessState(str, Enum):
    CHECKING = "checking"
    FAILED = "failed"
    READY = "ready"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
