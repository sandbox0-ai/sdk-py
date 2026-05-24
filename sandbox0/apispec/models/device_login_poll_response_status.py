from enum import Enum

class DeviceLoginPollResponseStatus(str, Enum):
    COMPLETED = "completed"
    PENDING = "pending"
    SLOW_DOWN = "slow_down"

    def __str__(self) -> str:
        return str(self.value)
