from enum import Enum

class SandboxFunctionRuntime(str, Enum):
    PYTHON = "python"

    def __str__(self) -> str:
        return str(self.value)
