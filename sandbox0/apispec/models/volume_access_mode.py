from enum import Enum


class VolumeAccessMode(str, Enum):
    ROX = "ROX"
    RWO = "RWO"
    RWX = "RWX"

    def __str__(self) -> str:
        return str(self.value)
