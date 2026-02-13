from __future__ import annotations

import json
import shlex
import threading
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, Optional

from sandbox0.apispec.models.create_cmd_context_request import CreateCMDContextRequest
from sandbox0.apispec.models.create_context_request import CreateContextRequest
from sandbox0.apispec.models.create_context_request_env_vars import CreateContextRequestEnvVars
from sandbox0.apispec.models.create_repl_context_request import CreateREPLContextRequest
from sandbox0.apispec.models.pty_size import PTYSize
from sandbox0.apispec.models.process_type import ProcessType
from sandbox0.apispec.types import UNSET
from sandbox0.errors import APIError
from sandbox0.models import CmdResult, RunResult, StreamInput, StreamOutput
from sandbox0.sandbox_contexts import SandboxContextsMixin
from sandbox0.sandbox_exposed_ports import SandboxExposedPortsMixin
from sandbox0.sandbox_files import SandboxFilesMixin
from sandbox0.sandbox_network import SandboxNetworkMixin
from sandbox0.sandbox_volumes import SandboxVolumesMixin

if TYPE_CHECKING:
    from websockets.sync.client import ClientConnection


@dataclass
class RunOptions:
    context_id: Optional[str] = None
    idle_timeout_sec: Optional[int] = None
    ttl_sec: Optional[int] = None
    cwd: Optional[str] = None
    env_vars: Optional[Dict[str, str]] = None
    pty_rows: Optional[int] = None
    pty_cols: Optional[int] = None


@dataclass
class CmdOptions:
    command: Optional[list[str]] = None
    wait: Optional[bool] = None
    idle_timeout_sec: Optional[int] = None
    ttl_sec: Optional[int] = None
    cwd: Optional[str] = None
    env_vars: Optional[Dict[str, str]] = None
    pty_rows: Optional[int] = None
    pty_cols: Optional[int] = None


class ContextStream:
    def __init__(self, conn: "ClientConnection", sandbox_id: str, context_id: str) -> None:
        self._conn = conn
        self._sandbox_id = sandbox_id
        self._context_id = context_id
        self._send_lock = threading.Lock()

    @property
    def context_id(self) -> str:
        return self._context_id

    def send(self, message: StreamInput) -> None:
        payload: dict[str, Any] = {"type": message.type}
        if message.data:
            payload["data"] = message.data
        if message.rows > 0:
            payload["rows"] = message.rows
        if message.cols > 0:
            payload["cols"] = message.cols
        if message.signal:
            payload["signal"] = message.signal
        if message.request_id:
            payload["request_id"] = message.request_id
        with self._send_lock:
            self._conn.send(json.dumps(payload))

    def send_input(self, data: str, request_id: Optional[str] = None) -> None:
        self.send(
            StreamInput(
                type="input",
                data=data,
                request_id=request_id or f"req-{time.time_ns()}",
            )
        )

    def send_resize(self, rows: int, cols: int) -> None:
        self.send(StreamInput(type="resize", rows=rows, cols=cols))

    def send_signal(self, signal: str) -> None:
        self.send(StreamInput(type="signal", signal=signal))

    def iter_outputs(self) -> Any:
        while True:
            raw = self._conn.recv()
            if raw is None:
                return
            if isinstance(raw, bytes):
                raw = raw.decode("utf-8", errors="replace")
            payload = json.loads(raw)
            yield StreamOutput(
                sandbox_id=self._sandbox_id,
                context_id=self._context_id,
                source=str(payload.get("source", "")),
                data=str(payload.get("data", "")),
            )

    def close(self) -> None:
        self._conn.close()


