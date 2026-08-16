from enum import Enum


class ObservabilityEventSource(str, Enum):
    CLUSTER_GATEWAY = "cluster_gateway"
    CTLD = "ctld"
    MANAGER = "manager"
    PROCD = "procd"

    def __str__(self) -> str:
        return str(self.value)
