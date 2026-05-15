from enum import Enum


class FileWatchSubscribedType(str, Enum):
    SUBSCRIBED = "subscribed"

    def __str__(self) -> str:
        return str(self.value)
