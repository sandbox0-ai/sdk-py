from enum import Enum

class ProtocolRuleProtocol(str, Enum):
    MCP = "mcp"

    def __str__(self) -> str:
        return str(self.value)
