from __future__ import annotations

import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Iterator, Optional

import httpx

from sandbox0.apispec.api.sandboxes import get_api_v1_sandboxes_id_logs
from sandbox0.errors import APIError
from sandbox0.models import SandboxLogs
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


class SandboxLogStream:
    def __init__(self, response: httpx.Response) -> None:
        self._response = response
        self.sandbox_id = response.headers.get("X-Sandbox-ID", "")
        self.pod_name = response.headers.get("X-Sandbox-Pod-Name", "")
        self.container = response.headers.get("X-Sandbox-Log-Container", "")

    @property
    def response(self) -> httpx.Response:
        return self._response

    def iter_bytes(self) -> Iterator[bytes]:
        return self._response.iter_bytes()

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
        resp = get_api_v1_sandboxes_id_logs.sync_detailed(
            id=self.id,
            client=self._client.api,
            container=opts.container or "procd",
            tail_lines=200 if opts.tail_lines is None else opts.tail_lines,
            limit_bytes=1048576 if opts.limit_bytes is None else opts.limit_bytes,
            follow=False,
            previous=opts.previous,
            timestamps=opts.timestamps,
            since_seconds=opts.since_seconds if opts.since_seconds is not None else _unset(),
        )
        if resp.status_code.value < 200 or resp.status_code.value >= 300:
            raise _api_error_from_response(httpx.Response(resp.status_code.value, content=resp.content, headers=resp.headers), resp.content)
        return SandboxLogs(
            sandbox_id=resp.headers.get("X-Sandbox-ID", self.id),
            pod_name=resp.headers.get("X-Sandbox-Pod-Name", ""),
            container=resp.headers.get("X-Sandbox-Log-Container", ""),
            previous=resp.headers.get("X-Sandbox-Log-Previous", "").lower() == "true",
            logs=resp.content.decode("utf-8", errors="replace"),
        )

    def stream_logs(self: "Sandbox", options: Optional[SandboxLogsOptions] = None) -> SandboxLogStream:  # type: ignore[misc]
        opts = options or SandboxLogsOptions()
        http_client = self._client.api.get_httpx_client()
        request = http_client.build_request(
            "GET",
            f"/api/v1/sandboxes/{self.id}/logs",
            params=_stream_params(opts),
        )
        request.extensions[SKIP_RESPONSE_NORMALIZE_EXTENSION] = True
        response = http_client.send(request, stream=True)
        if response.status_code < 200 or response.status_code >= 300:
            content = response.read()
            response.close()
            raise _api_error_from_response(response, content)
        content_type = response.headers.get("Content-Type", "")
        if content_type and not content_type.lower().startswith("text/plain"):
            response.close()
            raise APIError(
                status_code=response.status_code,
                code="unexpected_response",
                message=f"unexpected log stream content type: {content_type}",
            )
        return SandboxLogStream(response)


def _stream_params(options: SandboxLogsOptions) -> dict[str, str]:
    params: dict[str, str] = {"follow": "true"}
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


def _unset() -> Any:
    from sandbox0.apispec.types import UNSET

    return UNSET
