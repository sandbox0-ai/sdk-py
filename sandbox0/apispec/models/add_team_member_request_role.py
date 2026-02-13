from enum import Enum


class AddTeamMemberRequestRole(str, Enum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
