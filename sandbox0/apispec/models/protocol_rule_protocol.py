from enum import Enum


class ProtocolRuleProtocol(str, Enum):
    HTTP = "http"
    MCP = "mcp"

    def __str__(self) -> str:
        return str(self.value)
