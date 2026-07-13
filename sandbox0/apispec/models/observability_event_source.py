from enum import Enum


class ObservabilityEventSource(str, Enum):
    CLUSTER_GATEWAY = "cluster_gateway"
    CTLD = "ctld"
    MANAGER = "manager"
    NETD = "netd"
    PROCD = "procd"
    STORAGE_PROXY = "storage_proxy"

    def __str__(self) -> str:
        return str(self.value)
