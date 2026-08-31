from enum import Enum


class TemplateCreationStatusStage(str, Enum):
    CAPTURING = "capturing"
    PUBLISHING = "publishing"

    def __str__(self) -> str:
        return str(self.value)
