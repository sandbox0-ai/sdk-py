from __future__ import annotations

import datetime
from typing import Any, List, TYPE_CHECKING

from sandbox0.apispec.api.observability import get_api_v1_observability_logs
from sandbox0.apispec.api.observability import get_api_v1_observability_traces
from sandbox0.apispec.models.observability_log_record import ObservabilityLogRecord
from sandbox0.apispec.models.observability_trace_span import ObservabilityTraceSpan
from sandbox0.apispec.models.success_observability_log_record_list_response import (
    SuccessObservabilityLogRecordListResponse,
)
from sandbox0.apispec.models.success_observability_trace_span_list_response import (
    SuccessObservabilityTraceSpanListResponse,
)
from sandbox0.apispec.types import UNSET
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.client import Client


class ClientObservabilityMixin:
    _api: Any

    def list_observability_trace_spans(  # type: ignore[misc]
        self: "Client",
        *,
        sandbox_id: str = UNSET,  # type: ignore[assignment]
        trace_id: str = UNSET,  # type: ignore[assignment]
        start_time: datetime.datetime = UNSET,  # type: ignore[assignment]
        end_time: datetime.datetime = UNSET,  # type: ignore[assignment]
        limit: int = 100,
    ) -> List[ObservabilityTraceSpan]:
        resp = get_api_v1_observability_traces.sync_detailed(
            client=self._api,
            sandbox_id=sandbox_id,
            trace_id=trace_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        data = ensure_data(resp, SuccessObservabilityTraceSpanListResponse)
        return [] if data.spans.__class__.__name__ == "Unset" else list(data.spans)

    def list_observability_logs(  # type: ignore[misc]
        self: "Client",
        *,
        sandbox_id: str = UNSET,  # type: ignore[assignment]
        trace_id: str = UNSET,  # type: ignore[assignment]
        start_time: datetime.datetime = UNSET,  # type: ignore[assignment]
        end_time: datetime.datetime = UNSET,  # type: ignore[assignment]
        limit: int = 100,
    ) -> List[ObservabilityLogRecord]:
        resp = get_api_v1_observability_logs.sync_detailed(
            client=self._api,
            sandbox_id=sandbox_id,
            trace_id=trace_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
        )
        data = ensure_data(resp, SuccessObservabilityLogRecordListResponse)
        return [] if data.logs.__class__.__name__ == "Unset" else list(data.logs)
