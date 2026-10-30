from enum import Enum


class SandboxAppServiceRuntimeType(str, Enum):
    CMD = "cmd"
    FUNCTION = "function"
    MANUAL = "manual"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
