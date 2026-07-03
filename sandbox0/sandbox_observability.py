from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any, Iterator, Optional

import httpx

from sandbox0.apispec.api.audit import get_api_v1_sandboxes_id_audit_events
from sandbox0.apispec.api.observability import (
    get_api_v1_sandboxes_id_observability_events,
)
from sandbox0.apispec.api.observability import (
    get_api_v1_sandboxes_id_observability_logs,
)
from sandbox0.apispec.api.observability import (
    get_api_v1_sandboxes_id_observability_metrics,
)
from sandbox0.apispec.models.observability_event_source import (
    ObservabilityEventSource,
)
from sandbox0.apispec.models.sandbox_observability_event_type import (
    SandboxObservabilityEventType,
)
from sandbox0.apispec.models.sandbox_observability_events_response import (
    SandboxObservabilityEventsResponse,
)
from sandbox0.apispec.models.sandbox_observability_log_stream import (
    SandboxObservabilityLogStream,
)
from sandbox0.apispec.models.sandbox_observability_logs_response import (
    SandboxObservabilityLogsResponse,
)
from sandbox0.apispec.models.sandbox_observability_metrics_response import (
    SandboxObservabilityMetricsResponse,
)
from sandbox0.apispec.models.sandbox_observability_outcome import (
    SandboxObservabilityOutcome,
)
from sandbox0.apispec.models.sandbox_observability_watch_line import (
    SandboxObservabilityWatchLine,
)
from sandbox0.apispec.models.success_sandbox_observability_events_response import (
    SuccessSandboxObservabilityEventsResponse,
)
from sandbox0.apispec.models.success_sandbox_observability_logs_response import (
    SuccessSandboxObservabilityLogsResponse,
)
from sandbox0.apispec.models.success_sandbox_observability_metrics_response import (
    SuccessSandboxObservabilityMetricsResponse,
)
from sandbox0.apispec.types import UNSET
from sandbox0.errors import APIError
from sandbox0.response import ensure_data
from sandbox0.response_normalize import SKIP_RESPONSE_NORMALIZE_EXTENSION

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


@dataclass(frozen=True)
class SandboxObservabilityQueryOptions:
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    limit: Optional[int] = None
    cursor: Optional[str] = None


@dataclass(frozen=True)
class SandboxObservabilityWatchOptions:
    start_time: Optional[datetime] = None
    limit: Optional[int] = None
    cursor: Optional[str] = None


@dataclass(frozen=True)
class SandboxObservabilityEventOptions(SandboxObservabilityQueryOptions):
    source: Optional[ObservabilityEventSource] = None
    event_type: Optional[SandboxObservabilityEventType] = None
    outcome: Optional[SandboxObservabilityOutcome] = None


@dataclass(frozen=True)
class SandboxObservabilityEventWatchOptions(SandboxObservabilityWatchOptions):
    source: Optional[ObservabilityEventSource] = None
    event_type: Optional[SandboxObservabilityEventType] = None
    outcome: Optional[SandboxObservabilityOutcome] = None


@dataclass(frozen=True)
class SandboxObservabilityLogOptions(SandboxObservabilityQueryOptions):
    context_id: Optional[str] = None
    stream: Optional[SandboxObservabilityLogStream] = None


@dataclass(frozen=True)
class SandboxObservabilityLogWatchOptions(SandboxObservabilityWatchOptions):
    context_id: Optional[str] = None
    stream: Optional[SandboxObservabilityLogStream] = None


@dataclass(frozen=True)
class SandboxObservabilityMetricOptions(SandboxObservabilityQueryOptions):
    context_id: Optional[str] = None
    name: Optional[list[str]] = None
    names: Optional[str] = None


@dataclass(frozen=True)
class SandboxObservabilityMetricWatchOptions(SandboxObservabilityWatchOptions):
    context_id: Optional[str] = None
    name: Optional[list[str]] = None
    names: Optional[str] = None


class SandboxObservabilityWatchStream:
    def __init__(self, response: httpx.Response) -> None:
        self._response = response

    @property
    def response(self) -> httpx.Response:
        return self._response

    def iter_bytes(self) -> Iterator[bytes]:
        return self._response.iter_bytes()

    def iter_text(self) -> Iterator[str]:
        return self._response.iter_text()

    def iter_lines(self) -> Iterator[SandboxObservabilityWatchLine]:
        for raw_line in self._response.iter_lines():
            line = raw_line.strip()
            if not line:
                continue
            yield SandboxObservabilityWatchLine.from_dict(json.loads(line))

    def close(self) -> None:
        self._response.close()

    def __enter__(self) -> "SandboxObservabilityWatchStream":
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()


