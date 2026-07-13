from enum import Enum


class SandboxAuditIntegrityAlgorithm(str, Enum):
    ED25519_SHA256_V1 = "ed25519-sha256-v1"

    def __str__(self) -> str:
        return str(self.value)
