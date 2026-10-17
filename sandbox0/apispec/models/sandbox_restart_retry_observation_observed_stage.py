from enum import Enum


class SandboxRestartRetryObservationObservedStage(str, Enum):
    FAILED = "failed"
    PAUSED = "paused"
    PAUSING = "pausing"
    RESUMING = "resuming"
    SUCCEEDED = "succeeded"
    SUPERSEDED = "superseded"

    def __str__(self) -> str:
        return str(self.value)
