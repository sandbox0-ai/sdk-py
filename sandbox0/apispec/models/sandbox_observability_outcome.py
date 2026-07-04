from enum import Enum


class SandboxObservabilityOutcome(str, Enum):
    COMPLETED = "completed"
    DENIED = "denied"
    ERROR = "error"
    FAILED = "failed"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
