from enum import Enum


class VolumeSyncReseedRequiredDetailsReason(str, Enum):
    RESEED_REQUIRED = "reseed_required"

    def __str__(self) -> str:
        return str(self.value)
