"""Validation for conditional first launches; no retries or fallback mutations."""
from __future__ import annotations

import json
import re
from datetime import datetime
from typing import Optional

from sandbox0.apispec.models.sandbox_root_fs_fork_launch import SandboxRootFSForkLaunch
from sandbox0.apispec.types import UNSET


def _coordinate(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9._:-]{1,512}", value) is not None


def validate_input(sandbox_id: str, fork_operation_id: str, filesystem_id: str, head_generation_id: str,
                   writer_epoch: int, idempotency_key: str, expected_operation_id: Optional[str]) -> None:
    if (not isinstance(sandbox_id, str) or not sandbox_id or len(sandbox_id) > 512 or sandbox_id.strip() != sandbox_id
            or not all(_coordinate(v) for v in [fork_operation_id, filesystem_id, head_generation_id])
            or type(writer_epoch) is not int or not 1 <= writer_epoch <= 9007199254740991
            or not isinstance(idempotency_key, str) or re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", idempotency_key) is None
            or (expected_operation_id is not None and not _coordinate(expected_operation_id))):
        raise ValueError("invalid original fork launch conditions")


def validate_receipt(r: SandboxRootFSForkLaunch, content: bytes, sandbox_id: str, fork_operation_id: str,
                     filesystem_id: str, head_generation_id: str, writer_epoch: int,
                     expected_operation_id: Optional[str]) -> SandboxRootFSForkLaunch:
    # IntEnum decoding accepts booleans and integral floats. Inspect the wire to
    # reject those instead of letting them become trusted generation evidence.
    wire = json.loads(content).get("data")
    if (not isinstance(wire, dict)
            or any(type(wire.get(k)) is not int for k in ("writer_epoch", "lifecycle_epoch", "runtime_generation"))
            or wire.get("launch_digest", UNSET) is None or wire.get("completed_at", UNSET) is None):
        raise ValueError("invalid fork launch wire evidence")
    if (r.sandbox_id != sandbox_id or r.fork_operation_id != fork_operation_id or r.filesystem_id != filesystem_id
            or r.head_generation_id != head_generation_id or r.writer_epoch != writer_epoch or r.lifecycle_epoch != 1
            or not _coordinate(r.operation_id) or (expected_operation_id is not None and r.operation_id != expected_operation_id)
            or type(r.current) is not bool):
        raise ValueError("fork launch receipt does not match original conditions")
    valid = False
    if r.state in ("pending", "aborted"):
        valid = r.runtime_generation == 0 and r.launch_digest is UNSET and r.completed_at is UNSET and (r.state != "aborted" or not r.current)
    elif r.state == "completed":
        valid = (r.runtime_generation == 1 and isinstance(r.launch_digest, str)
                 and re.fullmatch(r"[a-f0-9]{64}", r.launch_digest) is not None
                 and isinstance(r.completed_at, datetime) and r.completed_at.utcoffset() is not None
                 and isinstance(wire.get("completed_at"), str)
                 and re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", wire["completed_at"], re.IGNORECASE) is not None)
    if not valid:
        raise ValueError("fork launch receipt has invalid completion evidence")
    return r
