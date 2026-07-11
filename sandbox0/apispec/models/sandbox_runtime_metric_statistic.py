from enum import Enum


class SandboxRuntimeMetricStatistic(str, Enum):
    AUTO = "auto"
    AVERAGE = "average"
    LAST = "last"
    MAXIMUM = "maximum"
    MINIMUM = "minimum"
    RATE = "rate"

    def __str__(self) -> str:
        return str(self.value)
