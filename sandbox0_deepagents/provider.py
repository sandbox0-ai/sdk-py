from __future__ import annotations

import os
from typing import Any, Dict, Optional

from deepagents_code.integrations.sandbox_provider import (
    SandboxInstallHint,
    SandboxNotFoundError,
    SandboxProvider,
    SandboxProviderMetadata,
)

from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.types import Unset
from sandbox0.client import DEFAULT_BASE_URL, Client as Sandbox0Client
from sandbox0.errors import APIError
from sandbox0.sandbox import Sandbox
from sandbox0_deepagents.backend import (
    DEFAULT_COMMAND_TIMEOUT_SEC,
    DEFAULT_WORKING_DIR,
    Sandbox0DeepAgentsSandbox,
)

DEFAULT_TEMPLATE = "default"
DEFAULT_SANDBOX_TTL_SEC = 60 * 60
DEFAULT_SANDBOX_HARD_TTL_SEC = 30 * 24 * 60 * 60


class Sandbox0Provider(SandboxProvider):
    """Deep Agents Code provider for Sandbox0 sandboxes."""

    metadata = SandboxProviderMetadata(
        name="sandbox0",
        working_dir=DEFAULT_WORKING_DIR,
        install=SandboxInstallHint(kind="package", name="sandbox0[deepagents]"),
        supports_sandbox_id=True,
        supports_snapshot_name=False,
    )

    def __init__(
        self,
        *,
        token: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        client: Optional[Sandbox0Client] = None,
        timeout: Optional[float] = None,
        user_agent: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        verify_ssl: bool = True,
    ) -> None:
        self._client = client
        self._token = token
        self._api_key = api_key
        self._base_url = base_url
        self._timeout = timeout
        self._user_agent = user_agent
        self._headers = headers
        self._verify_ssl = verify_ssl

    def get_or_create(
        self,
        *,
        sandbox_id: Optional[str] = None,
        **kwargs: Any,
    ) -> Sandbox0DeepAgentsSandbox:
        """Get an existing Sandbox0 sandbox, or claim a default-template sandbox."""
        client = self._resolve_client(**_client_kwargs(kwargs))
        working_dir = str(kwargs.pop("working_dir", DEFAULT_WORKING_DIR))
        default_timeout = int(kwargs.pop("default_timeout", DEFAULT_COMMAND_TIMEOUT_SEC))
        template = str(kwargs.pop("template", DEFAULT_TEMPLATE))
        sandbox_ttl_sec = kwargs.pop("sandbox_ttl_sec", None)
        sandbox_hard_ttl_sec = kwargs.pop("sandbox_hard_ttl_sec", None)
        sandbox_config = kwargs.pop("sandbox_config", None)
        if kwargs:
            msg = f"Received unsupported arguments: {sorted(kwargs)}"
            raise TypeError(msg)

        if sandbox_id:
            sandbox = self._reattach(client, sandbox_id)
        else:
            sandbox = client.sandboxes.claim(
                template,
                config=_build_sandbox_config(
                    sandbox_config=sandbox_config,
                    sandbox_ttl_sec=sandbox_ttl_sec,
                    sandbox_hard_ttl_sec=sandbox_hard_ttl_sec,
                ),
            )

        return Sandbox0DeepAgentsSandbox(
            sandbox=sandbox,
            working_dir=working_dir,
            default_timeout=default_timeout,
        )

    def delete(self, *, sandbox_id: str, **kwargs: Any) -> None:
        """Delete a Sandbox0 sandbox by ID."""
        client = self._resolve_client(**_client_kwargs(kwargs))
        if kwargs:
            msg = f"Received unsupported arguments: {sorted(kwargs)}"
            raise TypeError(msg)
        client.sandboxes.delete(sandbox_id)

    def _resolve_client(
        self,
        *,
        token: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
        user_agent: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        verify_ssl: Optional[bool] = None,
    ) -> Sandbox0Client:
        if self._client is not None:
            return self._client

        resolved_token = (
            token
            or api_key
            or self._token
            or self._api_key
            or os.environ.get("SANDBOX0_TOKEN")
            or os.environ.get("SANDBOX0_API_KEY")
        )
        if not resolved_token:
            raise ValueError(
                "Sandbox0Provider requires token/api_key, SANDBOX0_TOKEN, or SANDBOX0_API_KEY"
            )

        self._client = Sandbox0Client(
            token=resolved_token,
            base_url=base_url or self._base_url or os.environ.get("SANDBOX0_BASE_URL") or DEFAULT_BASE_URL,
            timeout=timeout if timeout is not None else self._timeout,
            user_agent=user_agent if user_agent is not None else self._user_agent,
            headers=headers if headers is not None else self._headers,
            verify_ssl=self._verify_ssl if verify_ssl is None else verify_ssl,
        )
        return self._client

    @staticmethod
    def _reattach(client: Sandbox0Client, sandbox_id: str) -> Sandbox:
        try:
            data = client.sandboxes.get(sandbox_id)
        except APIError as exc:
            if exc.status_code == 404:
                raise SandboxNotFoundError(sandbox_id) from exc
            raise
        template = str(getattr(data, "template_id", "") or DEFAULT_TEMPLATE)
        status = str(getattr(data, "status", "") or "")
        pod_name = str(getattr(data, "pod_name", "") or "")
        return Sandbox(
            id=sandbox_id,
            client=client,
            template=template,
            pod_name=pod_name,
            status=status,
        )


def _client_kwargs(kwargs: dict[str, Any]) -> dict[str, Any]:
    client_keys = {
        "token",
        "api_key",
        "base_url",
        "timeout",
        "user_agent",
        "headers",
        "verify_ssl",
    }
    extracted: dict[str, Any] = {}
    for key in list(kwargs):
        if key in client_keys:
            extracted[key] = kwargs.pop(key)
    return extracted


def _build_sandbox_config(
    *,
    sandbox_config: Any,
    sandbox_ttl_sec: Any,
    sandbox_hard_ttl_sec: Any,
) -> SandboxConfig:
    if sandbox_config is not None and not isinstance(sandbox_config, SandboxConfig):
        raise TypeError("sandbox_config must be a SandboxConfig instance")
    config = sandbox_config or SandboxConfig()
    if sandbox_ttl_sec is not None or isinstance(config.ttl, Unset):
        config.ttl = int(
            DEFAULT_SANDBOX_TTL_SEC if sandbox_ttl_sec is None else sandbox_ttl_sec
        )
    if sandbox_hard_ttl_sec is not None or isinstance(config.hard_ttl, Unset):
        config.hard_ttl = int(
            DEFAULT_SANDBOX_HARD_TTL_SEC
            if sandbox_hard_ttl_sec is None
            else sandbox_hard_ttl_sec
        )
    return config
