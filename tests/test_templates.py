from http import HTTPStatus
from unittest import TestCase

import httpx

from sandbox0.apispec.models.container_mount_spec import ContainerMountSpec
from sandbox0.apispec.models.container_spec import ContainerSpec
from sandbox0.apispec.models.resource_quota import ResourceQuota
from sandbox0.apispec.models.sandbox_template_spec import SandboxTemplateSpec
from sandbox0.apispec.models.shared_volume_spec import SharedVolumeSpec
from sandbox0.apispec.models.sidecar_container_spec import SidecarContainerSpec
from sandbox0.apispec.models.template_create_request import TemplateCreateRequest
from sandbox0.apispec.types import UNSET
from sandbox0.response_normalize import normalize_response_json
from sandbox0.template_helpers import (
    container as build_container,
    mount as build_mount,
    resources as build_resources,
    shared_volume as build_shared_volume,
    sidecar as build_sidecar,
    template_create_request,
    template_spec,
    template_update_request,
)


class TestTemplates(TestCase):
    def test_template_request_round_trips_shared_volumes(self) -> None:
        request = TemplateCreateRequest(
            template_id="tpl-shared-volume",
            spec=SandboxTemplateSpec(
                main_container=ContainerSpec(
                    image="nginx:1.27-alpine",
                    resources=ResourceQuota(cpu="500m", memory="2Gi"),
                ),
                shared_volumes=[
                    SharedVolumeSpec(
                        name="workspace",
                        mount_path="/workspace/shared",
                    )
                ],
                sidecars=[
                    SidecarContainerSpec(
                        name="helper",
                        image="busybox:latest",
                        resources=ResourceQuota(cpu="250m", memory="1Gi"),
                        mounts=[ContainerMountSpec(name="workspace", mount_path="/shared")],
                    )
                ],
            ),
        )

        encoded = request.to_dict()
        decoded = TemplateCreateRequest.from_dict(encoded)

        self.assertEqual(decoded.template_id, "tpl-shared-volume")
        self.assertEqual(len(decoded.spec.shared_volumes), 1)
        self.assertEqual(decoded.spec.shared_volumes[0].name, "workspace")
        self.assertEqual(len(decoded.spec.sidecars), 1)
        self.assertEqual(len(decoded.spec.sidecars[0].mounts), 1)
        self.assertEqual(decoded.spec.sidecars[0].mounts[0].mount_path, "/shared")

    def test_normalize_response_json_handles_shared_volumes(self) -> None:
        response = httpx.Response(
            status_code=HTTPStatus.OK,
            json={
                "data": {
                    "templateId": "tpl_123",
                    "spec": {
                        "sharedVolumes": None,
                        "sidecars": None,
                    },
                }
            },
        )

        normalize_response_json(response)
        body = response.json()

        self.assertEqual(body["data"]["spec"]["sharedVolumes"], [])
        self.assertEqual(body["data"]["spec"]["sidecars"], [])

    def test_template_helpers_build_shared_volume_requests(self) -> None:
        spec = template_spec(
            build_container("ubuntu:24.04", build_resources("1", "4Gi")),
            display_name="Helper Template",
            shared_volumes=[
                build_shared_volume(
                    "workspace",
                    "/workspace/shared",
                    sandbox_volume_id="vol_123",
                    writeback=True,
                )
            ],
            sidecars=[
                build_sidecar(
                    "helper",
                    "busybox:latest",
                    build_resources("250m", "1Gi"),
                    command=["sh", "-lc", "tail -f /dev/null"],
                    mounts=[build_mount("workspace", "/shared")],
                )
            ],
        )

        create_request = template_create_request("tpl-helper", spec)
        update_request = template_update_request(spec)

        self.assertEqual(create_request.template_id, "tpl-helper")
        self.assertEqual(create_request.spec.display_name, "Helper Template")
        self.assertEqual(len(create_request.spec.shared_volumes), 1)
        self.assertTrue(create_request.spec.shared_volumes[0].writeback)
        self.assertEqual(len(create_request.spec.sidecars), 1)
        self.assertEqual(create_request.spec.sidecars[0].mounts[0].mount_path, "/shared")
        self.assertIs(update_request.spec, spec)

    def test_template_helpers_allow_claim_bound_shared_volumes(self) -> None:
        volume = build_shared_volume("workspace", "/workspace/shared")

        self.assertEqual(volume.name, "workspace")
        self.assertEqual(volume.mount_path, "/workspace/shared")
        self.assertIs(volume.sandbox_volume_id, UNSET)
