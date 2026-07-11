from __future__ import annotations

import json
import threading
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Iterator, Optional, Union
from urllib.parse import quote

import httpx

from sandbox0.apispec.api.sessions import delete_api_v1_sandboxes_id_sessions_session_id
from sandbox0.apispec.api.sessions import get_api_v1_sandboxes_id_sessions
from sandbox0.apispec.api.sessions import get_api_v1_sandboxes_id_sessions_session_id
from sandbox0.apispec.api.sessions import (
    get_api_v1_sandboxes_id_sessions_session_id_events,
)
from sandbox0.apispec.api.sessions import post_api_v1_sandboxes_id_sessions
from sandbox0.apispec.api.sessions import (
    post_api_v1_sandboxes_id_sessions_session_id_attempts,
)
from sandbox0.apispec.api.sessions import (
    post_api_v1_sandboxes_id_sessions_session_id_inputs,
)
from sandbox0.apispec.api.sessions import (
    post_api_v1_sandboxes_id_sessions_session_id_signals,
)
from sandbox0.apispec.api.sessions import put_api_v1_sandboxes_id_sessions_session_id
from sandbox0.apispec.api.sessions import (
    put_api_v1_sandboxes_id_sessions_session_id_desired_state,
)
from sandbox0.apispec.api.sessions import (
    put_api_v1_sandboxes_id_sessions_session_id_terminal,
)
from sandbox0.apispec.models.create_execution_session_attempt_request import (
    CreateExecutionSessionAttemptRequest,
)
from sandbox0.apispec.models.execution_session import ExecutionSession
from sandbox0.apispec.models.execution_session_desired_state import (
    ExecutionSessionDesiredState,
)
from sandbox0.apispec.models.execution_session_desired_state_request import (
    ExecutionSessionDesiredStateRequest,
)
from sandbox0.apispec.models.execution_session_event import ExecutionSessionEvent
from sandbox0.apispec.models.execution_session_event_page import (
    ExecutionSessionEventPage,
)
from sandbox0.apispec.models.execution_session_input_request import (
    ExecutionSessionInputRequest,
)
from sandbox0.apispec.models.execution_session_input_response import (
    ExecutionSessionInputResponse,
)
from sandbox0.apispec.models.execution_session_signal_request import (
    ExecutionSessionSignalRequest,
)
from sandbox0.apispec.models.execution_session_spec import ExecutionSessionSpec
from sandbox0.apispec.models.execution_session_terminal_resize_request import (
    ExecutionSessionTerminalResizeRequest,
)
from sandbox0.apispec.models.execution_session_web_socket_input import (
    ExecutionSessionWebSocketInput,
)
from sandbox0.apispec.models.execution_session_web_socket_resize import (
    ExecutionSessionWebSocketResize,
)
from sandbox0.apispec.models.execution_session_web_socket_signal import (
    ExecutionSessionWebSocketSignal,
)
from sandbox0.apispec.models.success_accepted_response import SuccessAcceptedResponse
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_execution_session_event_page_response import (
    SuccessExecutionSessionEventPageResponse,
)
from sandbox0.apispec.models.success_execution_session_input_response import (
    SuccessExecutionSessionInputResponse,
)
from sandbox0.apispec.models.success_execution_session_list_response import (
    SuccessExecutionSessionListResponse,
)
from sandbox0.apispec.models.success_execution_session_response import (
    SuccessExecutionSessionResponse,
)
from sandbox0.apispec.models.success_resized_response import SuccessResizedResponse
from sandbox0.apispec.types import UNSET
from sandbox0.errors import APIError
from sandbox0.response import ensure_data, ensure_model
from sandbox0.response_normalize import SKIP_RESPONSE_NORMALIZE_EXTENSION

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox
    from websockets.sync.client import ClientConnection


@dataclass(frozen=True)
class SessionCreateOptions:
    """Options for creating a durable execution session."""

    idempotency_key: Optional[str] = None


@dataclass(frozen=True)
class SessionEventOptions:
    """Options for reading a page from a session event journal."""

    after: Optional[int] = None
    limit: Optional[int] = None


@dataclass(frozen=True)
class SessionEventStreamOptions:
    """Options for attaching to a resumable SSE event stream."""

    after: Optional[int] = None
    last_event_id: Optional[str] = None


@dataclass(frozen=True)
class SessionWebSocketOptions:
    """Options for attaching to a session WebSocket."""

    after: Optional[int] = None


@dataclass(frozen=True)
class SessionWebSocketMessage:
    type: str
    request_id: Optional[str] = None
    event: Optional[ExecutionSessionEvent] = None
    error: Optional[str] = None


SessionWebSocketRequest = Union[
    ExecutionSessionWebSocketInput,
    ExecutionSessionWebSocketSignal,
    ExecutionSessionWebSocketResize,
]


