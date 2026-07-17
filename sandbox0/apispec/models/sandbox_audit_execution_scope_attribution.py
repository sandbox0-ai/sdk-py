from enum import Enum


class SandboxAuditExecutionScopeAttribution(str, Enum):
    PROCESS_ENVIRONMENT = "process_environment"

    def __str__(self) -> str:
        return str(self.value)
