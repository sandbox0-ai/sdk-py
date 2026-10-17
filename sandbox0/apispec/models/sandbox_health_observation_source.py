from enum import Enum


class SandboxHealthObservationSource(str, Enum):
    GUEST_DIAGNOSTIC = "guest_diagnostic"
    NODE_RUNTIME = "node_runtime"
    NONE = "none"
    REGIONAL_AUTHORITY = "regional_authority"

    def __str__(self) -> str:
        return str(self.value)
