from enum import Enum


class VolumeBackend(str, Enum):
    S0FS = "s0fs"
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
