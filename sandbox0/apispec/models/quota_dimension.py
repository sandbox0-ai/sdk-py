from enum import Enum


class QuotaDimension(str, Enum):
    ACTIVE_SANDBOXES = "active_sandboxes"
    CPU_MILLICPU = "cpu_millicpu"
    EGRESS = "egress"
    INGRESS = "ingress"
    MEMORY_MIB = "memory_mib"
    SNAPSHOT_STORAGE_GB = "snapshot_storage_gb"
    VOLUME_STORAGE_GB = "volume_storage_gb"

    def __str__(self) -> str:
        return str(self.value)
