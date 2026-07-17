from http import HTTPStatus
from unittest import TestCase

import httpx

from sandbox0.apispec.models.container_spec import ContainerSpec
from sandbox0.apispec.models.resource_quota import ResourceQuota
from sandbox0.apispec.models.sandbox_template_spec import SandboxTemplateSpec
from sandbox0.apispec.models.sandbox_template_spec_env_vars import SandboxTemplateSpecEnvVars
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.response_normalize import normalize_response_json
from sandbox0.template_helpers import (
    container as build_container,
    resources as build_resources,
    template_create_request,
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
        update_request = template_update_request(spec)

        self.assertEqual(create_request.template_id, "tpl-helper")
        self.assertEqual(create_request.spec.display_name, "Helper Template")
        self.assertEqual(create_request.spec.env_vars.additional_properties["MODE"], "template")
        self.assertIs(update_request.spec, spec)
