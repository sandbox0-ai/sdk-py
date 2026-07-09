import json
from unittest import TestCase

import httpx

from sandbox0 import Client, ProcessEventWatchOptions, process_stdio_spec


class TestSandboxProcesses(TestCase):
    def test_create_process_and_send_input(self) -> None:
        seen = {}

        def handler(request: httpx.Request) -> httpx.Response:
            seen.setdefault("requests", []).append((request.method, request.url.path, json.loads(request.content)))
            if request.method == "POST" and request.url.path == "/base/api/v1/sandboxes/sb_123/processes":
                return httpx.Response(
                    201,
                    json={
                        "success": True,
                        "data": {
                            "process": {
                                "id": "proc_1",
                                "command": ["python", "-u"],
                                "state": "running",
                                "created_at": "2026-07-09T00:00:00Z",
                                "channels": [{"name": "stdio", "kind": "stdio"}],
                                "event_log": {"next_seq": 1, "oldest_seq": 1, "capacity": 1024},
                            }
                        },
                    },
                )
            if request.method == "POST" and request.url.path == "/base/api/v1/sandboxes/sb_123/processes/proc_1/events":
                return httpx.Response(
                    202,
                    json={
                        "success": True,
                        "data": {
                            "event": {
                                "seq": 2,
                                "event_id": "evt_1",
                                "process_id": "proc_1",
                                "channel": "stdio",
                                "type": "stdin.write",
                                "timestamp": "2026-07-09T00:00:01Z",
                                "payload": {"data": "hello\n"},
                            }
                        },
                    },
                )
            raise AssertionError(f"unexpected request: {request.method} {request.url}")

        client = Client(token="test-token", base_url="https://example.com/base")
        self.addCleanup(client.close)
        client.api.set_httpx_client(
            httpx.Client(
                base_url="https://example.com/base",
                headers={"Authorization": "Bearer test-token"},
                transport=httpx.MockTransport(handler),
            )
        )

        process = client.sandbox("sb_123").create_process(process_stdio_spec(["python", "-u"]))
        event = client.sandbox("sb_123").send_process_input("proc_1", "stdio", "hello\n", event_id="evt_1")

        self.assertEqual(process.id, "proc_1")
        self.assertEqual(event.seq, 2)
        self.assertEqual(seen["requests"][0][2]["command"], ["python", "-u"])
        self.assertEqual(seen["requests"][1][2]["event_id"], "evt_1")
        self.assertEqual(seen["requests"][1][2]["payload"]["data"], "hello\n")

    def test_watch_process_events_resumes_from_cursor(self) -> None:
        seen_queries = []

        def handler(request: httpx.Request) -> httpx.Response:
            self.assertEqual(request.method, "GET")
            self.assertEqual(request.url.path, "/base/api/v1/sandboxes/sb_123/processes/proc_1/events")
            seen_queries.append(dict(request.url.params))
            seq = 2 if request.url.params.get("cursor") == "1" else 1
            return httpx.Response(
                200,
                headers={"Content-Type": "text/event-stream"},
                stream=httpx.ByteStream(
                    f'data: {{"seq":{seq},"process_id":"proc_1","channel":"stdio","type":"stdout.line","timestamp":"2026-07-09T00:00:0{seq}Z","payload":{{"data":"line-{seq}"}}}}\n\n'.encode()
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

        with client.sandbox("sb_123").watch_process_events("proc_1") as stream:
            first = list(stream.iter_events())
        with client.sandbox("sb_123").watch_process_events(
            "proc_1",
            ProcessEventWatchOptions(cursor=first[0].seq),
        ) as stream:
            resumed = list(stream.iter_events())

        self.assertEqual(first[0].seq, 1)
        self.assertEqual(first[0].payload["data"], "line-1")
        self.assertEqual(resumed[0].seq, 2)
        self.assertEqual(seen_queries[1]["cursor"], "1")
