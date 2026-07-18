from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from sandbox0.apispec.models.template import Template
from sandbox0.apispec.types import Unset

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


class TemplateWaitTimeoutError(TimeoutError):
    def __init__(
        self,
        *,
        template_id: str,
        timeout_sec: float,
        last_template: Optional[Template] = None,
    ) -> None:
        super().__init__(
            f"timed out waiting for template {template_id} after {timeout_sec} seconds"
        )
        self.template_id = template_id
        self.timeout_sec = timeout_sec
        self.last_template = last_template


class TemplateCreationFailedError(RuntimeError):
    def __init__(self, template: Template) -> None:
        creation = None
        if not isinstance(template.status, Unset) and not isinstance(
            template.status.creation, Unset
        ):
            creation = template.status.creation

        stage = None
        reason = None
        detail = "template creation failed"
        if creation is not None:
            stage = creation.stage.value
            if not isinstance(creation.reason, Unset):
                reason = creation.reason
            if not isinstance(creation.message, Unset):
                detail = creation.message
            elif reason:
                detail = reason

        super().__init__(f"template {template.template_id} creation failed: {detail}")
        self.template_id = template.template_id
        self.stage = stage
        self.reason = reason
        self.last_template = template
