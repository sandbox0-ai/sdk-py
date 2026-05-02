from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.public_gateway_config import PublicGatewayConfig
from sandbox0.apispec.models.public_gateway_route import PublicGatewayRoute
from sandbox0.apispec.models.success_public_gateway_response import SuccessPublicGatewayResponse
from sandbox0.apispec.models.success_public_gateway_response_data import SuccessPublicGatewayResponseData
from sandbox0.apispec.types import Response


class TestSandboxPublicGateway(TestCase):
    def test_get_and_clear_public_gateway(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_get_sync_detailed(**kwargs):
            captured["get"] = kwargs
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessPublicGatewayResponse(
                    success=True,
                    data=SuccessPublicGatewayResponseData(
                        sandbox_id="sb_123",
                        public_gateway=PublicGatewayConfig(
                            enabled=True,
                            routes=[PublicGatewayRoute(id="api", port=8080, resume=True)],
                        ),
                        exposure_domain="example.test",
                    ),
                ),
            )

        def fake_put_sync_detailed(**kwargs):
            captured["put"] = kwargs
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessPublicGatewayResponse(
                    success=True,
                    data=SuccessPublicGatewayResponseData(
                        sandbox_id="sb_123",
                        public_gateway=kwargs["body"],
                        exposure_domain="example.test",
                    ),
                ),
            )

        with (
            patch(
                "sandbox0.sandbox_public_gateway.get_api_v1_sandboxes_id_public_gateway.sync_detailed",
                side_effect=fake_get_sync_detailed,
            ),
            patch(
                "sandbox0.sandbox_public_gateway.put_api_v1_sandboxes_id_public_gateway.sync_detailed",
                side_effect=fake_put_sync_detailed,
            ),
        ):
            current = client.sandbox("sb_123").get_public_gateway()
            cleared = client.sandbox("sb_123").clear_public_gateway()

        self.assertEqual(captured["get"]["id"], "sb_123")
        self.assertTrue(current.public_gateway.enabled)
        self.assertEqual(current.public_gateway.routes[0].port, 8080)
        self.assertEqual(current.exposure_domain, "example.test")
        self.assertEqual(captured["put"]["id"], "sb_123")
        self.assertFalse(captured["put"]["body"].enabled)
        self.assertFalse(cleared.public_gateway.enabled)
