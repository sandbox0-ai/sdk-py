from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

import httpx

from sandbox0 import Client, SandboxLogsOptions
from sandbox0.apispec.types import Response
from sandbox0.response_normalize import normalize_response_hook


class TestSandboxLogs(TestCase):
    def test_get_logs_uses_generated_api(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"ready\n",
                headers={
                    "X-Sandbox-ID": "sb_123",
                    "X-Sandbox-Pod-Name": "pod-a",
                    "X-Sandbox-Log-Container": "procd",
                },
                parsed="ready\n",
            )

        with patch("sandbox0.sandbox_logs.get_api_v1_sandboxes_id_logs.sync_detailed", side_effect=fake_sync_detailed):
            logs = client.sandbox("sb_123").get_logs(SandboxLogsOptions(tail_lines=20, timestamps=True))

        self.assertEqual(logs.logs, "ready\n")
        self.assertEqual(captured["id"], "sb_123")
        self.assertEqual(captured["tail_lines"], 20)
        self.assertEqual(captured["timestamps"], True)
        self.assertEqual(captured["follow"], False)

    def test_stream_logs_returns_live_response(self) -> None:
        seen = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen["path"] = request.url.path
            seen["query"] = dict(request.url.params)
            seen["authorization"] = request.headers.get("Authorization")
            return httpx.Response(
                200,
                headers={
                    "Content-Type": "text/plain; charset=utf-8",
                    "X-Sandbox-ID": "sb_123",
                    "X-Sandbox-Pod-Name": "pod-a",
                    "X-Sandbox-Log-Container": "procd",
                },
                stream=httpx.ByteStream(b"line one\n"),
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

        with client.sandbox("sb_123").stream_logs(SandboxLogsOptions(tail_lines=5)) as stream:
            self.assertEqual(stream.sandbox_id, "sb_123")
            self.assertEqual(stream.pod_name, "pod-a")
            self.assertEqual(stream.container, "procd")
            self.assertEqual(stream.read(), b"line one\n")

        self.assertEqual(seen["path"], "/base/api/v1/sandboxes/sb_123/logs")
        self.assertEqual(seen["query"]["follow"], "true")
        self.assertEqual(seen["query"]["tail_lines"], "5")
        self.assertEqual(seen["authorization"], "Bearer test-token")

    def test_stream_logs_skips_response_normalize_hook(self) -> None:
        class FailOnReadStream(httpx.SyncByteStream):
            def __iter__(self):
                raise AssertionError("stream body was read by response hook")

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                200,
                headers={"Content-Type": "text/plain"},
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

        with client.sandbox("sb_123").stream_logs(SandboxLogsOptions(tail_lines=5)):
            pass
