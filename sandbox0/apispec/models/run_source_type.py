from enum import Enum

class RunSourceType(str, Enum):
    SANDBOX_SERVICE = "sandbox_service"
    SNAPSHOT = "snapshot"

    def __str__(self) -> str:
        return str(self.value)
