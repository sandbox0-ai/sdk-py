from enum import Enum


class SandboxAuditEventPhase(str, Enum):
    ATTEMPT = "attempt"
    EFFECT = "effect"
    RESULT = "result"

    def __str__(self) -> str:
        return str(self.value)
