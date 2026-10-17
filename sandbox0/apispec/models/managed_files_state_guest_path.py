from enum import Enum


class ManagedFilesStateGuestPath(str, Enum):
    VALUE_0 = "/run/sandbox0/credentials"

    def __str__(self) -> str:
        return str(self.value)
