from enum import IntEnum


class SandboxRootFSForkLaunchLifecycleEpoch(IntEnum):
    VALUE_1 = 1

    def __str__(self) -> str:
        return str(self.value)
