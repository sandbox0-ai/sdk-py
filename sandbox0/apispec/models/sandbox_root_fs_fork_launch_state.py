from enum import Enum


class SandboxRootFSForkLaunchState(str, Enum):
    ABORTED = "aborted"
    COMPLETED = "completed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
