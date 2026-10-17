from enum import Enum


class SandboxHealthObservationState(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
