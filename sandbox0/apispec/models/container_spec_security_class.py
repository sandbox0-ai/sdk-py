from enum import Enum


class ContainerSpecSecurityClass(str, Enum):
    PRIVILEGED = "privileged"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
