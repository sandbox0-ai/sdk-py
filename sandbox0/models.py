from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class RunResult:
    sandbox_id: str
    context_id: str
    output: str


@dataclass(frozen=True)
class CmdResult:
    sandbox_id: str
    context_id: str
    output: str


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
class ExposedPort:
    port: int
    resume: bool
    public_url: str = ""


@dataclass(frozen=True)
class ExposedPortsResponse:
    ports: list[ExposedPort]
    exposure_domain: str = ""


@dataclass(frozen=True)
class FileWatchResponse:
    type: str
    watch_id: str = ""
    event: str = ""
    path: str = ""
    error: str = ""
