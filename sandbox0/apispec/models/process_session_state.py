from enum import Enum


class ProcessSessionState(str, Enum):
    CRASHED = "crashed"
    CREATED = "created"
    KILLED = "killed"
    PAUSED = "paused"
    RUNNING = "running"
    STARTING = "starting"
    STOPPED = "stopped"
    STOPPING = "stopping"

    def __str__(self) -> str:
        return str(self.value)
