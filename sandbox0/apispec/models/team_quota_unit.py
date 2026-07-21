from enum import Enum


class TeamQuotaUnit(str, Enum):
    BYTES = "bytes"
    CLAIMS = "claims"
    COUNT = "count"
    GB = "GB"
    REQUESTS = "requests"

    def __str__(self) -> str:
        return str(self.value)
