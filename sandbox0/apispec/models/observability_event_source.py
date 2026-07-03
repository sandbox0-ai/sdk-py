from enum import Enum


class ObservabilityEventSource(str, Enum):
    MANAGER = "manager"
    NETD = "netd"
    PROCD = "procd"

    def __str__(self) -> str:
        return str(self.value)
