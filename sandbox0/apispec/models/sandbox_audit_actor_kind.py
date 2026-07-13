from enum import Enum


class SandboxAuditActorKind(str, Enum):
    ANONYMOUS = "anonymous"
    API_KEY = "api_key"
    EXPOSURE_CREDENTIAL = "exposure_credential"
    HUMAN = "human"
    SANDBOX_WORKLOAD = "sandbox_workload"
    SERVICE = "service"
    SSH_USER = "ssh_user"

    def __str__(self) -> str:
        return str(self.value)
