from enum import Enum


class CloneVolumeFilesRequestMode(str, Enum):
    COPY = "copy"
    COW_OR_COPY = "cow_or_copy"
    COW_REQUIRED = "cow_required"

    def __str__(self) -> str:
        return str(self.value)
