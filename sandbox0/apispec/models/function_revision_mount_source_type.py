from enum import Enum

class FunctionRevisionMountSourceType(str, Enum):
    ARTIFACT = "artifact"
    SANDBOX_VOLUME = "sandbox_volume"
    VOLUME_SNAPSHOT = "volume_snapshot"

    def __str__(self) -> str:
        return str(self.value)
