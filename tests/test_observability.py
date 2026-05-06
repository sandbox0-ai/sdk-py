import datetime
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.observability_log_record import ObservabilityLogRecord
from sandbox0.apispec.models.observability_trace_span import ObservabilityTraceSpan
from sandbox0.apispec.models.success_observability_log_record_list_response import (
    SuccessObservabilityLogRecordListResponse,
)
from sandbox0.apispec.models.success_observability_log_record_list_response_data import (
    SuccessObservabilityLogRecordListResponseData,
)
from sandbox0.apispec.models.success_observability_trace_span_list_response import (
    SuccessObservabilityTraceSpanListResponse,
)
from sandbox0.apispec.models.success_observability_trace_span_list_response_data import (
    SuccessObservabilityTraceSpanListResponseData,
)
from sandbox0.apispec.types import Response


class TestObservability(TestCase):
    def test_list_trace_spans_forwards_filters(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}
        start_time = datetime.datetime(2026, 5, 7, 0, 0, tzinfo=datetime.timezone.utc)
        end_time = datetime.datetime(2026, 5, 7, 1, 0, tzinfo=datetime.timezone.utc)

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessObservabilityTraceSpanListResponse(
                    success=True,
                    data=SuccessObservabilityTraceSpanListResponseData(
                        spans=[ObservabilityTraceSpan(trace_id="trace-1", span_id="span-1", name="managed-agent.run")]
                    ),
                ),
            )

        with patch(
            "sandbox0.client_observability.get_api_v1_observability_traces.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            spans = client.list_observability_trace_spans(
                sandbox_id="sb_123",
                trace_id="trace-1",
                start_time=start_time,
                end_time=end_time,
                limit=25,
            )

        self.assertEqual(captured["sandbox_id"], "sb_123")
        self.assertEqual(captured["trace_id"], "trace-1")
        self.assertEqual(captured["start_time"], start_time)
        self.assertEqual(captured["end_time"], end_time)
        self.assertEqual(captured["limit"], 25)
        self.assertEqual(spans[0].name, "managed-agent.run")

    def test_list_logs_forwards_filters(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessObservabilityLogRecordListResponse(
                    success=True,
                    data=SuccessObservabilityLogRecordListResponseData(
                        logs=[ObservabilityLogRecord(trace_id="trace-1", body="agent phase started")]
                    ),
                ),
            )

        with patch(
            "sandbox0.client_observability.get_api_v1_observability_logs.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            logs = client.list_observability_logs(
                sandbox_id="sb_123",
                trace_id="trace-1",
                limit=10,
            )

        self.assertEqual(captured["sandbox_id"], "sb_123")
        self.assertEqual(captured["trace_id"], "trace-1")
        self.assertEqual(captured["limit"], 10)
        self.assertEqual(logs[0].body, "agent phase started")
