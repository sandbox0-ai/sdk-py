from enum import Enum


class SandboxAuditIntegritySignatureStatus(str, Enum):
    INVALID = "invalid"
    UNAVAILABLE = "unavailable"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
