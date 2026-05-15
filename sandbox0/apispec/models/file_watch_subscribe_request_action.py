from enum import Enum


class FileWatchSubscribeRequestAction(str, Enum):
    SUBSCRIBE = "subscribe"

    def __str__(self) -> str:
        return str(self.value)
