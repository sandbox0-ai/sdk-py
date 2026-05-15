from enum import Enum

class AddTeamMemberRequestRole(str, Enum):
    ADMIN = "admin"
    BUILDER = "builder"
    DEVELOPER = "developer"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
