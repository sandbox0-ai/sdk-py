from __future__ import annotations

import json
from typing import Any, Optional, Type, TypeVar

from sandbox0.apispec.models.error_envelope import ErrorEnvelope
from sandbox0.apispec.types import Response

from sandbox0.errors import APIError

T = TypeVar("T")


def ensure_model(response: Response[Any], model_type: Type[T]) -> T:
    parsed = response.parsed
    if isinstance(parsed, ErrorEnvelope):
        raise _to_api_error(response, parsed)
    if isinstance(parsed, model_type):
        return parsed
    raise _unexpected_response(response)


def ensure_data(response: Response[Any], envelope_type: Type[Any]) -> Any:
    parsed = response.parsed
    if isinstance(parsed, ErrorEnvelope):
        raise _to_api_error(response, parsed)
    if isinstance(parsed, envelope_type):
        data = getattr(parsed, "data", None)
        if _is_unset(data) or data is None:
            raise _unexpected_response(response)
        return data
    raise _unexpected_response(response)


def optional_data(response: Response[Any], envelope_type: Type[Any]) -> Any:
    parsed = response.parsed
    if isinstance(parsed, ErrorEnvelope):
        raise _to_api_error(response, parsed)
    if isinstance(parsed, envelope_type):
        return getattr(parsed, "data", None)
    raise _unexpected_response(response)


def _is_unset(value: Any) -> bool:
    return value is None or value.__class__.__name__ == "Unset"


def _to_api_error(response: Response[Any], envelope: ErrorEnvelope) -> APIError:
    return APIError(
        status_code=int(response.status_code),
        code=envelope.error.code,
        message=envelope.error.message,
        details=envelope.error.details,
        request_id=_request_id_from_headers(response.headers),
        body=response.content,
    )


def _unexpected_response(response: Response[Any]) -> APIError:
    body = response.content or b""
    message = "Unexpected API response"
    if body:
        try:
            payload = json.loads(body.decode("utf-8"))
            message = f"{message}: {json.dumps(payload, separators=(',', ':'), ensure_ascii=True)}"
        except Exception:
            message = f"{message}: {body.decode('utf-8', errors='replace').strip()}"
    return APIError(
        status_code=int(response.status_code),
        message=message,
        request_id=_request_id_from_headers(response.headers),
        body=response.content,
    )


def _request_id_from_headers(headers: dict[str, str]) -> Optional[str]:
    for key in ("X-Request-Id", "X-Request-ID", "Request-Id", "Request-ID"):
        value = headers.get(key)
        if value:
            stripped = value.strip()
            if stripped:
                return stripped
    return None
