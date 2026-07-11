from enum import Enum


class SandboxRuntimeMetricUnit(str, Enum):
    BYTES = "bytes"
    BYTES_PER_SECOND = "bytes_per_second"
    CORES = "cores"
    COUNT = "count"
    COUNT_PER_SECOND = "count_per_second"
    RATIO = "ratio"
    SECONDS = "seconds"

    def __str__(self) -> str:
        return str(self.value)
