from enum import Enum


class SeccompProfileType(str, Enum):
    LOCALHOST = "Localhost"
    RUNTIMEDEFAULT = "RuntimeDefault"
    UNCONFINED = "Unconfined"

    def __str__(self) -> str:
        return str(self.value)
