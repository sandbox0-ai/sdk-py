from enum import Enum


class QuotaDimension(str, Enum):
    ACTIVE_SANDBOXES = "active_sandboxes"
    API_REQUESTS = "api_requests"
    CPU_MILLICPU = "cpu_millicpu"
    MEMORY_MIB = "memory_mib"
    NETWORK_EGRESS_BYTES = "network_egress_bytes"
    NETWORK_INGRESS_BYTES = "network_ingress_bytes"
    SNAPSHOT_STORAGE_GB = "snapshot_storage_gb"
    VOLUME_STORAGE_GB = "volume_storage_gb"

    def __str__(self) -> str:
        return str(self.value)
