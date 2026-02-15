from __future__ import annotations

from typing import Any, TYPE_CHECKING

from sandbox0.apispec.api.templates import delete_api_v1_templates_id
from sandbox0.apispec.api.templates import get_api_v1_templates
from sandbox0.apispec.api.templates import get_api_v1_templates_id
from sandbox0.apispec.api.templates import post_api_v1_templates
from sandbox0.apispec.api.templates import put_api_v1_templates_id
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.models.success_template_list_response import SuccessTemplateListResponse
from sandbox0.apispec.models.success_template_response import SuccessTemplateResponse
from sandbox0.apispec.models.template import Template
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.models.template_update_request import TemplateUpdateRequest
from sandbox0.response import ensure_data, ensure_model

if TYPE_CHECKING:
    from sandbox0.client import Client


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

    def update_template(self: "Client", template_id: str, request: TemplateUpdateRequest) -> Template:  # type: ignore[misc]
        resp = put_api_v1_templates_id.sync_detailed(id=template_id, client=self._api, body=request)
        return ensure_data(resp, SuccessTemplateResponse)

    def delete_template(self: "Client", template_id: str) -> SuccessMessageResponse:  # type: ignore[misc]
        resp = delete_api_v1_templates_id.sync_detailed(id=template_id, client=self._api)
        return ensure_model(resp, SuccessMessageResponse)
