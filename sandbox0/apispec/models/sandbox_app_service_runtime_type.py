from enum import Enum

class SandboxAppServiceRuntimeType(str, Enum):
    CMD = "cmd"
    FUNCTION = "function"
    MANUAL = "manual"
    WARM_PROCESS = "warm_process"

    def __str__(self) -> str:
        return str(self.value)
