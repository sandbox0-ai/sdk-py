from enum import Enum


class TemplateCreationStatusState(str, Enum):
    CREATING = "creating"
    FAILED = "failed"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
