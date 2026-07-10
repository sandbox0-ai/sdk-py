from datetime import datetime, timezone
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

import httpx

from sandbox0 import Client, SessionCreateOptions, SessionEventStreamOptions
from sandbox0.apispec.models.execution_session import ExecutionSession
from sandbox0.apispec.models.execution_session_event_cursor import (
    ExecutionSessionEventCursor,
)
from sandbox0.apispec.models.execution_session_phase import ExecutionSessionPhase
from sandbox0.apispec.models.execution_session_spec import ExecutionSessionSpec
from sandbox0.apispec.models.success_execution_session_response import (
    SuccessExecutionSessionResponse,
)
from sandbox0.apispec.types import Response


class TestSandboxSessions(TestCase):
    def test_websocket_url_preserves_base_path(self) -> None:
        client = Client(token="test-token", base_url="https://example.com/base/")
        self.addCleanup(client.close)
        self.assertEqual(
            client.websocket_url("/api/v1/sessions/ses_123/ws"),
            "wss://example.com/base/api/v1/sessions/ses_123/ws",
        )

    def test_create_session_passes_idempotency_key(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}
        value = _session_fixture()

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.CREATED,
                content=b"{}",
                headers={},
                parsed=SuccessExecutionSessionResponse(success=True, data=value),
            )

        with patch(
            "sandbox0.sandbox_sessions.post_api_v1_sandboxes_id_sessions.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            created = client.sandbox("sb_123").create_session(
                ExecutionSessionSpec(command=["/bin/echo", "hello"]),
                SessionCreateOptions(idempotency_key="create-1"),
            )

        self.assertEqual(created.id, "ses_123")
        self.assertEqual(captured["id"], "sb_123")
        self.assertEqual(captured["idempotency_key"], "create-1")

    def test_watch_session_events_resumes_cursor(self) -> None:
        seen = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen["path"] = request.url.path
            seen["query"] = dict(request.url.params)
            seen["last_event_id"] = request.headers.get("Last-Event-ID")
            return httpx.Response(
                200,
                headers={"Content-Type": "text/event-stream"},
                stream=httpx.ByteStream(
                    b": heartbeat\n\n"
                    b"id: 8\nevent: output\n"
                    b'data: {"seq":8,"session_id":"ses_123","runtime_generation":2,'
                    b'"type":"output","occurred_at":"2026-07-11T00:00:00Z"}\n\n'
                ),
            )

        client = Client(token="test-token", base_url="https://example.com/base")
        self.addCleanup(client.close)
        client.api.set_httpx_client(
            httpx.Client(
                base_url="https://example.com/base",
                headers={"Authorization": "Bearer test-token"},
                transport=httpx.MockTransport(handler),
            )
        )

        with client.sandbox("sb_123").watch_session_events(
            "ses_123", SessionEventStreamOptions(after=6, last_event_id="7")
        ) as stream:
            events = list(stream.iter_events())

        self.assertEqual(
            seen["path"], "/base/api/v1/sandboxes/sb_123/sessions/ses_123/events/stream"
        )
        self.assertEqual(seen["query"]["after"], "6")
        self.assertEqual(seen["last_event_id"], "7")
        self.assertEqual(events[0].seq, 8)
        self.assertEqual(
            events[0].occurred_at, datetime(2026, 7, 11, tzinfo=timezone.utc)
        )


def _session_fixture() -> ExecutionSession:
    now = datetime(2026, 7, 11, tzinfo=timezone.utc)
    return ExecutionSession(
        id="ses_123",
        spec=ExecutionSessionSpec(command=["/bin/echo", "hello"]),
        spec_version=1,
        phase=ExecutionSessionPhase.RUNNING,
        runtime_generation=2,
        restart_count=0,
        cursor=ExecutionSessionEventCursor(earliest=1, latest=7),
        created_at=now,
        updated_at=now,
        last_activity_at=now,
    )
