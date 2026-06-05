from enum import Enum

class AppArmorProfileType(str, Enum):
    LOCALHOST = "Localhost"
    RUNTIMEDEFAULT = "RuntimeDefault"
    UNCONFINED = "Unconfined"

    def __str__(self) -> str:
        return str(self.value)
