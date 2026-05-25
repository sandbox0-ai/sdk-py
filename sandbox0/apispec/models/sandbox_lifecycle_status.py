from enum import Enum

class SandboxLifecycleStatus(str, Enum):
    CLEANED = "cleaned"
    COMPLETED = "completed"
    FAILED = "failed"
    RUNNING = "running"
    STARTING = "starting"
    TERMINATING = "terminating"

    def __str__(self) -> str:
        return str(self.value)
