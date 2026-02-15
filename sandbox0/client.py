from __future__ import annotations

from typing import Dict, Optional
from urllib.parse import urlparse, urlunparse

import httpx

from sandbox0.apispec.client import AuthenticatedClient
from sandbox0.resources import Sandboxes, Volumes
from sandbox0.response_normalize import normalize_response_hook, normalize_response_hook_async
from sandbox0.sandbox import Sandbox

DEFAULT_BASE_URL = "https://api.sandbox0.ai"


class Client:
    def __init__(
        self,
        *,
        token: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: Optional[float] = None,
        user_agent: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        verify_ssl: bool = True,
        raise_on_unexpected_status: bool = False,
    ) -> None:
        merged_headers: Dict[str, str] = {}
        if headers:
            merged_headers.update(headers)
        if user_agent:
            merged_headers["User-Agent"] = user_agent

        httpx_timeout = httpx.Timeout(timeout) if timeout is not None else None
        self._api = AuthenticatedClient(
            base_url=base_url,
            token=token,
            headers=merged_headers,
            timeout=httpx_timeout,
            verify_ssl=verify_ssl,
            raise_on_unexpected_status=raise_on_unexpected_status,
        )
        auth_value = f"{self._api.prefix} {self._api.token}" if self._api.prefix else self._api.token
        request_headers = dict(self._api._headers)
        request_headers[self._api.auth_header_name] = auth_value
        self._api.set_httpx_client(
            httpx.Client(
                base_url=base_url,
                headers=request_headers,
                cookies=self._api._cookies,
                timeout=httpx_timeout,
                verify=verify_ssl,
                follow_redirects=self._api._follow_redirects,
                event_hooks={"response": [normalize_response_hook]},
            )
        )
        self._api.set_async_httpx_client(
            httpx.AsyncClient(
                base_url=base_url,
                headers=request_headers,
                cookies=self._api._cookies,
                timeout=httpx_timeout,
                verify=verify_ssl,
                follow_redirects=self._api._follow_redirects,
                event_hooks={"response": [normalize_response_hook_async]},
            )
        )
        self.base_url = base_url
        self.sandboxes = Sandboxes(self)
        self.volumes = Volumes(self)

    @property
    def api(self) -> AuthenticatedClient:
        return self._api

    def sandbox(self, sandbox_id: str) -> Sandbox:
        return Sandbox(id=sandbox_id, client=self)

    def websocket_url(self, path: str) -> str:
        parsed = urlparse(self.base_url)
        scheme = parsed.scheme.lower()
        if scheme == "https":
            ws_scheme = "wss"
        elif scheme == "http":
            ws_scheme = "ws"
        elif scheme in ("ws", "wss"):
            ws_scheme = scheme
        else:
            raise ValueError(f"unsupported URL scheme: {parsed.scheme}")
        normalized_path = path if path.startswith("/") else "/" + path
        return urlunparse((ws_scheme, parsed.netloc, normalized_path, "", "", ""))

    def ws_headers(self) -> dict[str, str]:
        # Reuse generated client's auth/header behavior for WebSocket upgrade requests.
        http_client = self._api.get_httpx_client()
        return dict(http_client.headers)

    def close(self) -> None:
        """Close the underlying HTTP clients and release resources."""
        self._api.__exit__(None, None, None)

    def __enter__(self) -> "Client":
        self._api.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
