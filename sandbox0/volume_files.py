from __future__ import annotations

import base64
import json
from io import BytesIO
from typing import Any, cast

from sandbox0.apispec.api.files import delete_api_v1_sandboxvolumes_id_files
from sandbox0.apispec.api.files import get_api_v1_sandboxvolumes_id_files
from sandbox0.apispec.api.files import get_api_v1_sandboxvolumes_id_files_list
from sandbox0.apispec.api.files import get_api_v1_sandboxvolumes_id_files_stat
from sandbox0.apispec.api.files import post_api_v1_sandboxvolumes_id_files
from sandbox0.apispec.api.files import post_api_v1_sandboxvolumes_id_files_move
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
from sandbox0.sandbox_files import FileWatchStream
from sandbox0.response import ensure_data, ensure_model


def read_volume_file(client: Any, volume_id: str, path: str) -> bytes:
    resp = get_api_v1_sandboxvolumes_id_files.sync_detailed(id=volume_id, client=client.api, path=path)

    content_type = str(resp.headers.get("Content-Type", "")).lower()
    if "application/json" in content_type:
        envelope = ensure_model(resp, SuccessFileReadResponse)
        data = envelope.data
        if data.__class__.__name__ == "Unset":
            raise APIError(status_code=int(resp.status_code), message="unexpected empty volume file response")
        if isinstance(data, FileContentResponse):
            if data.encoding.__class__.__name__ != "Unset" and data.encoding != FileContentResponseEncoding.BASE64:
                raise APIError(status_code=int(resp.status_code), message=f"unsupported file encoding: {data.encoding}")
            content = "" if data.content.__class__.__name__ == "Unset" else data.content
            return base64.b64decode(cast(str, content))
    if resp.parsed is None:
        raise APIError(status_code=int(resp.status_code), message="unexpected empty volume file response")
    return resp.content


def stat_volume_file(client: Any, volume_id: str, path: str) -> FileInfo:
    resp = get_api_v1_sandboxvolumes_id_files_stat.sync_detailed(id=volume_id, client=client.api, path=path)
    return ensure_data(resp, SuccessFileStatResponse)


def list_volume_files(client: Any, volume_id: str, path: str) -> list[FileInfo]:
    resp = get_api_v1_sandboxvolumes_id_files_list.sync_detailed(id=volume_id, client=client.api, path=path)
    data = ensure_data(resp, SuccessFileListResponse)
    entries = data.entries
    if entries.__class__.__name__ == "Unset":
        return []
    return entries


def write_volume_file(client: Any, volume_id: str, path: str, data: bytes) -> SuccessWrittenResponse:
    resp = post_api_v1_sandboxvolumes_id_files.sync_detailed(
        id=volume_id,
        client=client.api,
        path=path,
        body=APIFile(payload=BytesIO(data)),
    )
    parsed = resp.parsed
    if isinstance(parsed, SuccessWrittenResponse):
        return parsed
    if isinstance(parsed, SuccessCreatedResponse):
        raise APIError(status_code=int(resp.status_code), message="directory created instead of file")
    raise APIError(status_code=int(resp.status_code), message="unexpected response")


def mkdir_volume_file(client: Any, volume_id: str, path: str, recursive: bool = False) -> SuccessCreatedResponse:
    resp = post_api_v1_sandboxvolumes_id_files.sync_detailed(
        id=volume_id,
        client=client.api,
        path=path,
        mkdir=True,
        recursive=recursive if recursive else UNSET,
        body=APIFile(payload=BytesIO(b"")),
    )
    return ensure_model(resp, SuccessCreatedResponse)


def delete_volume_file(client: Any, volume_id: str, path: str) -> SuccessDeletedResponse:
    resp = delete_api_v1_sandboxvolumes_id_files.sync_detailed(id=volume_id, client=client.api, path=path)
    return ensure_model(resp, SuccessDeletedResponse)


def move_volume_file(client: Any, volume_id: str, source: str, destination: str) -> SuccessMovedResponse:
    resp = post_api_v1_sandboxvolumes_id_files_move.sync_detailed(
        id=volume_id,
        client=client.api,
        body=MoveFileRequest(source=source, destination=destination),
    )
    return ensure_model(resp, SuccessMovedResponse)


def watch_volume_files(client: Any, volume_id: str, path: str, recursive: bool = False) -> FileWatchStream:
    from websockets.sync.client import connect

    ws_url = client.websocket_url(f"/api/v1/sandboxvolumes/{volume_id}/files/watch")
    conn = connect(ws_url, additional_headers=client.ws_headers())
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
