from enum import Enum


class TeamQuotaCapacityPolicyWriteRequestKind(str, Enum):
    CAPACITY = "capacity"

    def __str__(self) -> str:
        return str(self.value)
