from enum import Enum

class EgressAuthFailurePolicy(str, Enum):
    FAIL_CLOSED = "fail-closed"
    FAIL_OPEN = "fail-open"

    def __str__(self) -> str:
        return str(self.value)
