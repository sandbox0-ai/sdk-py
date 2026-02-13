from __future__ import annotations

import os

from sandbox0 import Client


def create_client() -> Client:
    token = required_env("SANDBOX0_TOKEN")
    base_url = os.getenv("SANDBOX0_BASE_URL", "https://api.sandbox0.ai")
    return Client(token=token, base_url=base_url)


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} is required")
    return value
