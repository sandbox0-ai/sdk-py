from enum import Enum


class TeamQuotaUnit(str, Enum):
    BYTES = "bytes"
    COUNT = "count"
    GB = "GB"
    MIB = "MiB"
    MILLICPU = "millicpu"
    REQUESTS = "requests"

    def __str__(self) -> str:
        return str(self.value)
