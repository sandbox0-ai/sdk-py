from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.sandbox_app_service import SandboxAppService
from sandbox0.apispec.models.sandbox_app_service_ingress import SandboxAppServiceIngress
from sandbox0.apispec.models.sandbox_app_service_route import SandboxAppServiceRoute
from sandbox0.apispec.models.sandbox_app_service_runtime import SandboxAppServiceRuntime
from sandbox0.apispec.models.sandbox_app_service_runtime_type import SandboxAppServiceRuntimeType
from sandbox0.apispec.models.sandbox_app_service_view import SandboxAppServiceView
from sandbox0.apispec.models.sandbox_function import SandboxFunction
from sandbox0.apispec.models.sandbox_function_runtime import SandboxFunctionRuntime
from sandbox0.apispec.models.sandbox_function_source import SandboxFunctionSource
from sandbox0.apispec.models.sandbox_function_source_type import SandboxFunctionSourceType
from sandbox0.apispec.models.success_sandbox_services_response import SuccessSandboxServicesResponse
from sandbox0.apispec.models.success_sandbox_services_response_data import SuccessSandboxServicesResponseData
from sandbox0.apispec.types import Response


class TestSandboxServices(TestCase):
    def test_get_and_clear_services(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_get_sync_detailed(**kwargs):
            captured["get"] = kwargs
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessSandboxServicesResponse(
                    success=True,
                    data=SuccessSandboxServicesResponseData(
                        sandbox_id="sb_123",
                        services=[
                            SandboxAppServiceView(
                                id="api",
                                port=8080,
                                ingress=SandboxAppServiceIngress(
                                    public=True,
                                    routes=[SandboxAppServiceRoute(id="api", resume=True)],
                                ),
                                publishable=False,
                                public_url="https://rs-default-api-abcde--p8080.us.sandbox0.app",
                            )
                        ],
                    ),
                ),
            )

        def fake_put_sync_detailed(**kwargs):
            captured["put"] = kwargs
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessSandboxServicesResponse(
                    success=True,
                    data=SuccessSandboxServicesResponseData(
                        sandbox_id="sb_123",
                        services=[],
                    ),
                ),
            )

        with (
            patch(
                "sandbox0.sandbox_services.get_api_v1_sandboxes_id_services.sync_detailed",
                side_effect=fake_get_sync_detailed,
            ),
            patch(
                "sandbox0.sandbox_services.put_api_v1_sandboxes_id_services.sync_detailed",
                side_effect=fake_put_sync_detailed,
            ),
        ):
            current = client.sandbox("sb_123").get_services()
            cleared = client.sandbox("sb_123").clear_services()

        self.assertEqual(captured["get"]["id"], "sb_123")
        self.assertEqual(current.services[0].id, "api")
        self.assertEqual(current.services[0].port, 8080)
        self.assertEqual(
            current.services[0].public_url,
            "https://rs-default-api-abcde--p8080.us.sandbox0.app",
        )
        self.assertEqual(captured["put"]["id"], "sb_123")
        self.assertEqual(captured["put"]["body"].services, [])
        self.assertEqual(cleared.services, [])

    def test_update_services(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_put_sync_detailed(**kwargs):
            captured["put"] = kwargs
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessSandboxServicesResponse(
                    success=True,
                    data=SuccessSandboxServicesResponseData(
                        sandbox_id="sb_123",
                        services=[],
                    ),
                ),
            )

        service = SandboxAppService(
            id="api",
            port=8080,
            ingress=SandboxAppServiceIngress(public=True, routes=[SandboxAppServiceRoute(id="api", resume=True)]),
        )
        with patch(
            "sandbox0.sandbox_services.put_api_v1_sandboxes_id_services.sync_detailed",
            side_effect=fake_put_sync_detailed,
        ):
            client.sandbox("sb_123").update_services([service])

        self.assertEqual(captured["put"]["body"].services, [service])

    def test_update_function_service(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_put_sync_detailed(**kwargs):
            captured["put"] = kwargs
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessSandboxServicesResponse(
                    success=True,
                    data=SuccessSandboxServicesResponseData(
                        sandbox_id="sb_123",
                        services=[],
                    ),
                ),
            )

        service = SandboxAppService(
            id="handler",
            port=49983,
            runtime=SandboxAppServiceRuntime(
                type_=SandboxAppServiceRuntimeType.FUNCTION,
                function=SandboxFunction(
                    runtime=SandboxFunctionRuntime.PYTHON,
                    handler="handler",
                    source=SandboxFunctionSource(
                        type_=SandboxFunctionSourceType.INLINE,
                        code="def handler(request):\n    return {'status': 200, 'body': 'ok'}\n",
                    ),
                ),
            ),
            ingress=SandboxAppServiceIngress(
                public=True,
                routes=[SandboxAppServiceRoute(id="handler", path_prefix="/", resume=True)],
            ),
        )
        with patch(
            "sandbox0.sandbox_services.put_api_v1_sandboxes_id_services.sync_detailed",
            side_effect=fake_put_sync_detailed,
        ):
            client.sandbox("sb_123").update_services([service])

        self.assertEqual(captured["put"]["body"].services, [service])
        self.assertEqual(service.runtime.type_, SandboxAppServiceRuntimeType.FUNCTION)
        self.assertEqual(service.runtime.function.runtime, SandboxFunctionRuntime.PYTHON)
        self.assertEqual(service.runtime.function.source.type_, SandboxFunctionSourceType.INLINE)
