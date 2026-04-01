from enum import Enum


class SyncEventType(str, Enum):
    CHMOD = "chmod"
    CREATE = "create"
    INVALIDATE = "invalidate"
    REMOVE = "remove"
    RENAME = "rename"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
