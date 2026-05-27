from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from sandbox0.apispec.api.functions import post_api_v1_sandboxes_id_functions_name_invoke
from sandbox0.apispec.models.function_invoke_request import FunctionInvokeRequest
from sandbox0.apispec.models.function_invoke_response import FunctionInvokeResponse
from sandbox0.apispec.models.success_function_invoke_response import SuccessFunctionInvokeResponse
from sandbox0.response import ensure_data

if TYPE_CHECKING:
    from sandbox0.sandbox import Sandbox


class SandboxFunctionsMixin:
    id: str
    _client: Any

    def invoke_function(
        self: "Sandbox",
        name: str,
        request: Optional[FunctionInvokeRequest] = None,
    ) -> FunctionInvokeResponse:  # type: ignore[misc]
        if not name.strip():
            raise ValueError("function name is required")
        resp = post_api_v1_sandboxes_id_functions_name_invoke.sync_detailed(
            id=self.id,
            name=name,
            client=self._client.api,
            body=request or FunctionInvokeRequest(),
        )
        return ensure_data(resp, SuccessFunctionInvokeResponse)
