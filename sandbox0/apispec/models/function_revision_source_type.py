from enum import Enum

class FunctionRevisionSourceType(str, Enum):
    ARTIFACT = "artifact"
    REVISION_SPEC = "revision_spec"
    SANDBOX_SERVICE = "sandbox_service"

    def __str__(self) -> str:
        return str(self.value)
