from enum import Enum


class TemplateCreationStatusStage(str, Enum):
    CAPTURING = "capturing"
    PUBLISHING = "publishing"
    RECONCILING = "reconciling"

    def __str__(self) -> str:
        return str(self.value)
