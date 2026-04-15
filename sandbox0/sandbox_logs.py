from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Iterator, Optional

import httpx

from sandbox0.errors import APIError
from sandbox0.response_normalize import SKIP_RESPONSE_NORMALIZE_EXTENSION

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


@dataclass(frozen=True)
class SandboxLogsOptions:
    container: str = ""
    tail_lines: Optional[int] = None
    limit_bytes: Optional[int] = None
    previous: bool = False
    timestamps: bool = False
    since_seconds: Optional[int] = None


@dataclass(frozen=True)
class SandboxLogs:
    sandbox_id: str
    pod_name: str
    container: str
    previous: bool
    logs: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "sandbox_id": self.sandbox_id,
            "pod_name": self.pod_name,
            "container": self.container,
            "previous": self.previous,
            "logs": self.logs,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SandboxLogs":
        return cls(
            sandbox_id=str(data.get("sandbox_id", "")),
            pod_name=str(data.get("pod_name", "")),
            container=str(data.get("container", "")),
            previous=bool(data.get("previous", False)),
            logs=str(data.get("logs", "")),
        )


class SandboxLogStream:
    def __init__(self, response: httpx.Response) -> None:
        self._response = response
        self.sandbox_id = response.headers.get("X-Sandbox-ID", "")
        self.pod_name = response.headers.get("X-Sandbox-Pod-Name", "")
        self.container = response.headers.get("X-Sandbox-Log-Container", "")
        self.previous = _bool_header(response.headers.get("X-Sandbox-Log-Previous"), False)

    @property
    def response(self) -> httpx.Response:
        return self._response

    def iter_bytes(self) -> Iterator[bytes]:
        yield from self._response.iter_bytes()

    def iter_text(self) -> Iterator[str]:
        return self._response.iter_text()

    def read(self) -> bytes:
        return self._response.read()

    def close(self) -> None:
        self._response.close()

    def __enter__(self) -> "SandboxLogStream":
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()


class SandboxLogsMixin:
    id: str
    _client: Any

    def get_logs(self: "Sandbox", options: Optional[SandboxLogsOptions] = None) -> SandboxLogs:  # type: ignore[misc]
        opts = options or SandboxLogsOptions()
        http_client = self._client.api.get_httpx_client()
        request = http_client.build_request(
            "GET",
            f"/api/v1/sandboxes/{self.id}/logs",
            params=_logs_params(opts, follow=False),
        )
        request.extensions[SKIP_RESPONSE_NORMALIZE_EXTENSION] = True
        response = http_client.send(request)
        try:
            if response.status_code < 200 or response.status_code >= 300:
                raise _api_error_from_response(response, response.read())
            content_type = response.headers.get("Content-Type", "")
            if _has_content_type_prefix(content_type, "application/json"):
                payload = response.json()
                return SandboxLogs.from_dict(payload.get("data") or {})
            if content_type and not _has_content_type_prefix(content_type, "text/plain"):
                raise APIError(
                    status_code=response.status_code,
                    code="unexpected_response",
                    message=f"unexpected log snapshot content type: {content_type}",
                )
            return _sandbox_logs_from_response(response, self.id, opts, response.text)
        finally:
            response.close()

    def stream_logs(self: "Sandbox", options: Optional[SandboxLogsOptions] = None) -> SandboxLogStream:  # type: ignore[misc]
        opts = options or SandboxLogsOptions()
        http_client = self._client.api.get_httpx_client()
        request = http_client.build_request(
            "GET",
            f"/api/v1/sandboxes/{self.id}/logs",
            params=_logs_params(opts, follow=True),
        )
        request.extensions[SKIP_RESPONSE_NORMALIZE_EXTENSION] = True
        response = http_client.send(request, stream=True)
        if response.status_code < 200 or response.status_code >= 300:
            content = response.read()
            response.close()
            raise _api_error_from_response(response, content)
        content_type = response.headers.get("Content-Type", "")
        if content_type and not _has_content_type_prefix(content_type, "text/plain"):
            response.close()
            raise APIError(
                status_code=response.status_code,
                code="unexpected_response",
                message=f"unexpected log stream content type: {content_type}",
            )
        return SandboxLogStream(response)


def _logs_params(options: SandboxLogsOptions, follow: bool) -> dict[str, str]:
    params: dict[str, str] = {"follow": "true" if follow else "false"}
    if options.container:
        params["container"] = options.container
    if options.tail_lines is not None:
        params["tail_lines"] = str(options.tail_lines)
    if options.limit_bytes is not None:
        params["limit_bytes"] = str(options.limit_bytes)
    if options.previous:
        params["previous"] = "true"
    if options.timestamps:
        params["timestamps"] = "true"
    if options.since_seconds is not None:
        params["since_seconds"] = str(options.since_seconds)
    return params


def _sandbox_logs_from_response(response: httpx.Response, sandbox_id: str, options: SandboxLogsOptions, logs: str) -> SandboxLogs:
    return SandboxLogs(
        sandbox_id=response.headers.get("X-Sandbox-ID") or sandbox_id,
        pod_name=response.headers.get("X-Sandbox-Pod-Name", ""),
        container=response.headers.get("X-Sandbox-Log-Container", ""),
        previous=_bool_header(response.headers.get("X-Sandbox-Log-Previous"), options.previous),
        logs=logs,
    )


def _bool_header(value: Optional[str], fallback: bool) -> bool:
    if value is None:
        return fallback
    return value.lower() == "true"


def _has_content_type_prefix(content_type: str, expected: str) -> bool:
    return content_type.lower().startswith(expected)


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
        message=content.decode("utf-8", errors="replace").strip() or response.reason_phrase,
        request_id=response.headers.get("X-Request-ID"),
        body=content,
    )
