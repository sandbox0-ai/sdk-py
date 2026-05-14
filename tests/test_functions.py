from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.function_alias import FunctionAlias
from sandbox0.apispec.models.function_record import FunctionRecord
from sandbox0.apispec.models.function_revision import FunctionRevision
from sandbox0.apispec.models.function_source_request import FunctionSourceRequest
from sandbox0.apispec.models.sandbox_app_service import SandboxAppService
from sandbox0.apispec.models.sandbox_app_service_ingress import SandboxAppServiceIngress
from sandbox0.apispec.models.success_function_alias_response import SuccessFunctionAliasResponse
from sandbox0.apispec.models.success_function_alias_response_data import SuccessFunctionAliasResponseData
from sandbox0.apispec.models.success_function_create_response import SuccessFunctionCreateResponse
from sandbox0.apispec.models.success_function_create_response_data import SuccessFunctionCreateResponseData
from sandbox0.apispec.models.success_function_revision_create_response import (
    SuccessFunctionRevisionCreateResponse,
)
from sandbox0.apispec.models.success_function_revision_create_response_data import (
    SuccessFunctionRevisionCreateResponseData,
)
from sandbox0.apispec.types import Response


class TestFunctions(TestCase):
    def test_create_from_sandbox_builds_request(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        captured = {}

        def fake_sync_detailed(*, client, body):
            captured["body"] = body
            return Response(
                status_code=HTTPStatus.CREATED,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionCreateResponse(
                    success=True,
                    data=SuccessFunctionCreateResponseData(
                        function=_function_record(),
                        revision=_function_revision(1),
                        alias=_function_alias(1),
                    ),
                ),
            )

        with patch("sandbox0.client_functions.post_api_v1_functions.sync_detailed", side_effect=fake_sync_detailed):
            result = client.functions.create_from_sandbox("sbx-1", "web", name="web-fn")

        request = captured["body"]
        self.assertEqual(request.name, "web-fn")
        self.assertEqual(request.source.sandbox_id, "sbx-1")
        self.assertEqual(request.source.service_id, "web")
        self.assertEqual(result.function.id, "fn-1")
        self.assertEqual(result.revision.revision_number, 1)
        self.assertEqual(result.alias.alias, "production")

    def test_create_revision_and_alias(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        captured = {}

        def fake_revision(*, id, client, body):
            captured["revision_id"] = id
            captured["revision_body"] = body
            return Response(
                status_code=HTTPStatus.CREATED,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionRevisionCreateResponse(
                    success=True,
                    data=SuccessFunctionRevisionCreateResponseData(
                        revision=_function_revision(2),
                        promoted=False,
                    ),
                ),
            )

        def fake_alias(*, id, alias, client, body):
            captured["alias_id"] = id
            captured["alias"] = alias
            captured["alias_body"] = body
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionAliasResponse(
                    success=True,
                    data=SuccessFunctionAliasResponseData(alias=_function_alias(body.revision_number)),
                ),
            )

        with patch(
            "sandbox0.client_functions.post_api_v1_functions_id_revisions.sync_detailed",
            side_effect=fake_revision,
        ), patch(
            "sandbox0.client_functions.put_api_v1_functions_id_aliases_alias.sync_detailed",
            side_effect=fake_alias,
        ):
            revision = client.create_function_revision_from_sandbox("fn-1", "sbx-1", "web-v2", promote=False)
            alias = client.functions.set_alias("fn-1", "production", 2)

        self.assertEqual(captured["revision_id"], "fn-1")
        self.assertEqual(captured["revision_body"].source.service_id, "web-v2")
        self.assertFalse(captured["revision_body"].promote)
        self.assertFalse(revision.promoted)
        self.assertEqual(captured["alias"], "production")
        self.assertEqual(alias.revision_number, 2)


def _function_record() -> FunctionRecord:
    return FunctionRecord(
        id="fn-1",
        team_id="team-1",
        name="web",
        slug="web",
        domain_label="web",
        created_at="2026-05-14T00:00:00Z",
        updated_at="2026-05-14T00:00:00Z",
        host="web.sandbox0.site",
        url="https://web.sandbox0.site",
    )


def _function_revision(revision_number: int) -> FunctionRevision:
    return FunctionRevision(
        id=f"rev-{revision_number}",
        function_id="fn-1",
        team_id="team-1",
        revision_number=revision_number,
        source_sandbox_id="sbx-1",
        source_service_id="web",
        source_template_id="default",
        service_snapshot=SandboxAppService(
            id="web",
            port=8080,
            ingress=SandboxAppServiceIngress(public=True),
        ),
        created_at="2026-05-14T00:00:00Z",
    )


def _function_alias(revision_number: int) -> FunctionAlias:
    return FunctionAlias(
        function_id="fn-1",
        alias="production",
        revision_id=f"rev-{revision_number}",
        revision_number=revision_number,
        updated_at="2026-05-14T00:00:00Z",
    )
