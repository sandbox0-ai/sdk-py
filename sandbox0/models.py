from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from sandbox0.apispec.models.public_gateway_config import PublicGatewayConfig


@dataclass(frozen=True)
class RunResult:
    sandbox_id: str
    context_id: str
    output_raw: str


@dataclass(frozen=True)
class CmdResult:
    sandbox_id: str
    context_id: str
    output_raw: str


@dataclass(frozen=True)
class StreamInput:
    type: str = "input"
    data: str = ""
    rows: int = 0
    cols: int = 0
    signal: str = ""
    request_id: str = ""


@dataclass(frozen=True)
class StreamOutput:
    sandbox_id: str
    context_id: str
    source: str
    data: str


@dataclass(frozen=True)
class StreamDone:
    sandbox_id: str
    context_id: str
    request_id: Optional[str] = None
    exit_code: Optional[int] = None
    state: Optional[str] = None


@dataclass(frozen=True)
class PublicGatewayResponse:
    sandbox_id: str
    public_gateway: "PublicGatewayConfig"
    exposure_domain: str = ""


@dataclass(frozen=True)
class FileWatchResponse:
    type: str
    watch_id: str = ""
    event: str = ""
    path: str = ""
    error: str = ""


@dataclass(frozen=True)
class SandboxLogs:
    sandbox_id: str
    pod_name: str
    container: str
    previous: bool
    logs: str
