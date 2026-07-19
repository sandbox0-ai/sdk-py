from enum import Enum


class TeamQuotaKind(str, Enum):
    CAPACITY = "capacity"
    CONCURRENCY = "concurrency"
    RATE = "rate"

    def __str__(self) -> str:
        return str(self.value)
