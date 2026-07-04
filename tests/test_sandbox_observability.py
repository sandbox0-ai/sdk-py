from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

import httpx

from sandbox0 import Client, SandboxObservabilityLogOptions, SandboxObservabilityLogWatchOptions
from sandbox0.apispec.models.sandbox_observability_logs_response import (
    SandboxObservabilityLogsResponse,
)
from sandbox0.apispec.models.sandbox_observability_watch_line_type import (
    SandboxObservabilityWatchLineType,
)
from sandbox0.apispec.models.success_sandbox_observability_logs_response import (
    SuccessSandboxObservabilityLogsResponse,
)
from sandbox0.apispec.types import Response
from sandbox0.response_normalize import normalize_response_hook


class TestSandboxObservability(TestCase):
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
                    success=True,
                    data=SandboxObservabilityLogsResponse(logs=[])
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

        self.assertEqual(seen["path"], "/base/api/v1/sandboxes/sb_123/observability/logs")
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

        with client.sandbox("sb_123").watch_logs(SandboxObservabilityLogWatchOptions(limit=5)):
            pass
