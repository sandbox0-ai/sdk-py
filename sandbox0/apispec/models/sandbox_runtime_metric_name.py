from enum import Enum


class SandboxRuntimeMetricName(str, Enum):
    SANDBOX_CPU_LIMIT = "sandbox.cpu.limit"
    SANDBOX_CPU_TIME = "sandbox.cpu.time"
    SANDBOX_CPU_USAGE = "sandbox.cpu.usage"
    SANDBOX_CPU_UTILIZATION = "sandbox.cpu.utilization"
    SANDBOX_MEMORY_AVAILABLE = "sandbox.memory.available"
    SANDBOX_MEMORY_LIMIT = "sandbox.memory.limit"
    SANDBOX_MEMORY_USAGE = "sandbox.memory.usage"
    SANDBOX_MEMORY_UTILIZATION = "sandbox.memory.utilization"
    SANDBOX_MEMORY_WORKING_SET = "sandbox.memory.working_set"
    SANDBOX_NETWORK_ERRORS = "sandbox.network.errors"
    SANDBOX_NETWORK_IO = "sandbox.network.io"
    SANDBOX_PROCESS_COUNT = "sandbox.process.count"
    SANDBOX_ROOTFS_WRITABLE_INODES = "sandbox.rootfs.writable.inodes"
    SANDBOX_ROOTFS_WRITABLE_USAGE = "sandbox.rootfs.writable.usage"

    def __str__(self) -> str:
        return str(self.value)
