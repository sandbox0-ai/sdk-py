from enum import Enum


class TeamQuotaUnit(str, Enum):
    BYTES = "bytes"
    COUNT = "count"
    MILLICORES = "millicores"
    OPERATIONS = "operations"
    REQUESTS = "requests"

    def __str__(self) -> str:
        return str(self.value)
