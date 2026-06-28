from enum import Enum


class SandboxLifecycleStatus(str, Enum):
    FAILED = "failed"
    PAUSED = "paused"
    RUNNING = "running"
    STARTING = "starting"
    TERMINATING = "terminating"

    def __str__(self) -> str:
        return str(self.value)
