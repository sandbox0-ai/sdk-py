from __future__ import annotations

import base64
import binascii
import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Optional
from urllib.parse import quote

from sandbox0.apispec.api.sandboxes import (
    delete_sandbox_managed_file,
    delete_sandbox_namespaced_managed_file,
    inspect_sandbox_managed_files,
    read_sandbox_managed_file,
    read_sandbox_namespaced_managed_file,
    write_sandbox_managed_file,
    write_sandbox_namespaced_managed_file,
)
from sandbox0.apispec.models.managed_files_state import ManagedFilesState
from sandbox0.apispec.models.managed_file_write_request import ManagedFileWriteRequest
from sandbox0.apispec.models.success_managed_files_state_response import SuccessManagedFilesStateResponse
from sandbox0.apispec.models.success_managed_file_read_response import SuccessManagedFileReadResponse
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.client import Client
    from sandbox0.sandbox import Sandbox


def _validate_name(value: str) -> None:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9._-]{1,128}", value) or value in (".", "..") or value.startswith(".s0-write-"):
        raise ValueError("invalid managed file name or namespace")


def _validate_sequence(value: str) -> None:
    if not isinstance(value, str) or not re.fullmatch(r"0|[1-9][0-9]{0,19}", value) or int(value) > (1 << 64) - 1:
        raise ValueError("invalid managed file mutation sequence")


@dataclass(frozen=True)
class ManagedFileRead:
    state: ManagedFilesState
    content: bytes = field(repr=False)


@dataclass(frozen=True)
class ManagedFiles:
    """Fixed-generation file access independent of guest execution.

    No automatic resume, fallback, generation discovery or mutation retry.
    Namespaces share a sequence, which native guest writes do not advance.
    Reconcile ambiguous writes with inspect/read before a new mutation.
    """

    _client: Client = field(repr=False)
    _sandbox_id: str
    runtime_generation: int
    namespace: Optional[str] = None

    def __post_init__(self) -> None:
        if type(self.runtime_generation) is not int or not 0 < self.runtime_generation < (1 << 63):
            raise ValueError("invalid managed file runtime generation")
        if self.namespace is not None:
            _validate_name(self.namespace)
        if self._sandbox_id in (".", ".."):
            raise ValueError("invalid managed file sandbox identity")

    def _params(self) -> dict[str, Any]:
        return {"id": quote(self._sandbox_id, safe=""), "runtime_generation": self.runtime_generation, "client": self._client.api}

    def _validate_state(self, state: Any) -> None:
        if state.runtime_generation != self.runtime_generation:
            raise ValueError("managed file response generation changed")
        _validate_sequence(state.mutation_sequence)

    def inspect(self) -> ManagedFilesState:
        """Describe the projection, not historical RootFS credential safety."""
        response = inspect_sandbox_managed_files.sync_detailed(**self._params())
        state: ManagedFilesState = ensure_data(response, SuccessManagedFilesStateResponse)
        self._validate_state(state)
        return state

    def read(self, name: str) -> ManagedFileRead:
        _validate_name(name)
        params = self._params()
        if self.namespace is None:
            response = read_sandbox_managed_file.sync_detailed(name=name, **params)
        else:
            response = read_sandbox_namespaced_managed_file.sync_detailed(namespace=self.namespace, name=name, **params)
        data = ensure_data(response, SuccessManagedFileReadResponse)
        self._validate_state(data)
        try:
            if not isinstance(data.content, str) or len(data.content) > 4 * ((4 * 1024 * 1024 + 2) // 3):
                raise ValueError()
            content = base64.b64decode(data.content, validate=True)
            if len(content) > 4 * 1024 * 1024 or base64.b64encode(content).decode("ascii") != data.content:
                raise ValueError()
        except (ValueError, binascii.Error):
            raise ValueError("invalid managed file response content") from None
        state = ManagedFilesState(runtime_generation=data.runtime_generation, mutation_sequence=data.mutation_sequence, size_bytes=data.size_bytes, guest_path=data.guest_path)
        return ManagedFileRead(state=state, content=content)

    def write(self, name: str, content: bytes, *, expected_mutation_sequence: str) -> ManagedFilesState:
        _validate_name(name)
        _validate_sequence(expected_mutation_sequence)
        if not isinstance(content, bytes) or len(content) > 4 * 1024 * 1024:
            raise ValueError("invalid managed file content size or type")
        body = ManagedFileWriteRequest(content=base64.b64encode(content).decode("ascii"), expected_mutation_sequence=expected_mutation_sequence)
        params = self._params()
        if self.namespace is None:
            response = write_sandbox_managed_file.sync_detailed(name=name, body=body, **params)
        else:
            response = write_sandbox_namespaced_managed_file.sync_detailed(namespace=self.namespace, name=name, body=body, **params)
        state: ManagedFilesState = ensure_data(response, SuccessManagedFilesStateResponse)
        self._validate_state(state)
        return state

    def delete(self, name: str, *, expected_mutation_sequence: str) -> ManagedFilesState:
        _validate_name(name)
        _validate_sequence(expected_mutation_sequence)
        params = self._params()
        if self.namespace is None:
            response = delete_sandbox_managed_file.sync_detailed(name=name, expected_mutation_sequence=expected_mutation_sequence, **params)
        else:
            response = delete_sandbox_namespaced_managed_file.sync_detailed(namespace=self.namespace, name=name, expected_mutation_sequence=expected_mutation_sequence, **params)
        state: ManagedFilesState = ensure_data(response, SuccessManagedFilesStateResponse)
        self._validate_state(state)
        return state


class SandboxManagedFilesMixin:
    id: str
    _client: Any

    def managed_files(self: "Sandbox", *, runtime_generation: int, namespace: Optional[str] = None) -> ManagedFiles:  # type: ignore[misc]
        return ManagedFiles(self._client, self.id, runtime_generation, namespace)
