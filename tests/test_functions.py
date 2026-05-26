from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.function import Function
from sandbox0.apispec.models.function_deploy_result import FunctionDeployResult
from sandbox0.apispec.models.function_revision import FunctionRevision
from sandbox0.apispec.models.function_scale_policy import FunctionScalePolicy
from sandbox0.apispec.models.success_deleted_response import SuccessDeletedResponse
from sandbox0.apispec.models.success_deleted_response_data import SuccessDeletedResponseData
from sandbox0.apispec.models.success_function_deploy_result_response import SuccessFunctionDeployResultResponse
from sandbox0.apispec.models.success_function_list_response import SuccessFunctionListResponse
from sandbox0.apispec.models.success_function_list_response_data import SuccessFunctionListResponseData
from sandbox0.apispec.models.success_function_revision_list_response import SuccessFunctionRevisionListResponse
from sandbox0.apispec.models.success_function_revision_list_response_data import SuccessFunctionRevisionListResponseData
from sandbox0.apispec.types import Response
from sandbox0.resources import FunctionDeployOptions, FunctionDeploySpec, FunctionServiceSpec, FunctionSnapshotMount


class TestFunctions(TestCase):
    def test_deploy_builds_snapshot_request(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_sync_detailed(*, client, body):
            captured["body"] = body
            return _deploy_response()

        with patch("sandbox0.resources.post_api_v1_functions_deploy.sync_detailed", side_effect=fake_sync_detailed):
            result = client.functions.deploy(
                FunctionDeploySpec(
                    name="API",
                    slug="api",
                    template="node",
                    service=FunctionServiceSpec(
                        id="api",
                        port=8080,
                        command=["node", "server.js"],
                        cwd="/app",
                        env_vars={"NODE_ENV": "production"},
                        health_path="/healthz",
                    ),
                    mounts=[FunctionSnapshotMount(snapshot_id="snap_123", mount_path="/app")],
                    scale=FunctionScalePolicy(idle_timeout_seconds=120),
                    activate=False,
                )
            )

        request = captured["body"]
        encoded = request.to_dict()
        self.assertEqual(result.function.id, "fn_123")
        self.assertEqual(encoded["name"], "API")
        self.assertEqual(encoded["slug"], "api")
        self.assertEqual(encoded["activate"], False)
        self.assertEqual(encoded["scale"]["idle_timeout_seconds"], 120)
        self.assertEqual(encoded["source"]["type"], "snapshot")
        self.assertEqual(encoded["spec"]["template"], "node")
        self.assertEqual(encoded["spec"]["service"]["id"], "api")
        self.assertEqual(encoded["spec"]["service"]["runtime"]["command"], ["node", "server.js"])
        self.assertEqual(encoded["spec"]["mounts"][0]["snapshot_id"], "snap_123")
        self.assertEqual(encoded["spec"]["mounts"][0]["read_only"], True)

    def test_deploy_from_sandbox_service(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}

        def fake_sync_detailed(*, client, body):
            captured["body"] = body
            return _deploy_response()

        with patch("sandbox0.resources.post_api_v1_functions_deploy.sync_detailed", side_effect=fake_sync_detailed):
            result = client.functions.deploy_from_sandbox_service(
                "sb_123",
                "api",
                FunctionDeployOptions(name="API", slug="api"),
            )

        encoded = captured["body"].to_dict()
        self.assertEqual(result.function.slug, "api")
        self.assertEqual(encoded["source"]["type"], "sandbox_service")
        self.assertEqual(encoded["source"]["sandbox_service"]["sandbox_id"], "sb_123")
        self.assertEqual(encoded["source"]["sandbox_service"]["service_id"], "api")

    def test_list_revisions_and_activate(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        with patch(
            "sandbox0.resources.get_api_v1_functions.sync_detailed",
            return_value=Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionListResponse(
                    success=True,
                    data=SuccessFunctionListResponseData(functions=[_function()]),
                ),
            ),
        ):
            functions = client.functions.list()

        with patch(
            "sandbox0.resources.get_api_v1_functions_id_revisions.sync_detailed",
            return_value=Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionRevisionListResponse(
                    success=True,
                    data=SuccessFunctionRevisionListResponseData(revisions=[_revision()]),
                ),
            ),
        ):
            revisions = client.functions.revisions("api")

        with patch(
            "sandbox0.resources.put_api_v1_functions_id_active_revision.sync_detailed",
            return_value=_deploy_response(),
        ) as activate_mock:
            activated = client.functions.activate_revision("api", "fr_123")

        self.assertEqual(functions[0].id, "fn_123")
        self.assertEqual(revisions[0].id, "fr_123")
        self.assertEqual(activated.revision.id, "fr_123")
        request = activate_mock.call_args.kwargs["body"]
        self.assertEqual(request.revision_id, "fr_123")

    def test_delete_returns_deleted_response(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        with patch(
            "sandbox0.resources.delete_api_v1_functions_id.sync_detailed",
            return_value=Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessDeletedResponse(success=True, data=SuccessDeletedResponseData(deleted=True)),
            ),
        ):
            response = client.functions.delete("api")

        self.assertEqual(response.data.deleted, True)


def _deploy_response() -> Response:
    return Response(
        status_code=HTTPStatus.CREATED,
        content=b"{}",
        headers={},
        parsed=SuccessFunctionDeployResultResponse(
            success=True,
            data=FunctionDeployResult(function=_function(), revision=_revision()),
        ),
    )


def _function() -> Function:
    return Function.from_dict(
        {
            "id": "fn_123",
            "team_id": "team_123",
            "name": "API",
            "slug": "api",
            "domain_label": "api-abcd1234",
            "url": "https://api-abcd1234.fn.us.sandbox0.app",
            "active_revision_id": "fr_123",
            "enabled": True,
            "scale": {"idle_timeout_seconds": 300},
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
        }
    )


def _revision() -> FunctionRevision:
    return FunctionRevision.from_dict(
        {
            "id": "fr_123",
            "function_id": "fn_123",
            "team_id": "team_123",
            "number": 1,
            "source": {"type": "snapshot"},
            "spec": {
                "template": "node",
                "service": {
                    "id": "api",
                    "port": 8080,
                    "ingress": {"public": True, "routes": [{"id": "api", "resume": True}]},
                },
                "mounts": [],
            },
            "status": "active",
            "created_at": "2026-01-01T00:00:00Z",
        }
    )
