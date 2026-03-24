from enum import Enum


class GatewayMetadataGatewayMode(str, Enum):
    DIRECT = "direct"
    GLOBAL = "global"

    def __str__(self) -> str:
        return str(self.value)
