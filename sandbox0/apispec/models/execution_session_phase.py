from enum import Enum


class ExecutionSessionPhase(str, Enum):
    BACKOFF = "backoff"
    EXITED = "exited"
    FAILED = "failed"
    PAUSED = "paused"
    PENDING = "pending"
    RUNNING = "running"
    STARTING = "starting"
    STOPPED = "stopped"
    STOPPING = "stopping"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