class SessionEventStream:
    """A resumable SSE attachment. Closing it does not stop the session."""

    def __init__(self, response: httpx.Response) -> None:
        self._response = response

    @property
    def response(self) -> httpx.Response:
        return self._response

    def iter_events(self) -> Iterator[ExecutionSessionEvent]:
        data_lines: list[str] = []
        for raw_line in self._response.iter_lines():
            line = raw_line.rstrip("\r")
            if line == "":
                if data_lines:
                    yield ExecutionSessionEvent.from_dict(
                        json.loads("\n".join(data_lines))
                    )
                    data_lines.clear()
                continue
            if line.startswith("data:"):
                value = line[5:]
                data_lines.append(value[1:] if value.startswith(" ") else value)
        if data_lines:
            yield ExecutionSessionEvent.from_dict(json.loads("\n".join(data_lines)))

    def close(self) -> None:
        self._response.close()

    def __enter__(self) -> "SessionEventStream":
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()


class ExecutionSessionConnection:
    """A duplex attachment whose closure does not affect session lifecycle or stdin."""

    def __init__(self, conn: "ClientConnection") -> None:
        self._conn = conn
        self._send_lock = threading.Lock()

    def send(self, request: SessionWebSocketRequest) -> None:
        with self._send_lock:
            self._conn.send(json.dumps(request.to_dict()))

    def iter_messages(self) -> Iterator[SessionWebSocketMessage]:
        from websockets.exceptions import ConnectionClosedOK

        while True:
            try:
                raw = self._conn.recv()
            except ConnectionClosedOK:
                return
            if raw is None:
                return
            if isinstance(raw, bytes):
                raw = raw.decode("utf-8", errors="replace")
            payload = json.loads(raw)
            message_type = str(payload.get("type", ""))
            event = None
            if message_type == "event" and isinstance(payload.get("event"), dict):
                event = ExecutionSessionEvent.from_dict(payload["event"])
            if message_type not in ("ack", "error", "event"):
                continue
            yield SessionWebSocketMessage(
                type=message_type,
                request_id=_optional_string(payload.get("request_id")),
                event=event,
                error=_optional_string(payload.get("error")),
            )

    def close(self) -> None:
        """Detach this client without stopping the session or closing stdin."""
        self._conn.close()

    def __enter__(self) -> "ExecutionSessionConnection":
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()


