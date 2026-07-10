from enum import Enum


class SandboxRuntimeMetricKind(str, Enum):
    COUNTER = "counter"
    GAUGE = "gauge"

    def __str__(self) -> str:
        return str(self.value)
