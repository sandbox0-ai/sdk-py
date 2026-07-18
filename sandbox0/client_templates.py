from __future__ import annotations

import math
import time
from dataclasses import dataclass
from typing import Any, Optional, TYPE_CHECKING

from sandbox0.apispec.api.templates import delete_api_v1_templates_id
from sandbox0.apispec.api.templates import get_api_v1_templates
from sandbox0.apispec.api.templates import get_api_v1_templates_id
from sandbox0.apispec.api.templates import post_api_v1_templates
from sandbox0.apispec.api.templates import post_api_v1_templates_from_sandbox
from sandbox0.apispec.api.templates import put_api_v1_templates_id
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_template_list_response import SuccessTemplateListResponse
from sandbox0.apispec.models.success_template_response import SuccessTemplateResponse
from sandbox0.apispec.models.template import Template
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.models.template_creation_status_state import (
    TemplateCreationStatusState,
)
from sandbox0.apispec.models.template_from_sandbox_create_request import (
    TemplateFromSandboxCreateRequest,
)
from sandbox0.apispec.models.template_update_request import TemplateUpdateRequest
from sandbox0.apispec.types import UNSET, Unset
from sandbox0.errors import (
    TemplateCreationFailedError,
    TemplateWaitTimeoutError,
)
from sandbox0.response import ensure_data, ensure_model

if TYPE_CHECKING:
    from sandbox0.client import Client


@dataclass(frozen=True)
class CreateTemplateFromSandboxOptions:
    """Options for creating a template from a sandbox."""

    idempotency_key: Optional[str] = None
    wait: bool = False
    timeout_sec: float = 600.0
    poll_interval_sec: float = 0.5


class ClientTemplatesMixin:
    _api: Any

    def list_templates(self: "Client") -> list[Template]:  # type: ignore[misc]
        resp = get_api_v1_templates.sync_detailed(client=self._api)
        data = ensure_data(resp, SuccessTemplateListResponse)
        templates = data.templates
        if templates.__class__.__name__ == "Unset":
            return []
        return templates

    # Backward-compatible alias.
    def list_template(self: "Client") -> list[Template]:  # type: ignore[misc]
        return self.list_templates()  # type: ignore[attr-defined]

    def get_template(self: "Client", template_id: str) -> Template:  # type: ignore[misc]
        resp = get_api_v1_templates_id.sync_detailed(id=template_id, client=self._api)
        return ensure_data(resp, SuccessTemplateResponse)

    def create_template(self: "Client", request: TemplateCreateRequest) -> Template:  # type: ignore[misc]
        resp = post_api_v1_templates.sync_detailed(client=self._api, body=request)
        return ensure_data(resp, SuccessTemplateResponse)

    def create_template_from_sandbox(  # type: ignore[misc]
        self: "Client",
        request: TemplateFromSandboxCreateRequest,
        options: Optional[CreateTemplateFromSandboxOptions] = None,
    ) -> Template:
        opts = options or CreateTemplateFromSandboxOptions()
        resp = post_api_v1_templates_from_sandbox.sync_detailed(
            client=self._api,
            body=request,
            idempotency_key=(
                opts.idempotency_key
                if opts.idempotency_key is not None
                else UNSET
            ),
        )
        template = ensure_data(resp, SuccessTemplateResponse)
        if not opts.wait:
            return template
        return self.wait_template_ready(  # type: ignore[attr-defined]
            template.template_id,
            timeout_sec=opts.timeout_sec,
            poll_interval_sec=opts.poll_interval_sec,
        )

    def wait_template_ready(  # type: ignore[misc]
        self: "Client",
        template_id: str,
        *,
        timeout_sec: float = 600.0,
        poll_interval_sec: float = 0.5,
    ) -> Template:
        if not math.isfinite(timeout_sec) or timeout_sec < 0:
            raise ValueError("timeout_sec must be a finite value greater than or equal to zero")
        if not math.isfinite(poll_interval_sec) or poll_interval_sec <= 0:
            raise ValueError("poll_interval_sec must be a finite value greater than zero")

        deadline = time.monotonic() + timeout_sec
        last_template: Optional[Template] = None
        while True:
            last_template = self.get_template(template_id)  # type: ignore[attr-defined]
            if isinstance(last_template.status, Unset) or isinstance(
                last_template.status.creation, Unset
            ):
                return last_template

            state = last_template.status.creation.state
            if state == TemplateCreationStatusState.READY:
                return last_template
            if state == TemplateCreationStatusState.FAILED:
                raise TemplateCreationFailedError(last_template)
            if state != TemplateCreationStatusState.CREATING:
                raise RuntimeError(
                    f"template {template_id} has unknown creation state {state!s}"
                )

            remaining_sec = deadline - time.monotonic()
            if remaining_sec <= 0:
                raise TemplateWaitTimeoutError(
                    template_id=template_id,
                    timeout_sec=timeout_sec,
                    last_template=last_template,
                )
            time.sleep(min(poll_interval_sec, remaining_sec))

    def update_template(self: "Client", template_id: str, request: TemplateUpdateRequest) -> Template:  # type: ignore[misc]
        resp = put_api_v1_templates_id.sync_detailed(id=template_id, client=self._api, body=request)
        return ensure_data(resp, SuccessTemplateResponse)

    def delete_template(self: "Client", template_id: str) -> SuccessMessageResponse:  # type: ignore[misc]
        resp = delete_api_v1_templates_id.sync_detailed(id=template_id, client=self._api)
        return ensure_model(resp, SuccessMessageResponse)
