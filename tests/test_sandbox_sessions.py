from datetime import datetime, timezone
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

import httpx

from sandbox0 import Client, SessionCreateOptions, SessionEventStreamOptions, SessionWebSocketOptions
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
    def test_find_conditional_session_never_creates_or_resumes(self) -> None:
        calls = []
        state = {"status": 200, "generation": 2}
        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request)
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.url.path, "/api/v1/sandboxes/sb_123/sessions/conditional/lookup")
            self.assertEqual(request.url.params["runtime_generation"], "2")
            self.assertEqual(request.headers["Idempotency-Key"], "original-key")
            fixture = _session_fixture()
            fixture.runtime_generation = state["generation"]
            return httpx.Response(state["status"], json=(
                {"success": True, "data": fixture.to_dict()} if state["status"] == 200
                else {"success": False, "error": {"code": "session_not_found", "message": "unavailable"}}
            ), headers={"Cache-Control": "no-store"})
        client = Client(token="fixture", base_url="https://example.com")
        self.addCleanup(client.close)
        client.api.set_httpx_client(httpx.Client(base_url="https://example.com", transport=httpx.MockTransport(handler)))
        sandbox = client.sandbox("sb_123")
        self.assertEqual(sandbox.find_conditional_session("original-key", 2).id, "ses_123")
        for status in [404, 405, 409, 503]:
            state["status"] = status
            with self.assertRaises(Exception):
                sandbox.find_conditional_session("original-key", 2)
        state.update(status=200, generation=3)
        with self.assertRaisesRegex(ValueError, "different runtime generation"):
            sandbox.find_conditional_session("original-key", 2)
        for generation in [0, -1, True, 2**63]:
            with self.assertRaises(ValueError):
                sandbox.find_conditional_session("original-key", generation)
        with self.assertRaises(ValueError):
            sandbox.find_conditional_session("", 2)
        self.assertEqual(len(calls), 6)

    def test_conditional_session_has_no_unconditional_fallback(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        spec = ExecutionSessionSpec(command=["/bin/true"])
        options = SessionCreateOptions(idempotency_key="conditional-key", runtime_generation=7)
        with patch("sandbox0.sandbox_sessions.post_api_v1_sandboxes_id_sessions_conditional.sync_detailed") as conditional, patch(
            "sandbox0.sandbox_sessions.post_api_v1_sandboxes_id_sessions.sync_detailed"
        ) as legacy:
            fixture = _session_fixture()
            fixture.runtime_generation = 7
            conditional.return_value = Response(status_code=HTTPStatus.CREATED, content=b"{}", headers={},
                parsed=SuccessExecutionSessionResponse(success=True, data=fixture))
            client.sandbox("sb_123").create_session(spec, options)
            kwargs = conditional.call_args.kwargs
            self.assertEqual(kwargs["body"].sandbox_id, "sb_123")
            self.assertEqual(kwargs["body"].runtime_generation, 7)
            self.assertEqual(kwargs["idempotency_key"], "conditional-key")
            conditional.side_effect = RuntimeError("unsupported conditional route")
            with self.assertRaises(RuntimeError):
                client.sandbox("sb_123").create_session(spec, options)
            conditional.side_effect = None
            fixture.runtime_generation = 8
            with self.assertRaises(ValueError):
                client.sandbox("sb_123").create_session(spec, options)
            for generation in [0, -1, True, 2**63]:
                with self.assertRaises(ValueError):
                    client.sandbox("sb_123").create_session(spec, SessionCreateOptions(idempotency_key="key", runtime_generation=generation))
            with self.assertRaises(ValueError):
                client.sandbox("sb_123").create_session(spec, SessionCreateOptions(runtime_generation=7))
            self.assertEqual(conditional.call_count, 3)
            legacy.assert_not_called()

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


class ConditionalAttachmentTests(TestCase):
    def test_exact_handshake_invalid_inputs_and_no_fallback(self) -> None:
        from urllib.parse import urlparse, parse_qs
        sandbox = Client(token="fixture", base_url="http://example.test").sandbox("sandbox")
        with patch("websockets.sync.client.connect") as connect:
            sandbox.connect_conditional_session("session", "original", 7, "attempt", SessionWebSocketOptions(after=5))
            args, kwargs = connect.call_args
            url = urlparse(args[0])
            self.assertEqual(url.path, "/api/v1/sandboxes/sandbox/sessions/session/conditional/ws")
            self.assertEqual(parse_qs(url.query), {"runtime_generation":["7"],"attempt_id":["attempt"],"after":["5"]})
            self.assertEqual(kwargs["additional_headers"]["Idempotency-Key"], "original")
            for code in [404,405,409,503]:
                connect.side_effect = RuntimeError(str(code))
                with self.assertRaisesRegex(RuntimeError,str(code)):
                    sandbox.connect_conditional_session("session","original",7,"attempt")
            for gen in [0,-1,True,2**63]:
                with self.assertRaises(ValueError): sandbox.connect_conditional_session("session","original",gen,"attempt")
            for args in [("","original","attempt"),("session","","attempt"),("session","original","")]:
                with self.assertRaises(ValueError): sandbox.connect_conditional_session(args[0],args[1],7,args[2])
            for cursor in [-1,True,2**63]:
                with self.assertRaises(ValueError): sandbox.connect_conditional_session("session","original",7,"attempt",SessionWebSocketOptions(after=cursor))
            self.assertEqual(connect.call_count,5)

class RestoredConditionalAttachmentTests(TestCase):
    def test_exact_handshake_invalid_inputs_and_no_fallback(self) -> None:
        from urllib.parse import urlparse, parse_qs
        sandbox = Client(token="fixture", base_url="http://example.test").sandbox("sandbox")
        with patch("websockets.sync.client.connect") as connect:
            sandbox.connect_restored_conditional_session("session", "original", 7, 1, "attempt", SessionWebSocketOptions(after=5))
            args, kwargs = connect.call_args
            url = urlparse(args[0])
            self.assertEqual(url.path, "/api/v1/sandboxes/sandbox/sessions/session/conditional/ws")
            self.assertEqual(parse_qs(url.query), {"creation_runtime_generation":["1"],"runtime_generation":["7"],"attempt_id":["attempt"],"after":["5"]})
            self.assertEqual(kwargs["additional_headers"]["Idempotency-Key"], "original")
            for code in [404,405,409,503]:
                connect.side_effect = RuntimeError(str(code))
                with self.assertRaisesRegex(RuntimeError,str(code)):
                    sandbox.connect_restored_conditional_session("session","original",7,1,"attempt")
            for gen in [0,-1,True,2**63]:
                with self.assertRaises(ValueError): sandbox.connect_restored_conditional_session("session","original",gen,1,"attempt")
            for args in [("","original","attempt"),("session","","attempt"),("session","original","")]:
                with self.assertRaises(ValueError): sandbox.connect_restored_conditional_session(args[0],args[1],7,1,args[2])
            for cursor in [-1,True,2**63]:
                with self.assertRaises(ValueError): sandbox.connect_restored_conditional_session("session","original",7,1,"attempt",SessionWebSocketOptions(after=cursor))
            self.assertEqual(connect.call_count,5)
