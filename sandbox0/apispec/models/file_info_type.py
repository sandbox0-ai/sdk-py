from enum import Enum


class FileInfoType(str, Enum):
    DIR = "dir"
    FILE = "file"
    SYMLINK = "symlink"

    def __str__(self) -> str:
        return str(self.value)
