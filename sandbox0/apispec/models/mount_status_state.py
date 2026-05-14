from enum import Enum

class MountStatusState(str, Enum):
    FAILED = "failed"
    MOUNTED = "mounted"
    MOUNTING = "mounting"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
