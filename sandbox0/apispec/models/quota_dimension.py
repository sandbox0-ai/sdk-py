from enum import Enum


class QuotaDimension(str, Enum):
    ACTIVE_SANDBOXES = "active_sandboxes"
    API_REQUESTS = "api_requests"
    NETWORK_EGRESS_BYTES = "network_egress_bytes"
    NETWORK_INGRESS_BYTES = "network_ingress_bytes"
    SANDBOX_CLAIMS = "sandbox_claims"
    SNAPSHOT_STORAGE_GB = "snapshot_storage_gb"
    VOLUME_STORAGE_GB = "volume_storage_gb"

    def __str__(self) -> str:
        return str(self.value)