class SandboxObservabilityMixin:
    id: str
    _client: Any

    def list_observability_events(
        self: "Sandbox",
        options: Optional[SandboxObservabilityEventOptions] = None,
    ) -> SandboxObservabilityEventsResponse:  # type: ignore[misc]
        opts = options or SandboxObservabilityEventOptions()
        resp = get_api_v1_sandboxes_id_observability_events.sync_detailed(
            id=self.id,
            client=self._client.api,
            start_time=_value(opts.start_time),
            end_time=_value(opts.end_time),
            limit=_value(opts.limit),
            cursor=_value(opts.cursor),
            source=_value(opts.source),
            event_type=_value(opts.event_type),
            outcome=_value(opts.outcome),
        )
        return ensure_data(resp, SuccessSandboxObservabilityEventsResponse)

    def list_audit_events(
        self: "Sandbox",
        options: Optional[SandboxObservabilityEventOptions] = None,
    ) -> SandboxObservabilityEventsResponse:  # type: ignore[misc]
        opts = options or SandboxObservabilityEventOptions()
        resp = get_api_v1_sandboxes_id_audit_events.sync_detailed(
            id=self.id,
            client=self._client.api,
            start_time=_value(opts.start_time),
            end_time=_value(opts.end_time),
            limit=_value(opts.limit),
            cursor=_value(opts.cursor),
            source=_value(opts.source),
            event_type=_value(opts.event_type),
            outcome=_value(opts.outcome),
        )
        return ensure_data(resp, SuccessSandboxObservabilityEventsResponse)

    def list_logs(
        self: "Sandbox",
        options: Optional[SandboxObservabilityLogOptions] = None,
    ) -> SandboxObservabilityLogsResponse:  # type: ignore[misc]
        opts = options or SandboxObservabilityLogOptions()
        resp = get_api_v1_sandboxes_id_observability_logs.sync_detailed(
            id=self.id,
            client=self._client.api,
            start_time=_value(opts.start_time),
            end_time=_value(opts.end_time),
            limit=_value(opts.limit),
            cursor=_value(opts.cursor),
            context_id=_value(opts.context_id),
            stream=_value(opts.stream),
        )
        return ensure_data(resp, SuccessSandboxObservabilityLogsResponse)

    def list_metrics(
        self: "Sandbox",
        options: Optional[SandboxObservabilityMetricOptions] = None,
    ) -> SandboxObservabilityMetricsResponse:  # type: ignore[misc]
        opts = options or SandboxObservabilityMetricOptions()
        resp = get_api_v1_sandboxes_id_observability_metrics.sync_detailed(
            id=self.id,
            client=self._client.api,
            start_time=_value(opts.start_time),
            end_time=_value(opts.end_time),
            limit=_value(opts.limit),
            cursor=_value(opts.cursor),
            context_id=_value(opts.context_id),
            name=_value(opts.name),
            names=_value(opts.names),
        )
        return ensure_data(resp, SuccessSandboxObservabilityMetricsResponse)

    def watch_observability_events(
        self: "Sandbox",
        options: Optional[SandboxObservabilityEventWatchOptions] = None,
    ) -> SandboxObservabilityWatchStream:  # type: ignore[misc]
        return self._watch_observability(
            f"/api/v1/sandboxes/{self.id}/observability/events",
            _event_params(options or SandboxObservabilityEventWatchOptions()),
        )

    def watch_audit_events(
        self: "Sandbox",
        options: Optional[SandboxObservabilityEventWatchOptions] = None,
    ) -> SandboxObservabilityWatchStream:  # type: ignore[misc]
        return self._watch_observability(
            f"/api/v1/sandboxes/{self.id}/audit/events",
            _event_params(options or SandboxObservabilityEventWatchOptions()),
        )

    def watch_logs(
        self: "Sandbox",
        options: Optional[SandboxObservabilityLogWatchOptions] = None,
    ) -> SandboxObservabilityWatchStream:  # type: ignore[misc]
        return self._watch_observability(
            f"/api/v1/sandboxes/{self.id}/observability/logs",
            _log_params(options or SandboxObservabilityLogWatchOptions()),
        )

    def watch_metrics(
        self: "Sandbox",
        options: Optional[SandboxObservabilityMetricWatchOptions] = None,
    ) -> SandboxObservabilityWatchStream:  # type: ignore[misc]
        return self._watch_observability(
            f"/api/v1/sandboxes/{self.id}/observability/metrics",
            _metric_params(options or SandboxObservabilityMetricWatchOptions()),
        )

    def _watch_observability(
        self: "Sandbox",
        path: str,
        params: dict[str, str],
    ) -> SandboxObservabilityWatchStream:  # type: ignore[misc]
        http_client = self._client.api.get_httpx_client()
        request = http_client.build_request(
            "GET",
            path,
            params={**params, "watch": "true"},
            headers={"Accept": "application/x-ndjson"},
        )
        request.extensions[SKIP_RESPONSE_NORMALIZE_EXTENSION] = True
        response = http_client.send(request, stream=True)
        if response.status_code < 200 or response.status_code >= 300:
            content = response.read()
            response.close()
            raise _api_error_from_response(response, content)
        content_type = response.headers.get("Content-Type", "")
        if content_type and not content_type.lower().startswith("application/x-ndjson"):
            response.close()
            raise APIError(
                status_code=response.status_code,
                code="unexpected_response",
                message=f"unexpected observability watch content type: {content_type}",
            )
        return SandboxObservabilityWatchStream(response)


def _event_params(options: SandboxObservabilityEventWatchOptions) -> dict[str, str]:
    params = _watch_params(options)
    if options.source is not None:
        params["source"] = options.source.value
    if options.event_type is not None:
        params["event_type"] = options.event_type.value
    if options.outcome is not None:
        params["outcome"] = options.outcome.value
    return params


def _log_params(options: SandboxObservabilityLogWatchOptions) -> dict[str, str]:
    params = _watch_params(options)
    if options.context_id:
        params["context_id"] = options.context_id
    if options.stream is not None:
        params["stream"] = options.stream.value
    return params


def _metric_params(options: SandboxObservabilityMetricWatchOptions) -> dict[str, str]:
    params = _watch_params(options)
    if options.context_id:
        params["context_id"] = options.context_id
    if options.name:
        params["name"] = ",".join(options.name)
    if options.names:
        params["names"] = options.names
    return params


def _watch_params(options: SandboxObservabilityWatchOptions) -> dict[str, str]:
    params: dict[str, str] = {}
    if options.start_time is not None:
        params["start_time"] = options.start_time.isoformat()
    if options.limit is not None:
        params["limit"] = str(options.limit)
    if options.cursor:
        params["cursor"] = options.cursor
    return params


def _value(value: Any) -> Any:
    if value is None:
        return UNSET
    return value


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
