from enum import Enum


class CreateSandboxVolumeS3ConfigProvider(str, Enum):
    ALI = "ali"
    AWS = "aws"
    R2 = "r2"

    def __str__(self) -> str:
        return str(self.value)
