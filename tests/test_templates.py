from http import HTTPStatus
from unittest import TestCase

import httpx

from sandbox0.apispec.models.container_spec import ContainerSpec
from sandbox0.apispec.models.resource_quota import ResourceQuota
from sandbox0.apispec.models.sandbox_template_spec import SandboxTemplateSpec
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.models.warm_process_spec import WarmProcessSpec
from sandbox0.apispec.models.warm_process_spec_env_vars import WarmProcessSpecEnvVars
from sandbox0.apispec.models.warm_process_spec_type import WarmProcessSpecType
from sandbox0.response_normalize import normalize_response_json
from sandbox0.template_helpers import (
    container as build_container,
    resources as build_resources,
    template_create_request,
    template_spec,
    template_update_request,
    warm_process as build_warm_process,
)


class TestTemplates(TestCase):
    def test_template_request_round_trips_warm_processes(self) -> None:
        request = TemplateCreateRequest(
            template_id="tpl-warm-process",
            spec=SandboxTemplateSpec(
                main_container=ContainerSpec(
                    image="nginx:1.27-alpine",
                    resources=ResourceQuota(cpu="500m", memory="2Gi"),
                ),
                warm_processes=[
                    WarmProcessSpec(
                        type_=WarmProcessSpecType.CMD,
                        alias="helper",
                        command=["sh", "-lc", "tail -f /dev/null"],
                        cwd="/workspace",
                        env_vars=WarmProcessSpecEnvVars.from_dict({"MODE": "warm"}),
                    )
                ],
            ),
        )

        encoded = request.to_dict()
        decoded = TemplateCreateRequest.from_dict(encoded)

        self.assertEqual(decoded.template_id, "tpl-warm-process")
        self.assertEqual(len(decoded.spec.warm_processes), 1)
        process = decoded.spec.warm_processes[0]
        self.assertEqual(process.type_, WarmProcessSpecType.CMD)
        self.assertEqual(process.command, ["sh", "-lc", "tail -f /dev/null"])
        self.assertEqual(process.env_vars.additional_properties["MODE"], "warm")

    def test_normalize_response_json_handles_warm_processes(self) -> None:
        response = httpx.Response(
            status_code=HTTPStatus.OK,
            json={
                "data": {
                    "templateId": "tpl_123",
                    "spec": {
                        "warmProcesses": None,
                    },
                }
            },
        )

        normalize_response_json(response)
        body = response.json()

        self.assertEqual(body["data"]["spec"]["warmProcesses"], [])

    def test_template_helpers_build_warm_process_requests(self) -> None:
        spec = template_spec(
            build_container("ubuntu:24.04", build_resources("1", "4Gi")),
            display_name="Helper Template",
            warm_processes=[
                build_warm_process(
                    WarmProcessSpecType.CMD,
                    alias="helper",
                    command=["sh", "-lc", "tail -f /dev/null"],
                    cwd="/workspace",
                    env_vars={"MODE": "warm"},
                )
            ],
        )

        create_request = template_create_request("tpl-helper", spec)
        update_request = template_update_request(spec)

        self.assertEqual(create_request.template_id, "tpl-helper")
        self.assertEqual(create_request.spec.display_name, "Helper Template")
        self.assertEqual(len(create_request.spec.warm_processes), 1)
        process = create_request.spec.warm_processes[0]
        self.assertEqual(process.alias, "helper")
        self.assertEqual(process.cwd, "/workspace")
        self.assertEqual(process.env_vars.additional_properties["MODE"], "warm")
        self.assertIs(update_request.spec, spec)
