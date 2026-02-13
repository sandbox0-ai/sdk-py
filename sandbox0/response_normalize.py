from __future__ import annotations

import json
from typing import Any

import httpx

_NULL_MAP_KEYS = {
    "annotations",
    "envVars",
    "env_vars",
    "labels",
    "matchLabels",
    "nodeSelector",
}

_NULL_ARRAY_KEYS = {
    "allowedCidrs",
    "allowedDomains",
    "allowedPorts",
    "allowedTeams",
    "api_keys",
    "args",
    "candidates",
    "command",
    "conditions",
    "contexts",
    "data",
    "deniedCidrs",
    "deniedDomains",
    "deniedPorts",
    "drop",
    "entries",
    "env",
    "exposed_ports",
    "identities",
    "matchExpressions",
    "matchFields",
    "members",
    "mounts",
    "namespaces",
    "nodeSelectorTerms",
    "preferredDuringSchedulingIgnoredDuringExecution",
    "providers",
    "requiredDuringSchedulingIgnoredDuringExecution",
    "roles",
    "sidecars",
    "tags",
    "teams",
    "templates",
    "tolerations",
    "values",
}


def _normalize_null_string_map(value: dict[str, Any]) -> bool:
    changed = False
    for key, raw in value.items():
        if raw is None:
            value[key] = ""
            changed = True
    return changed


def _normalize_null_maps(payload: Any) -> tuple[Any, bool]:
    if isinstance(payload, dict):
        changed = False
        normalized: dict[str, Any] = {}
        for key, raw in payload.items():
            if raw is None and key in _NULL_MAP_KEYS:
                normalized[key] = {}
                changed = True
                continue
            if raw is None and key in _NULL_ARRAY_KEYS:
                normalized[key] = []
                changed = True
                continue
            if key in _NULL_MAP_KEYS and isinstance(raw, dict):
                changed = _normalize_null_string_map(raw) or changed
            next_value, nested_changed = _normalize_null_maps(raw)
            normalized[key] = next_value
            changed = nested_changed or changed
        return normalized, changed

    if isinstance(payload, list):
        changed = False
        normalized_list: list[Any] = []
        for item in payload:
            next_value, nested_changed = _normalize_null_maps(item)
            normalized_list.append(next_value)
            changed = nested_changed or changed
        return normalized_list, changed

    return payload, False


def normalize_response_json(response: httpx.Response) -> None:
    content_type = response.headers.get("content-type", "").lower()
    if "application/json" not in content_type:
        return

    body = response.content
    if not body:
        return

    try:
        payload = json.loads(body)
    except ValueError:
        return

    normalized, changed = _normalize_null_maps(payload)
    if not changed:
        return

    response._content = json.dumps(normalized, separators=(",", ":")).encode("utf-8")
    response.headers["content-length"] = str(len(response.content))


def normalize_response_hook(response: httpx.Response) -> None:
    response.read()
    normalize_response_json(response)


async def normalize_response_hook_async(response: httpx.Response) -> None:
    await response.aread()
    normalize_response_json(response)
