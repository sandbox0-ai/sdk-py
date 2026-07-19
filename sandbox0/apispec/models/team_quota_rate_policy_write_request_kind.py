from enum import Enum


class TeamQuotaRatePolicyWriteRequestKind(str, Enum):
    RATE = "rate"

    def __str__(self) -> str:
        return str(self.value)
