from enum import Enum


class SandboxObservabilityOutcome(str, Enum):
    ACCEPTED = "accepted"
    COMPLETED = "completed"
    DENIED = "denied"
    ERROR = "error"
    FAILED = "failed"
    SUCCEEDED = "succeeded"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
