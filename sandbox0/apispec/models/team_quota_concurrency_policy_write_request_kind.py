from enum import Enum


class TeamQuotaConcurrencyPolicyWriteRequestKind(str, Enum):
    CONCURRENCY = "concurrency"

    def __str__(self) -> str:
        return str(self.value)
