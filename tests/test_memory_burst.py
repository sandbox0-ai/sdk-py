import json
from unittest import TestCase

import httpx
from sandbox0 import Client
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_resource_config import SandboxResourceConfig
from sandbox0.apispec.types import UNSET


class TestMemoryBurst(TestCase):
    def test_omitted_burst_keeps_legacy_wire_shape(self) -> None:
        self.assertEqual(SandboxResourceConfig(memory="4Gi").to_dict(), {"memory": "4Gi"})
        self.assertIs(SandboxResourceConfig.from_dict({"memory": "4Gi"}).memory_burst_percent, UNSET)

    def test_memory_shortcut_preserves_burst_without_mutating_config(self) -> None:
        for legacy in (False, True):
            for percent in (0, 50):
                with self.subTest(legacy=legacy, percent=percent):
                    config = SandboxConfig(resources=SandboxResourceConfig(memory="2Gi", memory_burst_percent=percent))
                    captured = []
                    def handler(request: httpx.Request) -> httpx.Response:
                        captured.append(json.loads(request.content))
                        return httpx.Response(201, json={"success": True, "data": {"sandbox_id": "sb_burst", "template": "default", "status": "running", "runtime_id": "allocation", "cluster_id": "cluster"}})
                    with Client(token="test-token", base_url="https://example.test") as client:
                        client.api.set_httpx_client(httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler)))
                        if legacy:
                            client.claim_sandbox("default", config=config, memory="4Gi")
                        else:
                            client.sandboxes.claim("default", config=config, memory="4Gi")
                    self.assertEqual(captured[0]["config"]["resources"], {"memory": "4Gi", "memory_burst_percent": percent})
                    self.assertEqual(config.resources.memory, "2Gi")
