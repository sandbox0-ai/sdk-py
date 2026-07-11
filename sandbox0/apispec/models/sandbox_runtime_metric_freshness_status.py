from enum import Enum


class SandboxRuntimeMetricFreshnessStatus(str, Enum):
    FRESH = "fresh"
    MISSING = "missing"
    STALE = "stale"

    def __str__(self) -> str:
        return str(self.value)
