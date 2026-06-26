from __future__ import annotations

from typing import Any, Optional

from deepagents.backends.protocol import (
    ExecuteResponse,
    FileDownloadResponse,
    FileUploadResponse,
)
from deepagents.backends.sandbox import BaseSandbox

from sandbox0.errors import APIError
from sandbox0.sandbox import CmdOptions, Sandbox

DEFAULT_WORKING_DIR = "/workspace"
DEFAULT_COMMAND_TIMEOUT_SEC = 30 * 60


class Sandbox0DeepAgentsSandbox(BaseSandbox):
    """Deep Agents sandbox backend backed by a Sandbox0 sandbox."""

    def __init__(
        self,
        *,
        sandbox: Sandbox,
        working_dir: str = DEFAULT_WORKING_DIR,
        default_timeout: int = DEFAULT_COMMAND_TIMEOUT_SEC,
    ) -> None:
        self._sandbox = sandbox
        self._working_dir = working_dir
        self._default_timeout = default_timeout

    @property
    def id(self) -> str:
        """Return the Sandbox0 sandbox ID."""
        return self._sandbox.id

    @property
    def working_dir(self) -> str:
        """Return the working directory used for shell commands."""
        return self._working_dir

    def execute(
        self,
        command: str,
        *,
        timeout: Optional[int] = None,
    ) -> ExecuteResponse:
        """Execute a shell command in the Sandbox0 sandbox."""
        effective_timeout = self._default_timeout if timeout is None else timeout
        ttl_sec = None if effective_timeout == 0 else max(int(effective_timeout), 1)
        try:
            result = self._sandbox.cmd(
                command or "true",
                CmdOptions(
                    command=["bash", "-lc", command],
                    wait=True,
                    cwd=self._working_dir,
                    ttl_sec=ttl_sec,
                ),
            )
        except Exception as exc:  # noqa: BLE001 - normalize transport failures for LLM callers
            return ExecuteResponse(output=str(exc), exit_code=1, truncated=False)

        output = _combine_output(result.stdout, result.stderr, result.output_raw)
        return ExecuteResponse(
            output=output,
            exit_code=result.exit_code,
            truncated=False,
        )

    def upload_files(self, files: list[tuple[str, bytes]]) -> list[FileUploadResponse]:
        """Upload files into the Sandbox0 sandbox."""
        responses: list[FileUploadResponse] = []
        for path, content in files:
            if not path.startswith("/"):
                responses.append(FileUploadResponse(path=path, error="invalid_path"))
                continue
            try:
                self._sandbox.write_file(path, content)
            except Exception as exc:  # noqa: BLE001 - partial success is part of the contract
                responses.append(FileUploadResponse(path=path, error=_map_file_error(exc)))
            else:
                responses.append(FileUploadResponse(path=path, error=None))
        return responses

    def download_files(self, paths: list[str]) -> list[FileDownloadResponse]:
        """Download files from the Sandbox0 sandbox."""
        responses: list[FileDownloadResponse] = []
        for path in paths:
            if not path.startswith("/"):
                responses.append(
                    FileDownloadResponse(path=path, content=None, error="invalid_path")
                )
                continue
            try:
                content = self._sandbox.read_file(path)
            except Exception as exc:  # noqa: BLE001 - partial success is part of the contract
                responses.append(
                    FileDownloadResponse(
                        path=path,
                        content=None,
                        error=_map_file_error(exc),
                    )
                )
            else:
                responses.append(
                    FileDownloadResponse(path=path, content=content, error=None)
                )
        return responses


def _combine_output(stdout: str, stderr: str, output_raw: str) -> str:
    if stdout or stderr:
        output = stdout
        if stderr.strip():
            output += f"\n<stderr>{stderr.strip()}</stderr>"
        return output
    return output_raw


def _map_file_error(exc: Exception) -> str:
    if isinstance(exc, APIError):
        if exc.status_code == 404:
            return "file_not_found"
        if exc.status_code == 403:
            return "permission_denied"
        if exc.status_code == 400:
            return _classify_message(exc.message, default="invalid_path")
        classified = _classify_message(
            " ".join(part for part in (exc.code, exc.message) if part),
            default="",
        )
        if classified:
            return classified
        return exc.code or exc.message or str(exc)
    return _classify_message(str(exc), default=str(exc))


def _classify_message(message: str, *, default: str) -> str:
    lowered = message.lower()
    if "not found" in lowered or "no such file" in lowered:
        return "file_not_found"
    if "permission" in lowered or "denied" in lowered:
        return "permission_denied"
    if (
        "is a directory" in lowered
        or "not a file" in lowered
        or "path_not_file" in lowered
        or lowered.endswith("directory")
    ):
        return "is_directory"
    if "invalid" in lowered or "relative" in lowered:
        return "invalid_path"
    return default
