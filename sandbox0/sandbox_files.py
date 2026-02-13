from __future__ import annotations

import base64
import json
from io import BytesIO
from typing import TYPE_CHECKING, Any

from sandbox0.apispec.api.files import delete_api_v1_sandboxes_id_files
from sandbox0.apispec.api.files import get_api_v1_sandboxes_id_files
from sandbox0.apispec.api.files import get_api_v1_sandboxes_id_files_list
from sandbox0.apispec.api.files import get_api_v1_sandboxes_id_files_stat
from sandbox0.apispec.api.files import post_api_v1_sandboxes_id_files
from sandbox0.apispec.api.files import post_api_v1_sandboxes_id_files_move
from sandbox0.apispec.models.file_content_response import FileContentResponse
from sandbox0.apispec.models.file_content_response_encoding import FileContentResponseEncoding
from sandbox0.apispec.models.file_info import FileInfo
from sandbox0.apispec.models.move_file_request import MoveFileRequest
from sandbox0.apispec.models.success_created_response import SuccessCreatedResponse
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_file_list_response import SuccessFileListResponse
from sandbox0.apispec.models.success_file_read_response import SuccessFileReadResponse
from sandbox0.apispec.models.success_file_stat_response import SuccessFileStatResponse
from sandbox0.apispec.models.success_moved_response import SuccessMovedResponse
from sandbox0.apispec.models.success_written_response import SuccessWrittenResponse
from sandbox0.apispec.types import File as APIFile
from sandbox0.apispec.types import UNSET
from sandbox0.errors import APIError
from sandbox0.models import FileWatchResponse
from sandbox0.response import ensure_data, ensure_model

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox
    from websockets.sync.client import ClientConnection


class FileWatchStream:
    def __init__(self, conn: "ClientConnection", watch_id: str) -> None:
        self._conn = conn
        self.watch_id = watch_id

    def iter_events(self) -> Any:
        while True:
            raw = self._conn.recv()
            if raw is None:
                return
            if isinstance(raw, bytes):
                raw = raw.decode("utf-8", errors="replace")
            payload = json.loads(raw)
            yield FileWatchResponse(
                type=str(payload.get("type", "")),
                watch_id=str(payload.get("watch_id", "")),
                event=str(payload.get("event", "")),
                path=str(payload.get("path", "")),
                error=str(payload.get("error", "")),
            )

    def unsubscribe(self) -> None:
        self._conn.send(json.dumps({"action": "unsubscribe", "watch_id": self.watch_id}))
        self._conn.close()

    def close(self) -> None:
        self._conn.close()


class SandboxFilesMixin:
    id: str
    _client: any

    def read_file(self: "Sandbox", path: str) -> bytes:
        resp = get_api_v1_sandboxes_id_files.sync_detailed(id=self.id, client=self._client.api, path=path)

        content_type = str(resp.headers.get("Content-Type", "")).lower()
        if "application/json" in content_type:
            envelope = ensure_model(resp, SuccessFileReadResponse)
            data = envelope.data
            if data.__class__.__name__ == "Unset":
                raise APIError(status_code=int(resp.status_code), message="unexpected empty file response")
            if isinstance(data, FileContentResponse):
                if data.encoding.__class__.__name__ != "Unset" and data.encoding != FileContentResponseEncoding.BASE64:
                    raise APIError(status_code=int(resp.status_code), message=f"unsupported file encoding: {data.encoding}")
                content = "" if data.content.__class__.__name__ == "Unset" else data.content
                return base64.b64decode(content)
        if resp.parsed is None:
            raise APIError(status_code=int(resp.status_code), message="unexpected empty file response")
        return resp.content

    def stat_file(self: "Sandbox", path: str) -> FileInfo:
        resp = get_api_v1_sandboxes_id_files_stat.sync_detailed(id=self.id, client=self._client.api, path=path)
        return ensure_data(resp, SuccessFileStatResponse)

    def list_files(self: "Sandbox", path: str) -> list[FileInfo]:
        resp = get_api_v1_sandboxes_id_files_list.sync_detailed(id=self.id, client=self._client.api, path=path)
        data = ensure_data(resp, SuccessFileListResponse)
        entries = data.entries
        if entries.__class__.__name__ == "Unset":
            return []
        return entries

    def write_file(self: "Sandbox", path: str, data: bytes) -> SuccessWrittenResponse:
        resp = post_api_v1_sandboxes_id_files.sync_detailed(
            id=self.id,
            client=self._client.api,
            path=path,
            body=APIFile(payload=BytesIO(data)),
        )
        parsed = resp.parsed
        if isinstance(parsed, SuccessWrittenResponse):
            return parsed
        if isinstance(parsed, SuccessCreatedResponse):
            raise APIError(status_code=int(resp.status_code), message="directory created instead of file")
        raise APIError(status_code=int(resp.status_code), message="unexpected response")

    def mkdir(self: "Sandbox", path: str, recursive: bool = False) -> SuccessCreatedResponse:
        resp = post_api_v1_sandboxes_id_files.sync_detailed(
            id=self.id,
            client=self._client.api,
            path=path,
            mkdir=True,
            recursive=recursive if recursive else UNSET,
            body=APIFile(payload=BytesIO(b"")),
        )
        return ensure_model(resp, SuccessCreatedResponse)

    def delete_file(self: "Sandbox", path: str) -> SuccessDeletedResponse:
        resp = delete_api_v1_sandboxes_id_files.sync_detailed(id=self.id, client=self._client.api, path=path)
        return ensure_model(resp, SuccessDeletedResponse)

    def move_file(self: "Sandbox", source: str, destination: str) -> SuccessMovedResponse:
        resp = post_api_v1_sandboxes_id_files_move.sync_detailed(
            id=self.id,
            client=self._client.api,
            body=MoveFileRequest(source=source, destination=destination),
        )
        return ensure_model(resp, SuccessMovedResponse)

    def watch_files(self: "Sandbox", path: str, recursive: bool = False) -> FileWatchStream:
        from websockets.sync.client import connect

        ws_url = self._client.websocket_url(f"/api/v1/sandboxes/{self.id}/files/watch")
        conn = connect(ws_url, additional_headers=self._client.ws_headers())
        conn.send(json.dumps({"action": "subscribe", "path": path, "recursive": recursive}))
        raw = conn.recv()
        if raw is None:
            conn.close()
            raise APIError(status_code=0, message="watch subscribe failed: empty response")
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8", errors="replace")
        payload = json.loads(raw)
        if payload.get("type") == "error":
            conn.close()
            raise APIError(status_code=0, message=f"watch subscribe failed: {payload.get('error', '')}")
        if payload.get("type") != "subscribed" or not payload.get("watch_id"):
            conn.close()
            raise APIError(status_code=0, message=f"unexpected watch response: {payload.get('type', '')}")
        return FileWatchStream(conn=conn, watch_id=str(payload["watch_id"]))
