from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

import httpx

from sandbox0 import (
    Client,
    CreateTemplateFromSandboxOptions,
    TemplateCreationFailedError,
    TemplateWaitTimeoutError,
)
from sandbox0.apispec.models.container_spec import ContainerSpec
from sandbox0.apispec.models.resource_quota import ResourceQuota
from sandbox0.apispec.models.sandbox_template_spec import SandboxTemplateSpec
from sandbox0.apispec.models.sandbox_template_spec_env_vars import SandboxTemplateSpecEnvVars
from sandbox0.apispec.models.success_template_response import SuccessTemplateResponse
from sandbox0.apispec.models.template import Template
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.models.template_from_sandbox_spec_overrides import (
    TemplateFromSandboxSpecOverrides,
)
from sandbox0.apispec.types import Response
from sandbox0.response_normalize import normalize_response_json
from sandbox0.template_helpers import (
    container as build_container,
    resources as build_resources,
    template_create_request,
    template_from_sandbox_create_request,
    template_spec,
    template_update_request,
)


class TestTemplates(TestCase):
    def test_template_request_round_trips_env_vars(self) -> None:
        request = TemplateCreateRequest(
            template_id="tpl-env-vars",
            spec=SandboxTemplateSpec(
                main_container=ContainerSpec(
                    image="nginx:1.27-alpine",
                    resources=ResourceQuota(memory="2Gi"),
                ),
                env_vars=SandboxTemplateSpecEnvVars.from_dict({"MODE": "template"}),
            ),
        )

        encoded = request.to_dict()
        decoded = TemplateCreateRequest.from_dict(encoded)

        self.assertEqual(decoded.template_id, "tpl-env-vars")
        self.assertEqual(decoded.spec.env_vars.additional_properties["MODE"], "template")

    def test_normalize_response_json_handles_tags(self) -> None:
        response = httpx.Response(
            status_code=HTTPStatus.OK,
            json={
                "data": {
                    "templateId": "tpl_123",
                    "spec": {
                        "tags": None,
                    },
                }
            },
        )

        normalize_response_json(response)
        body = response.json()

        self.assertEqual(body["data"]["spec"]["tags"], [])

    def test_template_helpers_build_template_requests(self) -> None:
        spec = template_spec(
            build_container("ubuntu:24.04", build_resources("4Gi")),
            display_name="Helper Template",
            env_vars={"MODE": "template"},
        )

        create_request = template_create_request("tpl-helper", spec)
        from_sandbox_request = template_from_sandbox_create_request(
            "tpl-derived",
            "sb_123",
            TemplateFromSandboxSpecOverrides(display_name="Derived Template"),
        )
        update_request = template_update_request(spec)

        self.assertEqual(create_request.template_id, "tpl-helper")
        self.assertEqual(create_request.spec.display_name, "Helper Template")
        self.assertEqual(create_request.spec.env_vars.additional_properties["MODE"], "template")
        self.assertEqual(from_sandbox_request.template_id, "tpl-derived")
        self.assertEqual(from_sandbox_request.sandbox_id, "sb_123")
        self.assertEqual(
            from_sandbox_request.spec_overrides.display_name,
            "Derived Template",
        )
        self.assertIs(update_request.spec, spec)

    def test_create_template_from_sandbox_passes_idempotency_key(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        captured = {}
        creating = _template_fixture("creating")

        def fake_sync_detailed(**kwargs):
            captured.update(kwargs)
            return Response(
                status_code=HTTPStatus.ACCEPTED,
                content=b"{}",
                headers={},
                parsed=SuccessTemplateResponse(success=True, data=creating),
            )

        request = template_from_sandbox_create_request("tpl-derived", "sb_123")
        with patch(
            "sandbox0.client_templates.post_api_v1_templates_from_sandbox.sync_detailed",
            side_effect=fake_sync_detailed,
        ):
            result = client.create_template_from_sandbox(
                request,
                CreateTemplateFromSandboxOptions(
                    idempotency_key="create-derived-1"
                ),
            )

        self.assertIs(result, creating)
        self.assertIs(captured["body"], request)
        self.assertEqual(captured["idempotency_key"], "create-derived-1")

    def test_wait_template_ready_polls_until_ready(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        observations = [
            _template_fixture("creating"),
            _template_fixture("ready"),
        ]

        with patch.object(client, "get_template", side_effect=observations) as get:
            result = client.wait_template_ready(
                "tpl-derived",
                timeout_sec=1,
                poll_interval_sec=0.001,
            )

        self.assertEqual(result.status.creation.state.value, "ready")
        self.assertEqual(get.call_count, 2)

    def test_wait_template_ready_accepts_legacy_template(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        legacy = _template_fixture()

        with patch.object(client, "get_template", return_value=legacy):
            result = client.wait_template_ready(
                "tpl-legacy",
                timeout_sec=0,
                poll_interval_sec=0.001,
            )

        self.assertIs(result, legacy)

    def test_wait_template_ready_reports_failure_and_timeout(self) -> None:
        client = Client(token="test-token", base_url="https://example.com")
        self.addCleanup(client.close)
        failed = _template_fixture(
            "failed",
            stage="publishing",
            reason="registry_push_failed",
            message="registry rejected the image",
        )

        with patch.object(client, "get_template", return_value=failed):
            with self.assertRaises(TemplateCreationFailedError) as failure:
                client.wait_template_ready(
                    "tpl-derived",
                    timeout_sec=1,
                    poll_interval_sec=0.001,
                )

        self.assertEqual(failure.exception.stage, "publishing")
        self.assertEqual(failure.exception.reason, "registry_push_failed")

        creating = _template_fixture("creating")
        with patch.object(client, "get_template", return_value=creating):
            with self.assertRaises(TemplateWaitTimeoutError) as timeout:
                client.wait_template_ready(
                    "tpl-derived",
                    timeout_sec=0,
                    poll_interval_sec=0.001,
                )

        self.assertIs(timeout.exception.last_template, creating)


def _template_fixture(
    state: str | None = None,
    *,
    stage: str | None = None,
    reason: str | None = None,
    message: str | None = None,
) -> Template:
    status = {}
    if state is not None:
        creation = {"state": state, "stage": stage or "capturing"}
        if reason is not None:
            creation["reason"] = reason
        if message is not None:
            creation["message"] = message
        status["creation"] = creation

    return Template.from_dict(
        {
            "template_id": "tpl-derived",
            "scope": "team",
            "spec": {},
            "status": status,
            "created_at": "2026-07-18T00:00:00Z",
            "updated_at": "2026-07-18T00:00:00Z",
        }
    )
