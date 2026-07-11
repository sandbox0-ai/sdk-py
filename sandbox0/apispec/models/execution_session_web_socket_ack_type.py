from enum import Enum


class ExecutionSessionWebSocketAckType(str, Enum):
    ACK = "ack"

    def __str__(self) -> str:
        return str(self.value)
