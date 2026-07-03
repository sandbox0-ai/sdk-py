from enum import Enum


class SandboxObservabilityEventType(str, Enum):
    LIFECYCLE = "lifecycle"
    NETWORK_AUDIT = "network_audit"
    RUNTIME_STATS = "runtime_stats"

    def __str__(self) -> str:
        return str(self.value)
