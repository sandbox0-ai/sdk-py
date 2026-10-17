from __future__ import annotations

import base64
import binascii
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from urllib.parse import quote

from sandbox0.apispec.api.sandboxes import get_sandbox_snapshot_restore_final_capture, read_sandbox_snapshot_restore_final_capture_file, acknowledge_sandbox_snapshot_restore_final_capture
from sandbox0.apispec.api.sandboxes import (
    get_sandbox_restart_final_capture,
    read_sandbox_restart_final_capture_file,
    acknowledge_sandbox_restart_final_capture,
)
from sandbox0.apispec.models.sandbox_restart_final_capture import SandboxRestartFinalCapture
from sandbox0.apispec.models.sandbox_restart_final_capture_acknowledgement import SandboxRestartFinalCaptureAcknowledgement
from sandbox0.apispec.models.success_sandbox_restart_final_capture_response import SuccessSandboxRestartFinalCaptureResponse
from sandbox0.apispec.models.success_sandbox_restart_final_capture_file_response import SuccessSandboxRestartFinalCaptureFileResponse
from sandbox0.apispec.types import UNSET
from sandbox0.response import ensure_data
from sandbox0.sandbox_managed_files import _validate_name, _validate_sequence


def _capture_id(value: object) -> None:
    if not isinstance(value, str) or not re.fullmatch(r"[a-f0-9]{64}", value):
        raise ValueError("invalid final capture identity")


def _receipt_id(value: object) -> None:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9._:-]{1,255}", value):
        raise ValueError("invalid final capture receipt")


