from enum import Enum


class ProcessChannelFraming(str, Enum):
    JSONL = "jsonl"
    JSONRPC = "jsonrpc"
    LINE = "line"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
