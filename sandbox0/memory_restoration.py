from __future__ import annotations

import re
from datetime import datetime

from sandbox0.apispec.api.sandboxes import get_sandbox_memory_restoration
from sandbox0.apispec.client import AuthenticatedClient
from sandbox0.apispec.models.sandbox_memory_restoration import SandboxMemoryRestoration
from sandbox0.apispec.models.success_sandbox_memory_restoration_response import SuccessSandboxMemoryRestorationResponse
from sandbox0.response import ensure_data


def _integer(value: object, minimum: int, maximum: int = 2**63 - 1) -> bool:
    return type(value) is int and minimum <= value <= maximum


class ClientMemoryRestorationMixin:
    _api: AuthenticatedClient

    def get_sandbox_memory_restoration(self, sandbox_id: str, runtime_generation: int) -> SandboxMemoryRestoration:
        """Read external memory lineage; bind to owned publication/session history before adoption."""
        if not isinstance(sandbox_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]+", sandbox_id) or not _integer(runtime_generation, 1):
            raise ValueError("invalid memory restoration target")
        response = get_sandbox_memory_restoration.sync_detailed(sandbox_id, client=self._api, runtime_generation=runtime_generation)
        value = ensure_data(response, SuccessSandboxMemoryRestorationResponse)
        if (value.sandbox_id != sandbox_id or not _integer(value.runtime_generation, 1) or value.runtime_generation != runtime_generation or
            not isinstance(value.filesystem_id, str) or not value.filesystem_id or
            not isinstance(value.runtime_compatibility_digest, str) or not re.fullmatch(r"sha256:[a-f0-9]{64}", value.runtime_compatibility_digest) or
            not isinstance(value.observed_at, datetime) or value.observed_at.tzinfo is None or value.observed_at.utcoffset() is None or
            not isinstance(value.steps, list) or not 1 <= len(value.steps) <= 64):
            raise ValueError("invalid external memory restoration")
        previous = None
        for step in value.steps:
            if (any(not isinstance(v, str) or not 1 <= len(v) <= 512 for v in (step.operation_id, step.capture_operation_id)) or
                not isinstance(step.restore_id, str) or not re.fullmatch(r"[a-f0-9]{64}", step.restore_id) or
                not _integer(step.from_runtime_generation, 1) or not _integer(step.to_runtime_generation, 1) or step.to_runtime_generation <= step.from_runtime_generation or
                not _integer(step.managed_files_size_bytes, 0, 67108864) or
                (previous is not None and previous != step.from_runtime_generation)):
                raise ValueError("invalid external memory restoration")
            previous = step.to_runtime_generation
        if previous != runtime_generation:
            raise ValueError("invalid external memory restoration")
        return value