class SandboxSessionsMixin:
    id: str
    _client: Any

    def list_sessions(self: "Sandbox") -> list[ExecutionSession]:  # type: ignore[misc]
        response = get_api_v1_sandboxes_id_sessions.sync_detailed(
            id=self.id, client=self._client.api
        )
        return ensure_data(response, SuccessExecutionSessionListResponse).sessions

    def create_session(  # type: ignore[misc]
        self: "Sandbox",
        spec: ExecutionSessionSpec,
        options: Optional[SessionCreateOptions] = None,
    ) -> ExecutionSession:
        opts = options or SessionCreateOptions()
        response = post_api_v1_sandboxes_id_sessions.sync_detailed(
            id=self.id,
            client=self._client.api,
            body=spec,
            idempotency_key=_value(opts.idempotency_key),
        )
        return ensure_data(response, SuccessExecutionSessionResponse)

    def get_session(self: "Sandbox", session_id: str) -> ExecutionSession:  # type: ignore[misc]
        response = get_api_v1_sandboxes_id_sessions_session_id.sync_detailed(
            id=self.id, session_id=session_id, client=self._client.api
        )
        return ensure_data(response, SuccessExecutionSessionResponse)

    def update_session(  # type: ignore[misc]
        self: "Sandbox", session_id: str, spec: ExecutionSessionSpec
    ) -> ExecutionSession:
        response = put_api_v1_sandboxes_id_sessions_session_id.sync_detailed(
            id=self.id, session_id=session_id, client=self._client.api, body=spec
        )
        return ensure_data(response, SuccessExecutionSessionResponse)

    def delete_session(self: "Sandbox", session_id: str) -> SuccessDeletedResponse:  # type: ignore[misc]
        response = delete_api_v1_sandboxes_id_sessions_session_id.sync_detailed(
            id=self.id, session_id=session_id, client=self._client.api
        )
        return ensure_model(response, SuccessDeletedResponse)

    def set_session_desired_state(  # type: ignore[misc]
        self: "Sandbox", session_id: str, state: ExecutionSessionDesiredState
    ) -> ExecutionSession:
        response = (
            put_api_v1_sandboxes_id_sessions_session_id_desired_state.sync_detailed(
                id=self.id,
                session_id=session_id,
                client=self._client.api,
                body=ExecutionSessionDesiredStateRequest(state=state),
            )
        )
        return ensure_data(response, SuccessExecutionSessionResponse)

    def create_session_attempt(  # type: ignore[misc]
        self: "Sandbox", session_id: str, replace_current: bool = False
    ) -> ExecutionSession:
        response = post_api_v1_sandboxes_id_sessions_session_id_attempts.sync_detailed(
            id=self.id,
            session_id=session_id,
            client=self._client.api,
            body=CreateExecutionSessionAttemptRequest(replace_current=replace_current),
        )
        return ensure_data(response, SuccessExecutionSessionResponse)

    def write_session_input(  # type: ignore[misc]
        self: "Sandbox", session_id: str, request: ExecutionSessionInputRequest
    ) -> ExecutionSessionInputResponse:
        response = post_api_v1_sandboxes_id_sessions_session_id_inputs.sync_detailed(
            id=self.id, session_id=session_id, client=self._client.api, body=request
        )
        return ensure_data(response, SuccessExecutionSessionInputResponse)

    def send_session_signal(  # type: ignore[misc]
        self: "Sandbox", session_id: str, request: ExecutionSessionSignalRequest
    ) -> SuccessAcceptedResponse:
        response = post_api_v1_sandboxes_id_sessions_session_id_signals.sync_detailed(
            id=self.id, session_id=session_id, client=self._client.api, body=request
        )
        return ensure_model(response, SuccessAcceptedResponse)

    def resize_session_terminal(  # type: ignore[misc]
        self: "Sandbox", session_id: str, request: ExecutionSessionTerminalResizeRequest
    ) -> SuccessResizedResponse:
        response = put_api_v1_sandboxes_id_sessions_session_id_terminal.sync_detailed(
            id=self.id, session_id=session_id, client=self._client.api, body=request
        )
        return ensure_model(response, SuccessResizedResponse)

    def list_session_events(  # type: ignore[misc]
        self: "Sandbox",
        session_id: str,
        options: Optional[SessionEventOptions] = None,
    ) -> ExecutionSessionEventPage:
        opts = options or SessionEventOptions()
        response = get_api_v1_sandboxes_id_sessions_session_id_events.sync_detailed(
            id=self.id,
            session_id=session_id,
            client=self._client.api,
            after=_value(opts.after),
            limit=_value(opts.limit),
        )
        return ensure_data(response, SuccessExecutionSessionEventPageResponse)

    def watch_session_events(  # type: ignore[misc]
        self: "Sandbox",
        session_id: str,
        options: Optional[SessionEventStreamOptions] = None,
    ) -> SessionEventStream:
        opts = options or SessionEventStreamOptions()
        http_client = self._client.api.get_httpx_client()
        request = http_client.build_request(
            "GET",
            f"/api/v1/sandboxes/{quote(self.id, safe='')}/sessions/{quote(session_id, safe='')}/events/stream",
            params={"after": str(opts.after)} if opts.after is not None else None,
            headers={
                "Accept": "text/event-stream",
                **({"Last-Event-ID": opts.last_event_id} if opts.last_event_id else {}),
            },
        )
        request.extensions[SKIP_RESPONSE_NORMALIZE_EXTENSION] = True
        response = http_client.send(request, stream=True)
        if response.status_code < 200 or response.status_code >= 300:
            content = response.read()
            response.close()
            raise _api_error_from_response(response, content)
        content_type = response.headers.get("Content-Type", "")
        if content_type and not content_type.lower().startswith("text/event-stream"):
            response.close()
            raise APIError(
                status_code=response.status_code,
                code="unexpected_response",
                message=f"unexpected session event stream content type: {content_type}",
            )
        return SessionEventStream(response)

    def connect_session(  # type: ignore[misc]
        self: "Sandbox",
        session_id: str,
        options: Optional[SessionWebSocketOptions] = None,
    ) -> ExecutionSessionConnection:
        from websockets.sync.client import connect

        opts = options or SessionWebSocketOptions()
        path = f"/api/v1/sandboxes/{quote(self.id, safe='')}/sessions/{quote(session_id, safe='')}/ws"
        ws_url = self._client.websocket_url(path)
        if opts.after is not None:
            ws_url += f"?after={opts.after}"
        conn = connect(ws_url, additional_headers=self._client.ws_headers())
        return ExecutionSessionConnection(conn)


def _value(value: Any) -> Any:
    return UNSET if value is None else value


def _optional_string(value: Any) -> Optional[str]:
    return None if value is None else str(value)


def _api_error_from_response(response: httpx.Response, content: bytes) -> APIError:
    try:
        payload = json.loads(content.decode("utf-8"))
        error = payload.get("error") or {}
        if error:
            return APIError(
                status_code=response.status_code,
                code=error.get("code"),
                message=error.get("message") or response.reason_phrase,
                details=error.get("details"),
                request_id=response.headers.get("X-Request-ID"),
                body=content,
            )
    except Exception:
        pass
    return APIError(
        status_code=response.status_code,
        code="unexpected_response",
        message=content.decode("utf-8", errors="replace").strip()
        or response.reason_phrase,
        request_id=response.headers.get("X-Request-ID"),
        body=content,
    )
