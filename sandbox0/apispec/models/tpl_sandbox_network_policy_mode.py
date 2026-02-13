from enum import Enum


class TplSandboxNetworkPolicyMode(str, Enum):
    ALLOW_ALL = "allow-all"
    BLOCK_ALL = "block-all"

    def __str__(self) -> str:
        return str(self.value)
