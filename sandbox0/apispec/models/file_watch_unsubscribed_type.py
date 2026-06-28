from enum import Enum


class FileWatchUnsubscribedType(str, Enum):
    UNSUBSCRIBED = "unsubscribed"

    def __str__(self) -> str:
        return str(self.value)
