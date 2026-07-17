from enum import Enum


class SandboxObservabilityWatchLineType(str, Enum):
    ERROR = "error"
    EVENT = "event"
    HEARTBEAT = "heartbeat"
    LOG = "log"
    READY = "ready"
    WATERMARK = "watermark"

    def __str__(self) -> str:
        return str(self.value)
