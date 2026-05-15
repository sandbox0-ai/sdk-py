from enum import Enum


class SandboxAppServiceRouteAuthMode(str, Enum):
    BEARER = "bearer"
    HEADER = "header"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
