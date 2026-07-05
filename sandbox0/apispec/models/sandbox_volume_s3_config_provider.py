from enum import Enum


class SandboxVolumeS3ConfigProvider(str, Enum):
    ALI = "ali"
    AWS = "aws"
    R2 = "r2"

    def __str__(self) -> str:
        return str(self.value)
