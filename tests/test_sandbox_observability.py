from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch
from uuid import UUID

import httpx

from sandbox0 import (
    Client,
    SandboxObservabilityEventOptions,
    SandboxObservabilityEventWatchOptions,
    SandboxObservabilityLogOptions,
    SandboxObservabilityLogWatchOptions,
)
from sandbox0.apispec.models.observability_event_source import (
    ObservabilityEventSource,
)
from sandbox0.apispec.models.sandbox_audit_actor_kind import SandboxAuditActorKind
from sandbox0.apispec.models.sandbox_audit_integrity_signature_status import (
    SandboxAuditIntegritySignatureStatus,
)
from sandbox0.apispec.models.sandbox_observability_event_type import (
    SandboxObservabilityEventType,
)
from sandbox0.apispec.models.sandbox_observability_events_response import (
    SandboxObservabilityEventsResponse,
)
from sandbox0.apispec.models.sandbox_observability_logs_response import (
    SandboxObservabilityLogsResponse,
)
from sandbox0.apispec.models.sandbox_observability_watch_line_type import (
    SandboxObservabilityWatchLineType,
)
from sandbox0.apispec.models.sandbox_observability_outcome import (
    SandboxObservabilityOutcome,
)
from sandbox0.apispec.models.success_sandbox_observability_events_response import (
    SuccessSandboxObservabilityEventsResponse,
)
from sandbox0.apispec.models.success_sandbox_observability_logs_response import (
    SuccessSandboxObservabilityLogsResponse,
)
from sandbox0.apispec.types import Response
from sandbox0.response_normalize import normalize_response_hook


