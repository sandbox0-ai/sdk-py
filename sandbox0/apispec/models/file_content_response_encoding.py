from enum import Enum


class FileContentResponseEncoding(str, Enum):
    BASE64 = "base64"

    def __str__(self) -> str:
        return str(self.value)
