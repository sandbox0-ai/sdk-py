from enum import Enum

class FunctionRevisionStatus(str, Enum):
    ACTIVE = "active"
    CREATED = "created"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
