from enum import Enum


class ContainerSpecSecurityClass(str, Enum):
    PRIVILEGED = "privileged"

    def __str__(self) -> str:
        return str(self.value)
