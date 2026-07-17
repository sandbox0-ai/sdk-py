from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Iterator, Optional, Union
from uuid import UUID

import httpx

from sandbox0.apispec.api.observability import (
    get_api_v1_sandboxes_id_observability_events,
)
from sandbox0.apispec.api.observability import (
    get_api_v1_sandboxes_id_observability_logs,
)
from sandbox0.apispec.api.observability import (
    get_sandbox_runtime_metrics,
)
from sandbox0.apispec.api.observability import (
    get_sandbox_runtime_metrics_catalog,
)
from sandbox0.apispec.models.observability_event_source import (
    ObservabilityEventSource,
)
from sandbox0.apispec.models.sandbox_audit_actor_kind import SandboxAuditActorKind
from sandbox0.apispec.models.sandbox_audit_execution_scope_attribution import (
    SandboxAuditExecutionScopeAttribution,
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
from sandbox0.apispec.models.sandbox_runtime_metric_name import (
    SandboxRuntimeMetricName,
)
from sandbox0.apispec.models.sandbox_runtime_metric_statistic import (
    SandboxRuntimeMetricStatistic,
)
from sandbox0.apispec.models.sandbox_runtime_metrics_catalog_response import (
    SandboxRuntimeMetricsCatalogResponse,
)
from sandbox0.apispec.models.sandbox_runtime_metrics_response import (
    SandboxRuntimeMetricsResponse,
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
from sandbox0.apispec.models.success_sandbox_runtime_metrics_catalog_response import (
    SuccessSandboxRuntimeMetricsCatalogResponse,
)
from sandbox0.apispec.models.success_sandbox_runtime_metrics_response import (
    SuccessSandboxRuntimeMetricsResponse,
)
from sandbox0.apispec.types import UNSET
from sandbox0.errors import APIError
from sandbox0.response import ensure_data
from sandbox0.response_normalize import SKIP_RESPONSE_NORMALIZE_EXTENSION


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
    max_schema_version: int = 3
    source: Optional[ObservabilityEventSource] = None
    event_type: Optional[SandboxObservabilityEventType] = None
    outcome: Optional[SandboxObservabilityOutcome] = None
    actor_kind: Optional[SandboxAuditActorKind] = None
    actor_id: Optional[str] = None
    execution_scope_namespace: Optional[str] = None
    execution_scope_kind: Optional[str] = None
    execution_scope_id: Optional[str] = None
    execution_scope_attribution: Optional[
        SandboxAuditExecutionScopeAttribution
    ] = None
    action: Optional[str] = None
    resource_type: Optional[str] = None
    operation_id: Optional[str] = None
    event_id: Optional[UUID] = None


@dataclass(frozen=True)
class SandboxObservabilityEventWatchOptions(SandboxObservabilityWatchOptions):
    max_schema_version: int = 3
    source: Optional[ObservabilityEventSource] = None
    event_type: Optional[SandboxObservabilityEventType] = None
    outcome: Optional[SandboxObservabilityOutcome] = None
    actor_kind: Optional[SandboxAuditActorKind] = None
    actor_id: Optional[str] = None
    execution_scope_namespace: Optional[str] = None
    execution_scope_kind: Optional[str] = None
    execution_scope_id: Optional[str] = None
    execution_scope_attribution: Optional[
        SandboxAuditExecutionScopeAttribution
    ] = None
    action: Optional[str] = None
    resource_type: Optional[str] = None
    operation_id: Optional[str] = None


@dataclass(frozen=True)
class SandboxObservabilityLogOptions(SandboxObservabilityQueryOptions):
    context_id: Optional[str] = None
    stream: Optional[SandboxObservabilityLogStream] = None


@dataclass(frozen=True)
class SandboxObservabilityLogWatchOptions(SandboxObservabilityWatchOptions):
    context_id: Optional[str] = None
    stream: Optional[SandboxObservabilityLogStream] = None


@dataclass(frozen=True)
class SandboxObservabilityMetricOptions:
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    metrics: Optional[list[SandboxRuntimeMetricName]] = None
    step_seconds: Optional[int] = None
    statistic: Optional[SandboxRuntimeMetricStatistic] = None
    max_points: Optional[int] = None


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
        self,
        options: Optional[SandboxObservabilityEventOptions] = None,
    ) -> SandboxObservabilityEventsResponse:  # type: ignore[misc]
        opts = options or SandboxObservabilityEventOptions()
        _validate_execution_scope_schema(opts)
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
            actor_kind=_value(opts.actor_kind),
            actor_id=_value(opts.actor_id),
            execution_scope_namespace=_value(opts.execution_scope_namespace),
            execution_scope_kind=_value(opts.execution_scope_kind),
            execution_scope_id=_value(opts.execution_scope_id),
            execution_scope_attribution=_value(
                opts.execution_scope_attribution
            ),
            action=_value(opts.action),
            resource_type=_value(opts.resource_type),
            operation_id=_value(opts.operation_id),
            event_id=_value(opts.event_id),
            max_schema_version=opts.max_schema_version,
        )
        return ensure_data(resp, SuccessSandboxObservabilityEventsResponse)

    def list_logs(
        self,
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
        self,
        options: Optional[SandboxObservabilityMetricOptions] = None,
    ) -> SandboxRuntimeMetricsResponse:  # type: ignore[misc]
        opts = options or SandboxObservabilityMetricOptions()
        resp = get_sandbox_runtime_metrics.sync_detailed(
            id=self.id,
            client=self._client.api,
            start_time=_value(opts.start_time),
            end_time=_value(opts.end_time),
            metrics=_value(
                ",".join(metric.value for metric in opts.metrics)
                if opts.metrics
                else None
            ),
            step_seconds=_value(opts.step_seconds),
            statistic=_value(opts.statistic),
            max_points=_value(opts.max_points),
        )
        return ensure_data(resp, SuccessSandboxRuntimeMetricsResponse)

    def get_metrics_catalog(self) -> SandboxRuntimeMetricsCatalogResponse:  # type: ignore[misc]
        resp = get_sandbox_runtime_metrics_catalog.sync_detailed(
            id=self.id,
            client=self._client.api,
        )
        return ensure_data(resp, SuccessSandboxRuntimeMetricsCatalogResponse)

    def watch_observability_events(
        self,
        options: Optional[SandboxObservabilityEventWatchOptions] = None,
    ) -> SandboxObservabilityWatchStream:  # type: ignore[misc]
        opts = options or SandboxObservabilityEventWatchOptions()
        _validate_execution_scope_schema(opts)
        return self._watch_observability(
            f"/api/v1/sandboxes/{self.id}/observability/events",
            _event_params(opts),
        )

    def watch_logs(
        self,
        options: Optional[SandboxObservabilityLogWatchOptions] = None,
    ) -> SandboxObservabilityWatchStream:  # type: ignore[misc]
        return self._watch_observability(
            f"/api/v1/sandboxes/{self.id}/observability/logs",
            _log_params(options or SandboxObservabilityLogWatchOptions()),
        )

    def _watch_observability(
        self,
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
    params["max_schema_version"] = str(options.max_schema_version)
    if options.source is not None:
        params["source"] = options.source.value
    if options.event_type is not None:
        params["event_type"] = options.event_type.value
    if options.outcome is not None:
        params["outcome"] = options.outcome.value
    if options.actor_kind is not None:
        params["actor_kind"] = options.actor_kind.value
    if options.actor_id:
        params["actor_id"] = options.actor_id
    if options.execution_scope_namespace:
        params["execution_scope_namespace"] = options.execution_scope_namespace
    if options.execution_scope_kind:
        params["execution_scope_kind"] = options.execution_scope_kind
    if options.execution_scope_id:
        params["execution_scope_id"] = options.execution_scope_id
    if options.execution_scope_attribution is not None:
        params["execution_scope_attribution"] = (
            options.execution_scope_attribution.value
        )
    if options.action:
        params["action"] = options.action
    if options.resource_type:
        params["resource_type"] = options.resource_type
    if options.operation_id:
        params["operation_id"] = options.operation_id
    return params


def _validate_execution_scope_schema(
    options: Union[
        SandboxObservabilityEventOptions,
        SandboxObservabilityEventWatchOptions,
    ],
) -> None:
    has_scope_filter = any(
        (
            options.execution_scope_namespace,
            options.execution_scope_kind,
            options.execution_scope_id,
            options.execution_scope_attribution,
        )
    )
    if has_scope_filter and options.max_schema_version < 3:
        raise ValueError(
            "sandbox observability execution scope filters require "
            "max_schema_version >= 3"
        )


def _log_params(options: SandboxObservabilityLogWatchOptions) -> dict[str, str]:
    params = _watch_params(options)
    if options.context_id:
        params["context_id"] = options.context_id
    if options.stream is not None:
        params["stream"] = options.stream.value
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
