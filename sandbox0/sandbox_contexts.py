from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sandbox0.apispec.api.contexts import delete_api_v1_sandboxes_id_contexts_ctx_id
from sandbox0.apispec.api.contexts import get_api_v1_sandboxes_id_contexts
from sandbox0.apispec.api.contexts import get_api_v1_sandboxes_id_contexts_ctx_id
from sandbox0.apispec.api.contexts import get_api_v1_sandboxes_id_contexts_ctx_id_stats
from sandbox0.apispec.api.contexts import post_api_v1_sandboxes_id_contexts
from sandbox0.apispec.api.contexts import post_api_v1_sandboxes_id_contexts_ctx_id_exec
from sandbox0.apispec.api.contexts import post_api_v1_sandboxes_id_contexts_ctx_id_input
from sandbox0.apispec.api.contexts import post_api_v1_sandboxes_id_contexts_ctx_id_resize
from sandbox0.apispec.api.contexts import post_api_v1_sandboxes_id_contexts_ctx_id_restart
from sandbox0.apispec.api.contexts import post_api_v1_sandboxes_id_contexts_ctx_id_signal
from sandbox0.apispec.models.context_exec_response import ContextExecResponse
from sandbox0.apispec.models.context_input_request import ContextInputRequest
from sandbox0.apispec.models.context_response import ContextResponse
from sandbox0.apispec.models.context_stats_response import ContextStatsResponse
from sandbox0.apispec.models.create_context_request import CreateContextRequest
from sandbox0.apispec.models.resize_context_request import ResizeContextRequest
from sandbox0.apispec.models.signal_context_request import SignalContextRequest
from sandbox0.apispec.models.success_context_exec_response import SuccessContextExecResponse
from sandbox0.apispec.models.success_context_list_response import SuccessContextListResponse
from sandbox0.apispec.models.success_context_response import SuccessContextResponse
from sandbox0.apispec.models.success_context_stats_response import SuccessContextStatsResponse
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_resized_response import SuccessResizedResponse
from sandbox0.apispec.models.success_signaled_response import SuccessSignaledResponse
from sandbox0.apispec.models.success_written_response import SuccessWrittenResponse
from sandbox0.response import ensure_data, ensure_model

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


class SandboxContextsMixin:
    id: str
    _client: Any

    def list_contexts(self: "Sandbox") -> list[ContextResponse]:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_contexts.sync_detailed(id=self.id, client=self._client.api)
        data = ensure_data(resp, SuccessContextListResponse)
        contexts = data.contexts
        if contexts.__class__.__name__ == "Unset":
            return []
        return contexts

    # Backward-compatible alias.
    def list_context(self: "Sandbox") -> list[ContextResponse]:  # type: ignore[misc]
        return self.list_contexts()

    def create_context(self: "Sandbox", request: CreateContextRequest) -> ContextResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_contexts.sync_detailed(id=self.id, client=self._client.api, body=request)
        return ensure_data(resp, SuccessContextResponse)

    def get_context(self: "Sandbox", context_id: str) -> ContextResponse:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_contexts_ctx_id.sync_detailed(
            id=self.id,
            ctx_id=context_id,
            client=self._client.api,
        )
        return ensure_data(resp, SuccessContextResponse)

    def delete_context(self: "Sandbox", context_id: str) -> SuccessDeletedResponse:  # type: ignore[misc]
        resp = delete_api_v1_sandboxes_id_contexts_ctx_id.sync_detailed(
            id=self.id,
            ctx_id=context_id,
            client=self._client.api,
        )
        return ensure_model(resp, SuccessDeletedResponse)

    def restart_context(self: "Sandbox", context_id: str) -> ContextResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_contexts_ctx_id_restart.sync_detailed(
            id=self.id,
            ctx_id=context_id,
            client=self._client.api,
        )
        return ensure_data(resp, SuccessContextResponse)

    def context_input(self: "Sandbox", context_id: str, input: str) -> SuccessWrittenResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_contexts_ctx_id_input.sync_detailed(
            id=self.id,
            ctx_id=context_id,
            client=self._client.api,
            body=ContextInputRequest(data=input),
        )
        return ensure_model(resp, SuccessWrittenResponse)

    def context_exec(self: "Sandbox", context_id: str, input: str) -> ContextExecResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_contexts_ctx_id_exec.sync_detailed(
            id=self.id,
            ctx_id=context_id,
            client=self._client.api,
            body=ContextInputRequest(data=input),
        )
        return ensure_data(resp, SuccessContextExecResponse)

    def context_resize(self: "Sandbox", context_id: str, rows: int, cols: int) -> SuccessResizedResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_contexts_ctx_id_resize.sync_detailed(
            id=self.id,
            ctx_id=context_id,
            client=self._client.api,
            body=ResizeContextRequest(rows=rows, cols=cols),
        )
        return ensure_model(resp, SuccessResizedResponse)

    def context_signal(self: "Sandbox", context_id: str, signal: str) -> SuccessSignaledResponse:  # type: ignore[misc]
        resp = post_api_v1_sandboxes_id_contexts_ctx_id_signal.sync_detailed(
            id=self.id,
            ctx_id=context_id,
            client=self._client.api,
            body=SignalContextRequest(signal=signal),
        )
        return ensure_model(resp, SuccessSignaledResponse)

    def context_stats(self: "Sandbox", context_id: str) -> ContextStatsResponse:  # type: ignore[misc]
        resp = get_api_v1_sandboxes_id_contexts_ctx_id_stats.sync_detailed(
            id=self.id,
            ctx_id=context_id,
            client=self._client.api,
        )
        return ensure_data(resp, SuccessContextStatsResponse)
