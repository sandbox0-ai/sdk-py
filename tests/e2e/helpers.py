from __future__ import annotations

import os
import threading
import time
from dataclasses import dataclass
from typing import Optional

from sandbox0 import Client
from sandbox0.apispec.api.auth.post_auth_login import sync_detailed as auth_login
from sandbox0.apispec.client import Client as APIClient
from sandbox0.apispec.models.error_envelope import ErrorEnvelope
from sandbox0.apispec.models.login_request import LoginRequest
from sandbox0.apispec.models.success_login_response import SuccessLoginResponse
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.sandbox import Sandbox


@dataclass(frozen=True)
class E2EConfig:
    base_url: str
    email: str
    password: str
    template: str


_CONFIG: Optional[E2EConfig] = None
_TOKEN: Optional[str] = None


def load_e2e_config() -> Optional[E2EConfig]:
    global _CONFIG
    if _CONFIG is not None:
        return _CONFIG
    base_url = (os.getenv("S0_E2E_BASE_URL") or "").strip()
    password = (os.getenv("S0_E2E_PASSWORD") or "").strip()
    if not base_url or not password:
        return None
    email = (os.getenv("S0_E2E_EMAIL") or "").strip() or "admin@example.com"
    template = (os.getenv("S0_E2E_TEMPLATE") or "").strip() or "default"
    _CONFIG = E2EConfig(
        base_url=base_url,
        email=email,
        password=password,
        template=template,
    )
    return _CONFIG


def require_config(testcase) -> E2EConfig:
    cfg = load_e2e_config()
    if cfg is None:
        testcase.skipTest("S0_E2E_BASE_URL or S0_E2E_PASSWORD not set")
    return cfg


def login_with_retry(cfg: E2EConfig, timeout_sec: int = 180) -> str:
    api_client = APIClient(base_url=cfg.base_url)
    deadline = time.monotonic() + timeout_sec
    last_error: Optional[Exception] = None
    while time.monotonic() < deadline:
        try:
            token = login_once(api_client, cfg)
            if token:
                return token
        except Exception as exc:
            last_error = exc
        time.sleep(5)
    if last_error is None:
        raise RuntimeError("login timed out without error")
    raise last_error


def login_once(api_client: APIClient, cfg: E2EConfig) -> str:
    resp = auth_login(
        client=api_client,
        body=LoginRequest(email=cfg.email, password=cfg.password),
    )
    parsed = resp.parsed
    if isinstance(parsed, SuccessLoginResponse):
        data = parsed.data
        if data.__class__.__name__ != "Unset" and data.access_token:
            return data.access_token
        raise RuntimeError("login response missing access token")
    if isinstance(parsed, ErrorEnvelope):
        raise RuntimeError(f"login failed: {parsed.error.message}")
    raise RuntimeError(f"unexpected login response: status={resp.status_code}")


def e2e_token(cfg: E2EConfig) -> str:
    global _TOKEN
    if _TOKEN:
        return _TOKEN
    _TOKEN = login_with_retry(cfg)
    return _TOKEN


def new_client(cfg: E2EConfig, token: Optional[str] = None, **kwargs) -> Client:
    return Client(token=token or e2e_token(cfg), base_url=cfg.base_url, **kwargs)


def claim_sandbox(testcase, client: Client, cfg: E2EConfig, config: Optional[SandboxConfig] = None) -> Sandbox:
    sandbox = client.sandboxes.claim(cfg.template, config=config)

    def _cleanup() -> None:
        try:
            client.sandboxes.delete(sandbox.id)
        except Exception:
            pass

    testcase.addCleanup(_cleanup)
    return sandbox


def wait_for_watch_event(stream, timeout_sec: int = 10):
    result = {"event": None, "error": None}

    def _worker() -> None:
        try:
            for event in stream.iter_events():
                result["event"] = event
                return
        except Exception as exc:
            result["error"] = exc

    thread = threading.Thread(target=_worker, daemon=True)
    thread.start()
    thread.join(timeout_sec)
    if thread.is_alive():
        try:
            stream.close()
        except Exception:
            pass
        thread.join(1)
        return None
    if result["error"] is not None:
        raise result["error"]
    return result["event"]
