from enum import Enum


class FileWatchEventType(str, Enum):
    EVENT = "event"

    def __str__(self) -> str:
        return str(self.value)
