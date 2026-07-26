from datetime import datetime, timezone
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client, UsageWindow, UsageWindowPage
from sandbox0.apispec.models.success_usage_windows_response import (
    SuccessUsageWindowsResponse,
)
from sandbox0.apispec.types import Response


class TestUsage(TestCase):
    def setUp(self) -> None:
        self.client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(self.client.close)

    def test_list_usage_windows(self) -> None:
        window = UsageWindow(
            window_id="window-1",
            window_type="sandbox.runtime_mib_milliseconds",
            subject_type="sandbox",
            subject_id="sandbox-1",
            sandbox_id="sandbox-1",
            window_start=datetime(2026, 7, 26, tzinfo=timezone.utc),
            window_end=datetime(2026, 7, 26, 1, tzinfo=timezone.utc),
            value=3_686_400_000,
            unit="mib_milliseconds",
            recorded_at=datetime(2026, 7, 26, 1, 0, 1, tzinfo=timezone.utc),
        )
        page = UsageWindowPage(windows=[window], next_cursor="page-2")
        response = Response(
            status_code=HTTPStatus.OK,
            content=b"{}",
            headers={},
            parsed=SuccessUsageWindowsResponse(success=True, data=page),
        )

        with patch(
            "sandbox0.client_usage.get_api_v1_usage_windows.sync_detailed",
            return_value=response,
        ) as request:
            result = self.client.list_usage_windows(
                cursor="page-1",
                limit=250,
                window_type="sandbox.runtime_mib_milliseconds",
            )

        request.assert_called_once_with(
            client=self.client.api,
            cursor="page-1",
            limit=250,
            window_type="sandbox.runtime_mib_milliseconds",
        )
        self.assertIs(result, page)
        self.assertEqual(result.next_cursor, "page-2")
        self.assertEqual(result.windows[0].value, 3_686_400_000)
