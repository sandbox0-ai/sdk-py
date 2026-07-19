from enum import Enum


class TeamQuotaKey(str, Enum):
    ACTIVE_CONNECTION_COUNT = "active_connection_count"
    ACTIVE_REQUEST_COUNT = "active_request_count"
    API_REQUESTS = "api_requests"
    CONTROL_PLANE_OBJECT_COUNT = "control_plane_object_count"
    NETWORK_EGRESS_BYTES = "network_egress_bytes"
    NETWORK_INGRESS_BYTES = "network_ingress_bytes"
    NETWORK_OPERATIONS = "network_operations"
    OBSERVABILITY_INGEST_BYTES = "observability_ingest_bytes"
    ROOTFS_STORAGE_BYTES = "rootfs_storage_bytes"
    SANDBOX_CPU_MILLICORES = "sandbox_cpu_millicores"
    SANDBOX_EPHEMERAL_STORAGE_BYTES = "sandbox_ephemeral_storage_bytes"
    SANDBOX_IDENTITY_COUNT = "sandbox_identity_count"
    SANDBOX_MEMORY_BYTES = "sandbox_memory_bytes"
    SANDBOX_RUNTIME_COUNT = "sandbox_runtime_count"
    SANDBOX_SERVICE_REQUESTS = "sandbox_service_requests"
    SANDBOX_STARTS = "sandbox_starts"
    SNAPSHOT_STORAGE_BYTES = "snapshot_storage_bytes"
    STORAGE_OBJECT_COUNT = "storage_object_count"
    STORAGE_OPERATIONS = "storage_operations"
    TEMPLATE_IMAGE_STORAGE_BYTES = "template_image_storage_bytes"
    VOLUME_STORAGE_BYTES = "volume_storage_bytes"

    def __str__(self) -> str:
        return str(self.value)
