from enum import Enum


class TeamQuotaPolicySource(str, Enum):
    DEFAULT = "default"
    OVERRIDE = "override"

    def __str__(self) -> str:
        return str(self.value)
