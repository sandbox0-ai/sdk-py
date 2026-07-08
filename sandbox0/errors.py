from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


CLAIM_START_THROTTLED_CODE = "claim_start_throttled"


@dataclass
class APIError(Exception):
    status_code: int
    message: str
    code: Optional[str] = None
    request_id: Optional[str] = None
    details: Any = None
    body: Optional[bytes] = None
    retry_after: Optional[int] = None

    def __str__(self) -> str:
        parts = [f"status={self.status_code}"]
        if self.code:
            parts.append(f"code={self.code}")
        if self.request_id:
            parts.append(f"request_id={self.request_id}")
        parts.append(f"message={self.message}")
        return "APIError(" + ", ".join(parts) + ")"

    def is_claim_start_throttled(self) -> bool:
        return self.status_code == 429 and self.code == CLAIM_START_THROTTLED_CODE


def is_claim_start_throttled(error: BaseException) -> bool:
    return isinstance(error, APIError) and error.is_claim_start_throttled()
