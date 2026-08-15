from __future__ import annotations

from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


class SandboxSession:
    def __init__(self, sandbox: "Sandbox", closer: Callable[[], object]) -> None:
        self._sandbox = sandbox
        self._closer = closer
        self._closed = False

    @property
    def sandbox(self) -> "Sandbox":
        return self._sandbox

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._closer()

    def __enter__(self) -> "Sandbox":
        return self._sandbox

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        self.close()
