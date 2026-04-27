from enum import Enum


class CloneVolumeFileResultMode(str, Enum):
    COPY = "copy"
    COW = "cow"

    def __str__(self) -> str:
        return str(self.value)
