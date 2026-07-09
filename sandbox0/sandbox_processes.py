from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Iterator, Optional

import httpx

from sandbox0.apispec.api.processes import (
    delete_api_v1_sandboxes_id_processes_process_id,
    get_api_v1_sandboxes_id_processes,
    get_api_v1_sandboxes_id_processes_process_id,
    post_api_v1_sandboxes_id_processes,
    post_api_v1_sandboxes_id_processes_process_id_events,
    post_api_v1_sandboxes_id_processes_process_id_signal,
    put_api_v1_sandboxes_id_processes_process_id_channels_channel_pty_size,
)
from sandbox0.apispec.models.process_event import ProcessEvent
from sandbox0.apispec.models.process_event_type import ProcessEventType
from sandbox0.apispec.models.process_input_event import ProcessInputEvent
from sandbox0.apispec.models.process_input_event_payload import ProcessInputEventPayload
from sandbox0.apispec.models.process_session import ProcessSession
from sandbox0.apispec.models.process_spec import ProcessSpec
from sandbox0.apispec.models.resize_context_request import ResizeContextRequest
from sandbox0.apispec.models.signal_context_request import SignalContextRequest
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_process_event_response import SuccessProcessEventResponse
from sandbox0.apispec.models.success_process_session_list_response import (
    SuccessProcessSessionListResponse,
)
from sandbox0.apispec.models.success_process_session_response import (
    SuccessProcessSessionResponse,
)
from sandbox0.apispec.models.success_resized_response import SuccessResizedResponse
from sandbox0.apispec.models.success_signaled_response import SuccessSignaledResponse
from sandbox0.errors import APIError
from sandbox0.response import ensure_data, ensure_model
from sandbox0.response_normalize import SKIP_RESPONSE_NORMALIZE_EXTENSION
from sandbox0.sandbox_observability import _api_error_from_response


@dataclass(frozen=True)
class ProcessEventWatchOptions:
    cursor: Optional[int] = None


class ProcessEventStream:
    def __init__(self, response: httpx.Response) -> None:
        self._response = response

    @property
    def response(self) -> httpx.Response:
        return self._response

    def iter_bytes(self) -> Iterator[bytes]:
        return self._response.iter_bytes()

    def iter_text(self) -> Iterator[str]:
        return self._response.iter_text()

    def iter_events(self) -> Iterator[ProcessEvent]:
        data_lines: list[str] = []
        for raw_line in self._response.iter_lines():
            line = raw_line.rstrip("\r")
            if not line:
                if data_lines:
                    yield ProcessEvent.from_dict(json.loads("\n".join(data_lines)))
                    data_lines = []
                continue
            if line.startswith("data:"):
                data_lines.append(line[5:].lstrip())
        if data_lines:
            yield ProcessEvent.from_dict(json.loads("\n".join(data_lines)))

    def close(self) -> None:
        self._response.close()

    def __enter__(self) -> "ProcessEventStream":
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()


