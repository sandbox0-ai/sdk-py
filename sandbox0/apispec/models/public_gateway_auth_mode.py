from enum import Enum


class PublicGatewayAuthMode(str, Enum):
    BEARER = "bearer"
    HEADER = "header"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
