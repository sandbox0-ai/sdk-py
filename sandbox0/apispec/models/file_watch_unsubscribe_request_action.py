from enum import Enum


class FileWatchUnsubscribeRequestAction(str, Enum):
    UNSUBSCRIBE = "unsubscribe"

    def __str__(self) -> str:
        return str(self.value)