class SandboxProcessesMixin:
    id: str
    _client: Any

    def create_process(self, spec: ProcessSpec) -> ProcessSession:
        resp = post_api_v1_sandboxes_id_processes.sync_detailed(
            id=self.id,
            client=self._client.api,
            body=spec,
        )
        data = ensure_data(resp, SuccessProcessSessionResponse)
        process = data.process
        if process.__class__.__name__ == "Unset":
            raise APIError(status_code=0, message="create process returned empty process")
        return process

    def list_processes(self) -> list[ProcessSession]:
        resp = get_api_v1_sandboxes_id_processes.sync_detailed(
            id=self.id,
            client=self._client.api,
        )
        data = ensure_data(resp, SuccessProcessSessionListResponse)
        if data.processes.__class__.__name__ == "Unset":
            return []
        return list(data.processes)

    def get_process(self, process_id: str) -> ProcessSession:
        resp = get_api_v1_sandboxes_id_processes_process_id.sync_detailed(
            id=self.id,
            process_id=process_id,
            client=self._client.api,
        )
        data = ensure_data(resp, SuccessProcessSessionResponse)
        process = data.process
        if process.__class__.__name__ == "Unset":
            raise APIError(status_code=0, message="get process returned empty process")
        return process

    def delete_process(self, process_id: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandboxes_id_processes_process_id.sync_detailed(
            id=self.id,
            process_id=process_id,
            client=self._client.api,
        )
        return ensure_model(resp, SuccessDeletedResponse)

    def send_process_event(self, process_id: str, event: ProcessInputEvent) -> ProcessEvent:
        resp = post_api_v1_sandboxes_id_processes_process_id_events.sync_detailed(
            id=self.id,
            process_id=process_id,
            client=self._client.api,
            body=event,
        )
        data = ensure_data(resp, SuccessProcessEventResponse)
        accepted = data.event
        if accepted.__class__.__name__ == "Unset":
            raise APIError(status_code=0, message="send process event returned empty event")
        return accepted

    def send_process_input(
        self,
        process_id: str,
        channel: str,
        data: str,
        event_id: str,
    ) -> ProcessEvent:
        payload = ProcessInputEventPayload()
        payload["data"] = data
        event = ProcessInputEvent(
            event_id=event_id,
            channel=channel,
            type_=ProcessEventType.STDIN_WRITE,
            payload=payload,
        )
        return self.send_process_event(process_id, event)

    def watch_process_events(
        self,
        process_id: str,
        options: Optional[ProcessEventWatchOptions] = None,
    ) -> ProcessEventStream:
        params: dict[str, str] = {}
        if options is not None and options.cursor is not None:
            params["cursor"] = str(options.cursor)
        http_client = self._client.api.get_httpx_client()
        request = http_client.build_request(
            "GET",
            f"/api/v1/sandboxes/{self.id}/processes/{process_id}/events",
            params=params,
            headers={"Accept": "text/event-stream"},
        )
        request.extensions[SKIP_RESPONSE_NORMALIZE_EXTENSION] = True
        response = http_client.send(request, stream=True)
        if response.status_code < 200 or response.status_code >= 300:
            content = response.read()
            response.close()
            raise _api_error_from_response(response, content)
        content_type = response.headers.get("Content-Type", "")
        if content_type and not content_type.lower().startswith("text/event-stream"):
            response.close()
            raise APIError(
                status_code=response.status_code,
                code="unexpected_response",
                message=f"unexpected process event stream content type: {content_type}",
            )
        return ProcessEventStream(response)

    def signal_process(self, process_id: str, signal: str) -> SuccessSignaledResponse:
        resp = post_api_v1_sandboxes_id_processes_process_id_signal.sync_detailed(
            id=self.id,
            process_id=process_id,
            client=self._client.api,
            body=SignalContextRequest(signal=signal),
        )
        return ensure_model(resp, SuccessSignaledResponse)

    def resize_process_pty(
        self,
        process_id: str,
        channel: str,
        rows: int,
        cols: int,
    ) -> SuccessResizedResponse:
        if rows <= 0 or cols <= 0:
            raise APIError(status_code=0, code="invalid_argument", message="rows and cols must be > 0")
        resp = put_api_v1_sandboxes_id_processes_process_id_channels_channel_pty_size.sync_detailed(
            id=self.id,
            process_id=process_id,
            channel=channel,
            client=self._client.api,
            body=ResizeContextRequest(rows=rows, cols=cols),
        )
        return ensure_model(resp, SuccessResizedResponse)


def process_stdio_spec(command: list[str]) -> ProcessSpec:
    from sandbox0.apispec.models.process_channel_framing import ProcessChannelFraming
    from sandbox0.apispec.models.process_channel_kind import ProcessChannelKind
    from sandbox0.apispec.models.process_channel_spec import ProcessChannelSpec

    return ProcessSpec(
        command=command,
        channels=[
            ProcessChannelSpec(
                name="stdio",
                kind=ProcessChannelKind.STDIO,
                framing=ProcessChannelFraming.LINE,
                stdin=True,
                stdout=True,
                stderr=True,
            )
        ],
    )