class TestSandboxObservability(TestCase):
    def test_list_events_uses_v2_filters_and_decodes_signed_event(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}
        event_id = UUID("c48d73ec-a08f-41bb-82d2-3f48a827f9b2")

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            parsed = SuccessSandboxObservabilityEventsResponse.from_dict(
                _signed_audit_response()
            )
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=parsed,
            )

        with patch(
            "sandbox0.sandbox_observability."
            "get_api_v1_sandboxes_id_observability_events.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            events = client.sandbox("sb_123").list_observability_events(
                SandboxObservabilityEventOptions(
                    limit=25,
                    source=ObservabilityEventSource.CLUSTER_GATEWAY,
                    event_type=SandboxObservabilityEventType.API_ACCESS,
                    outcome=SandboxObservabilityOutcome.SUCCEEDED,
                    actor_kind=SandboxAuditActorKind.API_KEY,
                    actor_id="key_1",
                    action="sandbox.read",
                    resource_type="sandbox",
                    operation_id="op_123",
                )
            )

        self.assertEqual(captured["id"], "sb_123")
        self.assertEqual(captured["actor_kind"], SandboxAuditActorKind.API_KEY)
        self.assertEqual(captured["actor_id"], "key_1")
        self.assertEqual(captured["action"], "sandbox.read")
        self.assertEqual(captured["resource_type"], "sandbox")
        self.assertEqual(captured["operation_id"], "op_123")
        self.assertEqual(events.events[0].event_id, event_id)
        self.assertEqual(events.events[0].actor.kind, SandboxAuditActorKind.API_KEY)
        self.assertEqual(
            events.events[0].integrity.signature_status,
            SandboxAuditIntegritySignatureStatus.VERIFIED,
        )

    def test_list_events_supports_exact_event_id(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}
        event_id = UUID("c48d73ec-a08f-41bb-82d2-3f48a827f9b2")

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessSandboxObservabilityEventsResponse(
                    success=True,
                    data=SandboxObservabilityEventsResponse(events=[]),
                ),
            )

        with patch(
            "sandbox0.sandbox_observability."
            "get_api_v1_sandboxes_id_observability_events.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            client.sandbox("sb_123").list_observability_events(
                SandboxObservabilityEventOptions(event_id=event_id)
            )

        self.assertEqual(captured["event_id"], event_id)

    def test_watch_events_uses_v2_filters(self) -> None:
        seen = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen["query"] = dict(request.url.params)
            return httpx.Response(
                200,
                headers={"Content-Type": "application/x-ndjson"},
                stream=httpx.ByteStream(
                    b'{"type":"watermark","cursor":"c1",'
                    b'"watermark":"2026-07-13T14:32:30Z"}\n'
                ),
            )

        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        client.api.set_httpx_client(
            httpx.Client(
                base_url="https://example.com",
                transport=httpx.MockTransport(handler),
            )
        )

        with client.sandbox("sb_123").watch_observability_events(
            SandboxObservabilityEventWatchOptions(
                actor_kind=SandboxAuditActorKind.SANDBOX_WORKLOAD,
                actor_id="sb_123",
                action="network.connect",
                resource_type="sandbox_network",
                operation_id="op_456",
            )
        ) as stream:
            lines = list(stream.iter_lines())

        self.assertEqual(seen["query"]["actor_kind"], "sandbox_workload")
        self.assertEqual(seen["query"]["actor_id"], "sb_123")
        self.assertEqual(seen["query"]["action"], "network.connect")
        self.assertEqual(seen["query"]["resource_type"], "sandbox_network")
        self.assertEqual(seen["query"]["operation_id"], "op_456")
        self.assertEqual(lines[0].cursor, "c1")

    def test_list_logs_uses_generated_observability_api(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.OK,
                content=b'{"data":{"logs":[]}}',
                headers={},
                parsed=SuccessSandboxObservabilityLogsResponse(
                    success=True, data=SandboxObservabilityLogsResponse(logs=[])
                ),
            )

        with patch(
            "sandbox0.sandbox_observability.get_api_v1_sandboxes_id_observability_logs.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            logs = client.sandbox("sb_123").list_logs(
                SandboxObservabilityLogOptions(limit=20, context_id="ctx_1")
            )

        self.assertEqual(logs.logs, [])
        self.assertEqual(captured["id"], "sb_123")
        self.assertEqual(captured["limit"], 20)
        self.assertEqual(captured["context_id"], "ctx_1")

    def test_watch_logs_returns_ndjson_stream(self) -> None:
        seen = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen["path"] = request.url.path
            seen["query"] = dict(request.url.params)
            seen["authorization"] = request.headers.get("Authorization")
            seen["accept"] = request.headers.get("Accept")
            return httpx.Response(
                200,
                headers={"Content-Type": "application/x-ndjson"},
                stream=httpx.ByteStream(
                    b'{"type":"heartbeat","time":"2026-07-03T00:00:00Z"}\n'
                    b'{"type":"watermark","cursor":"c1","watermark":"2026-07-03T00:00:01Z"}\n'
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

        with client.sandbox("sb_123").watch_logs(
            SandboxObservabilityLogWatchOptions(cursor="c0", limit=5)
        ) as stream:
            lines = list(stream.iter_lines())

        self.assertEqual(
            seen["path"], "/base/api/v1/sandboxes/sb_123/observability/logs"
        )
        self.assertEqual(seen["query"]["watch"], "true")
        self.assertEqual(seen["query"]["cursor"], "c0")
        self.assertEqual(seen["query"]["limit"], "5")
        self.assertEqual(seen["authorization"], "Bearer test-token")
        self.assertEqual(seen["accept"], "application/x-ndjson")
        self.assertEqual(lines[0].type_, SandboxObservabilityWatchLineType.HEARTBEAT)
        self.assertEqual(lines[1].cursor, "c1")

    def test_watch_logs_skips_response_normalize_hook(self) -> None:
        class FailOnReadStream(httpx.SyncByteStream):
            def __iter__(self):
                raise AssertionError("stream body was read by response hook")

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                200,
                headers={"Content-Type": "application/x-ndjson"},
                stream=FailOnReadStream(),
            )

        client = Client(token="test-token", base_url="https://example.com/base")
        self.addCleanup(client.close)
        client.api.set_httpx_client(
            httpx.Client(
                base_url="https://example.com/base",
                headers={"Authorization": "Bearer test-token"},
                transport=httpx.MockTransport(handler),
                event_hooks={"response": [normalize_response_hook]},
            )
        )

        with client.sandbox("sb_123").watch_logs(
            SandboxObservabilityLogWatchOptions(limit=5)
        ):
            pass


def _signed_audit_response() -> dict[str, object]:
    return {
        "success": True,
        "data": {
            "events": [
                {
                    "event_id": "c48d73ec-a08f-41bb-82d2-3f48a827f9b2",
                    "schema_version": 2,
                    "team_id": "team_1",
                    "sandbox_id": "sb_123",
                    "region_id": "region_1",
                    "cluster_id": "cluster_1",
                    "occurred_at": "2026-07-13T14:32:29Z",
                    "ingested_at": "2026-07-13T14:32:30Z",
                    "source": "cluster_gateway",
                    "event_type": "api_access",
                    "phase": "result",
                    "outcome": "succeeded",
                    "actor": {"kind": "api_key", "id": "key_1"},
                    "action": "sandbox.read",
                    "resource": {"type": "sandbox", "id": "sb_123"},
                    "operation_id": "op_123",
                    "producer": {"service": "cluster-gateway"},
                    "integrity": {
                        "algorithm": "ed25519-sha256-v1",
                        "payload_hash": "0" * 64,
                        "signature": "A" * 86,
                        "signing_key_id": "1" * 64,
                        "signature_status": "verified",
                        "event_id_conflict": False,
                    },
                    "attributes": {},
                }
            ],
            "next_cursor": "c2",
            "watermark": "2026-07-13T14:32:30Z",
        },
    }