def _target(sandbox_id: str, operation_id: str) -> None:
    if (not isinstance(sandbox_id, str) or not sandbox_id or sandbox_id.strip() != sandbox_id or sandbox_id in (".", "..") or
        not isinstance(operation_id, str) or not re.fullmatch(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", operation_id)):
        raise ValueError("invalid restart final capture identity")


def _status(value: SandboxRestartFinalCapture, sandbox_id: str, operation_id: str) -> SandboxRestartFinalCapture:
    if (value.sandbox_id != sandbox_id or value.operation_id != operation_id or
        type(value.from_runtime_generation) is not int or not 0 < value.from_runtime_generation < 2**63):
        raise ValueError("invalid final capture status")
    if value.state == "pending":
        if value.capture_id is not UNSET or value.stopped_at is not UNSET or value.receipt_id is not UNSET:
            raise ValueError("pending final capture has a receipt")
    elif value.state in ("stopped", "acknowledged", "released"):
        _capture_id(value.capture_id)
        if not isinstance(value.stopped_at, datetime) or value.stopped_at.tzinfo is None or value.stopped_at.utcoffset() is None:
            raise ValueError("invalid stopped capture identity")
        if value.state == "stopped":
            if value.receipt_id is not UNSET:
                raise ValueError("unacknowledged capture has a receipt")
        else:
            _receipt_id(value.receipt_id)
    else:
        raise ValueError("invalid final capture state")
    return value


@dataclass(frozen=True)
class RestartFinalCaptureFile:
    operation_id: str
    capture_id: str
    runtime_generation: int
    mutation_sequence: str
    size_bytes: int
    found: bool
    content: bytes = field(repr=False)


class ClientRestartFinalCaptureMixin:
    _api: Any

    def get_sandbox_restart_final_capture(self, sandbox_id: str, operation_id: str) -> SandboxRestartFinalCapture:
        """Read durable stopped-source custody metadata without guest execution."""
        _target(sandbox_id, operation_id)
        response = get_sandbox_restart_final_capture.sync_detailed(id=quote(sandbox_id, safe=""), operation_id=operation_id, client=self._api)
        return _status(ensure_data(response, SuccessSandboxRestartFinalCaptureResponse), sandbox_id, operation_id)

    def read_sandbox_restart_final_capture_file(self, sandbox_id: str, operation_id: str, capture_id: str, namespace: str, name: str) -> RestartFinalCaptureFile:
        """Read transient bytes. Only found=False confirms absence; errors never imply logout."""
        _target(sandbox_id, operation_id)
        _capture_id(capture_id)
        _validate_name(namespace)
        _validate_name(name)
        response = read_sandbox_restart_final_capture_file.sync_detailed(id=quote(sandbox_id, safe=""), operation_id=operation_id, capture_id=capture_id, namespace=namespace, name=name, client=self._api)
        value = ensure_data(response, SuccessSandboxRestartFinalCaptureFileResponse)
        if (value.operation_id != operation_id or value.capture_id != capture_id or
            type(value.runtime_generation) is not int or not 0 < value.runtime_generation < 2**63 or
            type(value.size_bytes) is not int or not 1048576 <= value.size_bytes <= 67108864 or type(value.found) is not bool):
            raise ValueError("invalid final capture file authority")
        _validate_sequence(value.mutation_sequence)
        try:
            if not isinstance(value.content, str) or len(value.content) > 4 * ((4194304 + 2) // 3):
                raise ValueError()
            content = base64.b64decode(value.content, validate=True)
            if len(content) > 4194304 or base64.b64encode(content).decode("ascii") != value.content or (not value.found and content):
                raise ValueError()
        except (ValueError, binascii.Error):
            raise ValueError("invalid final capture file content") from None
        return RestartFinalCaptureFile(value.operation_id, value.capture_id, value.runtime_generation, value.mutation_sequence, value.size_bytes, value.found, content)

    def acknowledge_sandbox_restart_final_capture(self, sandbox_id: str, operation_id: str, capture_id: str, receipt_id: str) -> SandboxRestartFinalCapture:
        """Release custody only after durable encrypted credentials/logout commit.

        Reconcile uncertain replies with identical IDs. Never retries automatically.
        """
        _target(sandbox_id, operation_id)
        _capture_id(capture_id)
        _receipt_id(receipt_id)
        body = SandboxRestartFinalCaptureAcknowledgement(capture_id=capture_id, receipt_id=receipt_id)
        response = acknowledge_sandbox_restart_final_capture.sync_detailed(id=quote(sandbox_id, safe=""), operation_id=operation_id, body=body, client=self._api)
        value = _status(ensure_data(response, SuccessSandboxRestartFinalCaptureResponse), sandbox_id, operation_id)
        if value.capture_id != capture_id or value.receipt_id != receipt_id or value.state not in ("acknowledged", "released"):
            raise ValueError("final capture acknowledgement changed receipt")
        return value

    def get_sandbox_snapshot_restore_final_capture(self, sandbox_id: str, operation_id: str) -> SandboxRestartFinalCapture:
        """Read durable stopped-source custody metadata without guest execution."""
        _target(sandbox_id, operation_id)
        response = get_sandbox_snapshot_restore_final_capture.sync_detailed(id=quote(sandbox_id, safe=""), operation_id=operation_id, client=self._api)
        return _status(ensure_data(response, SuccessSandboxRestartFinalCaptureResponse), sandbox_id, operation_id)

    def read_sandbox_snapshot_restore_final_capture_file(self, sandbox_id: str, operation_id: str, capture_id: str, namespace: str, name: str) -> RestartFinalCaptureFile:
        """Read transient bytes. Only found=False confirms absence; errors never imply logout."""
        _target(sandbox_id, operation_id)
        _capture_id(capture_id)
        _validate_name(namespace)
        _validate_name(name)
        response = read_sandbox_snapshot_restore_final_capture_file.sync_detailed(id=quote(sandbox_id, safe=""), operation_id=operation_id, capture_id=capture_id, namespace=namespace, name=name, client=self._api)
        value = ensure_data(response, SuccessSandboxRestartFinalCaptureFileResponse)
        if (value.operation_id != operation_id or value.capture_id != capture_id or
            type(value.runtime_generation) is not int or not 0 < value.runtime_generation < 2**63 or
            type(value.size_bytes) is not int or not 1048576 <= value.size_bytes <= 67108864 or type(value.found) is not bool):
            raise ValueError("invalid final capture file authority")
        _validate_sequence(value.mutation_sequence)
        try:
            if not isinstance(value.content, str) or len(value.content) > 4 * ((4194304 + 2) // 3):
                raise ValueError()
            content = base64.b64decode(value.content, validate=True)
            if len(content) > 4194304 or base64.b64encode(content).decode("ascii") != value.content or (not value.found and content):
                raise ValueError()
        except (ValueError, binascii.Error):
            raise ValueError("invalid final capture file content") from None
        return RestartFinalCaptureFile(value.operation_id, value.capture_id, value.runtime_generation, value.mutation_sequence, value.size_bytes, value.found, content)

    def acknowledge_sandbox_snapshot_restore_final_capture(self, sandbox_id: str, operation_id: str, capture_id: str, receipt_id: str) -> SandboxRestartFinalCapture:
        """Release custody only after durable encrypted credentials/logout commit.

        Reconcile uncertain replies with identical IDs. Never retries automatically.
        """
        _target(sandbox_id, operation_id)
        _capture_id(capture_id)
        _receipt_id(receipt_id)
        body = SandboxRestartFinalCaptureAcknowledgement(capture_id=capture_id, receipt_id=receipt_id)
        response = acknowledge_sandbox_snapshot_restore_final_capture.sync_detailed(id=quote(sandbox_id, safe=""), operation_id=operation_id, body=body, client=self._api)
        value = _status(ensure_data(response, SuccessSandboxRestartFinalCaptureResponse), sandbox_id, operation_id)
        if value.capture_id != capture_id or value.receipt_id != receipt_id or value.state not in ("acknowledged", "released"):
            raise ValueError("final capture acknowledgement changed receipt")
        return value
