from enum import Enum


class SandboxObservabilityEventType(str, Enum):
    API_ACCESS = "api_access"
    FILE = "file"
    LIFECYCLE = "lifecycle"
    NETWORK_AUDIT = "network_audit"
    PROCESS = "process"
    RUNTIME_STATS = "runtime_stats"

    def __str__(self) -> str:
        return str(self.value)
