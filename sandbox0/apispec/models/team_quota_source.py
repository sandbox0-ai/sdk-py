from enum import Enum


class TeamQuotaSource(str, Enum):
    REGION_DEFAULT = "region_default"
    TEAM_OVERRIDE = "team_override"
    UNLIMITED = "unlimited"

    def __str__(self) -> str:
        return str(self.value)
