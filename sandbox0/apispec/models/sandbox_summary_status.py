from enum import Enum


class SandboxSummaryStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    RUNNING = "running"
    STARTING = "starting"

    def __str__(self) -> str:
        return str(self.value)
