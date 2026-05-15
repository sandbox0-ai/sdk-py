import datetime
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

from sandbox0 import Client
from sandbox0.apispec.models.function_alias import FunctionAlias
from sandbox0.apispec.models.function_record import FunctionRecord
from sandbox0.apispec.models.function_runtime_state import FunctionRuntimeState
from sandbox0.apispec.models.function_runtime_status import FunctionRuntimeStatus
from sandbox0.apispec.models.function_revision import FunctionRevision
from sandbox0.apispec.models.function_source_request import FunctionSourceRequest
from sandbox0.apispec.models.function_update_request import FunctionUpdateRequest
from sandbox0.apispec.models.sandbox_app_service import SandboxAppService
from sandbox0.apispec.models.sandbox_app_service_ingress import SandboxAppServiceIngress
from sandbox0.apispec.models.success_function_alias_list_response import SuccessFunctionAliasListResponse
from sandbox0.apispec.models.success_function_alias_list_response_data import SuccessFunctionAliasListResponseData
from sandbox0.apispec.models.success_function_alias_response import SuccessFunctionAliasResponse
from sandbox0.apispec.models.success_function_alias_response_data import SuccessFunctionAliasResponseData
from sandbox0.apispec.models.success_function_create_response import SuccessFunctionCreateResponse
from sandbox0.apispec.models.success_function_create_response_data import SuccessFunctionCreateResponseData
from sandbox0.apispec.models.success_function_response import SuccessFunctionResponse
from sandbox0.apispec.models.success_function_response_data import SuccessFunctionResponseData
from sandbox0.apispec.models.success_function_revision_create_response import (
    SuccessFunctionRevisionCreateResponse,
)
from sandbox0.apispec.models.success_function_revision_create_response_data import (
    SuccessFunctionRevisionCreateResponseData,
)
from sandbox0.apispec.models.success_function_revision_response import SuccessFunctionRevisionResponse
from sandbox0.apispec.models.success_function_revision_response_data import SuccessFunctionRevisionResponseData
from sandbox0.apispec.models.success_function_runtime_response import SuccessFunctionRuntimeResponse
from sandbox0.apispec.models.success_function_runtime_response_data import SuccessFunctionRuntimeResponseData
from sandbox0.apispec.types import Response, UNSET


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

    def test_update_delete_alias_revision_and_runtime(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)

        captured = {}

        def fake_update(*, id, client, body):
            captured["update_id"] = id
            captured["update_body"] = body
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionResponse(
                    success=True,
                    data=SuccessFunctionResponseData(function=_function_record(enabled=False)),
                ),
            )

        def fake_delete(*, id, client):
            captured["delete_id"] = id
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionResponse(
                    success=True,
                    data=SuccessFunctionResponseData(
                        function=_function_record(deleted_at=datetime.datetime(2026, 5, 14, 1, 0, tzinfo=datetime.timezone.utc))
                    ),
                ),
            )

        def fake_revision_get(*, id, revision_number, client):
            captured["revision_get"] = (id, revision_number)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionRevisionResponse(
                    success=True,
                    data=SuccessFunctionRevisionResponseData(revision=_function_revision(revision_number)),
                ),
            )

        def fake_aliases(*, id, client):
            captured["aliases_id"] = id
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionAliasListResponse(
                    success=True,
                    data=SuccessFunctionAliasListResponseData(aliases=[_function_alias(1)]),
                ),
            )

        def fake_alias_get(*, id, alias, client):
            captured["alias_get"] = (id, alias)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionAliasResponse(
                    success=True,
                    data=SuccessFunctionAliasResponseData(alias=_function_alias(1)),
                ),
            )

        def fake_runtime(*, id, client):
            captured.setdefault("runtime", []).append(id)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionRuntimeResponse(
                    success=True,
                    data=SuccessFunctionRuntimeResponseData(runtime=_function_runtime(FunctionRuntimeState.ACTIVE)),
                ),
            )

        def fake_runtime_idle(*, id, client):
            captured.setdefault("runtime_idle", []).append(id)
            return Response(
                status_code=HTTPStatus.OK,
                content=b"{}",
                headers={},
                parsed=SuccessFunctionRuntimeResponse(
                    success=True,
                    data=SuccessFunctionRuntimeResponseData(runtime=_function_runtime(FunctionRuntimeState.IDLE)),
                ),
            )

        with patch("sandbox0.client_functions.put_api_v1_functions_id.sync_detailed", side_effect=fake_update), patch(
            "sandbox0.client_functions.delete_api_v1_functions_id.sync_detailed",
            side_effect=fake_delete,
        ), patch(
            "sandbox0.client_functions.get_api_v1_functions_id_revisions_revision_number.sync_detailed",
            side_effect=fake_revision_get,
        ), patch(
            "sandbox0.client_functions.get_api_v1_functions_id_aliases.sync_detailed",
            side_effect=fake_aliases,
        ), patch(
            "sandbox0.client_functions.get_api_v1_functions_id_aliases_alias.sync_detailed",
            side_effect=fake_alias_get,
        ), patch(
            "sandbox0.client_functions.get_api_v1_functions_id_runtime.sync_detailed",
            side_effect=fake_runtime,
        ), patch(
            "sandbox0.client_functions.post_api_v1_functions_id_runtime_restart.sync_detailed",
            side_effect=fake_runtime_idle,
        ), patch(
            "sandbox0.client_functions.post_api_v1_functions_id_runtime_recycle.sync_detailed",
            side_effect=fake_runtime_idle,
        ):
            updated = client.functions.update("fn-1", FunctionUpdateRequest(name="new-name", enabled=False))
            deleted = client.delete_function("fn-1")
            revision = client.functions.get_revision("fn-1", 2)
            aliases = client.list_function_aliases("fn-1")
            alias = client.functions.get_alias("fn-1", "production")
            runtime = client.get_function_runtime("fn-1")
            restarted = client.functions.restart_runtime("fn-1")
            recycled = client.recycle_function_runtime("fn-1")

        self.assertEqual(captured["update_id"], "fn-1")
        self.assertEqual(captured["update_body"].name, "new-name")
        self.assertFalse(captured["update_body"].enabled)
        self.assertFalse(updated.enabled)
        self.assertEqual(captured["delete_id"], "fn-1")
        self.assertEqual(deleted.deleted_at.isoformat(), "2026-05-14T01:00:00+00:00")
        self.assertEqual(captured["revision_get"], ("fn-1", 2))
        self.assertEqual(revision.revision_number, 2)
        self.assertEqual(captured["aliases_id"], "fn-1")
        self.assertEqual(len(aliases), 1)
        self.assertEqual(captured["alias_get"], ("fn-1", "production"))
        self.assertEqual(alias.alias, "production")
        self.assertEqual(runtime.state, FunctionRuntimeState.ACTIVE)
        self.assertEqual(restarted.state, FunctionRuntimeState.IDLE)
        self.assertEqual(recycled.state, FunctionRuntimeState.IDLE)


def _function_record(*, enabled: bool = True, deleted_at=UNSET) -> FunctionRecord:
    return FunctionRecord(
        id="fn-1",
        team_id="team-1",
        name="web",
        slug="web",
        domain_label="web",
        enabled=enabled,
        created_at="2026-05-14T00:00:00Z",
        updated_at="2026-05-14T00:00:00Z",
        host="web.sandbox0.site",
        url="https://web.sandbox0.site",
        deleted_at=deleted_at,
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


def _function_runtime(state: FunctionRuntimeState) -> FunctionRuntimeStatus:
    runtime_sandbox_id = "sb-runtime" if state == FunctionRuntimeState.ACTIVE else UNSET
    runtime_context_id = "ctx-runtime" if state == FunctionRuntimeState.ACTIVE else UNSET
    return FunctionRuntimeStatus(
        function_id="fn-1",
        revision_id="rev-1",
        revision_number=1,
        state=state,
        runtime_sandbox_id=runtime_sandbox_id,
        runtime_context_id=runtime_context_id,
        runtime_updated_at=datetime.datetime(2026, 5, 14, tzinfo=datetime.timezone.utc),
    )
