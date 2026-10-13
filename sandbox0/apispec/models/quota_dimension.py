from enum import Enum


class QuotaDimension(str, Enum):
    ACTIVE_SANDBOXES = "active_sandboxes"
    API_REQUESTS = "api_requests"
    NETWORK_EGRESS_BYTES = "network_egress_bytes"
    NETWORK_INGRESS_BYTES = "network_ingress_bytes"
    PAUSED_SANDBOXES = "paused_sandboxes"
    SANDBOX_CLAIMS = "sandbox_claims"
    SNAPSHOTS_PER_SANDBOX = "snapshots_per_sandbox"

    def __str__(self) -> str:
        return str(self.value)
