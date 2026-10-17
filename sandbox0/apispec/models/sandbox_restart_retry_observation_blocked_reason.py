from enum import Enum


class SandboxRestartRetryObservationBlockedReason(str, Enum):
    ATTEMPT_TIMED_OUT = "attempt_timed_out"
    CAPACITY_UNAVAILABLE = "capacity_unavailable"
    CONTROL_PLANE_UNAVAILABLE = "control_plane_unavailable"
    LAUNCH_PENDING = "launch_pending"
    QUOTA_EXCEEDED = "quota_exceeded"
    RETIREMENT_PENDING = "retirement_pending"
    RUNTIME_UNAVAILABLE = "runtime_unavailable"
    STORAGE_NOT_WRITABLE = "storage_not_writable"

    def __str__(self) -> str:
        return str(self.value)
