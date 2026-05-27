from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.function_invoke_request import FunctionInvokeRequest
from sandbox0.apispec.models.function_invoke_response import FunctionInvokeResponse
from sandbox0.apispec.models.function_invoke_response_headers import FunctionInvokeResponseHeaders
from sandbox0.apispec.models.success_function_invoke_response import SuccessFunctionInvokeResponse
from sandbox0.apispec.types import Response


class TestSandboxFunctions(TestCase):
    def test_invoke_function(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionInvokeResponse(
                    success=True,
                    data=FunctionInvokeResponse(
                        status=201,
                        headers=FunctionInvokeResponseHeaders.from_dict({"x-value": ["ok"]}),
                        body_base64="aGk=",
                    ),
                ),
            )

        request = FunctionInvokeRequest(method="POST", path="/hello", body_base64="e30=")
        with patch(
            "sandbox0.sandbox_functions.post_api_v1_sandboxes_id_functions_name_invoke.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            response = client.sandbox("sb_123").invoke_function("main", request)

        self.assertEqual(captured["id"], "sb_123")
        self.assertEqual(captured["name"], "main")
        self.assertIs(captured["body"], request)
        self.assertEqual(response.status, 201)
        self.assertEqual(response.headers["x-value"], ["ok"])
        self.assertEqual(response.body_base64, "aGk=")