class Sandbox(
    SandboxContextsMixin,
    SandboxFilesMixin,
    SandboxNetworkMixin,
    SandboxVolumesMixin,
    SandboxExposedPortsMixin,
):
    def __init__(
        self,
        *,
        id: str,
        client: Any,
        template: str = "",
        cluster_id: Optional[str] = None,
        pod_name: str = "",
        status: str = "",
    ) -> None:
        self.id = id
        self.template = template
        self.cluster_id = cluster_id
        self.pod_name = pod_name
        self.status = status
        self._client = client
        self._repl_context_by_lang: dict[str, str] = {}
        self._lock = threading.Lock()

    def run(self, language: str, input: str, options: Optional[RunOptions] = None) -> RunResult:
        if not input.strip():
            raise ValueError("input cannot be empty")
        opts = options or RunOptions()
        context_id = self._ensure_repl_context(language=language, options=opts)
        exec_resp = self.context_exec(context_id=context_id, input=input)
        return RunResult(sandbox_id=self.id, context_id=context_id, output_raw=exec_resp.output_raw)

    def cmd(self, cmd: str, options: Optional[CmdOptions] = None) -> CmdResult:
        if not cmd.strip():
            raise ValueError("command cannot be empty")
        opts = options or CmdOptions()
        command = opts.command if opts.command is not None else shlex.split(cmd)
        if not command:
            raise ValueError("command cannot be empty")
        wait = True if opts.wait is None else opts.wait
        request = CreateContextRequest(
            type_=ProcessType.CMD,
            cmd=CreateCMDContextRequest(command=command),
            wait_until_done=wait,
            cwd=opts.cwd if opts.cwd is not None else UNSET,
            env_vars=self._build_env_vars(opts.env_vars),
            pty_size=self._build_pty(opts.pty_rows, opts.pty_cols),
            idle_timeout_sec=opts.idle_timeout_sec if opts.idle_timeout_sec is not None else UNSET,
            ttl_sec=opts.ttl_sec if opts.ttl_sec is not None else UNSET,
        )
        context_resp = self.create_context(request=request)
        output_raw = "" if context_resp.output_raw.__class__.__name__ == "Unset" else context_resp.output_raw
        return CmdResult(sandbox_id=self.id, context_id=context_resp.id, output_raw=output_raw)

    def run_stream(
        self,
        language: str,
        options: Optional[RunOptions] = None,
    ) -> ContextStream:
        opts = options or RunOptions()
        context_id = self._ensure_repl_context(language=language, options=opts)
        return self.connect_ws_context(context_id=context_id)

    def cmd_stream(self, cmd: str, options: Optional[CmdOptions] = None) -> ContextStream:
        if not cmd.strip():
            raise ValueError("command cannot be empty")
        opts = options or CmdOptions()
        command = opts.command if opts.command is not None else shlex.split(cmd)
        if not command:
            raise ValueError("command cannot be empty")
        wait = False if opts.wait is None else opts.wait
        request = CreateContextRequest(
            type_=ProcessType.CMD,
            cmd=CreateCMDContextRequest(command=command),
            wait_until_done=wait,
            cwd=opts.cwd if opts.cwd is not None else UNSET,
            env_vars=self._build_env_vars(opts.env_vars),
            pty_size=self._build_pty(opts.pty_rows, opts.pty_cols),
            idle_timeout_sec=opts.idle_timeout_sec if opts.idle_timeout_sec is not None else UNSET,
            ttl_sec=opts.ttl_sec if opts.ttl_sec is not None else UNSET,
        )
        context_resp = self.create_context(request=request)
        return self.connect_ws_context(context_id=context_resp.id)

    def connect_ws_context(self, context_id: str) -> ContextStream:
        from websockets.sync.client import connect

        ws_url = self._client.websocket_url(f"/api/v1/sandboxes/{self.id}/contexts/{context_id}/ws")
        conn = connect(ws_url, additional_headers=self._client.ws_headers())
        return ContextStream(conn=conn, sandbox_id=self.id, context_id=context_id)

    def _ensure_repl_context(self, language: str, options: RunOptions) -> str:
        if options.context_id:
            return options.context_id
        lang = language.strip() or "python"
        with self._lock:
            cached = self._repl_context_by_lang.get(lang)
        if cached:
            return cached
        request = CreateContextRequest(
            type_=ProcessType.REPL,
            repl=CreateREPLContextRequest(language=lang),
            cwd=options.cwd if options.cwd is not None else UNSET,
            env_vars=self._build_env_vars(options.env_vars),
            pty_size=self._build_pty(options.pty_rows, options.pty_cols),
            idle_timeout_sec=options.idle_timeout_sec if options.idle_timeout_sec is not None else UNSET,
            ttl_sec=options.ttl_sec if options.ttl_sec is not None else UNSET,
        )
        context_resp = self.create_context(request=request)
        context_id = context_resp.id
        with self._lock:
            self._repl_context_by_lang[lang] = context_id
        return context_id

    @staticmethod
    def _build_pty(rows: Optional[int], cols: Optional[int]) -> Any:
        if rows is None or cols is None:
            return UNSET
        if rows <= 0 or cols <= 0:
            raise APIError(status_code=0, message="pty rows and cols must be > 0")
        return PTYSize(rows=rows, cols=cols)

    @staticmethod
    def _build_env_vars(env_vars: Optional[Dict[str, str]]) -> Any:
        if env_vars is None:
            return UNSET
        model = CreateContextRequestEnvVars()
        model.additional_properties = dict(env_vars)
        return model

