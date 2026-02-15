import unittest

from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.models import ExposedPort

from tests.e2e.helpers import claim_sandbox, new_client, require_config


class TestSandboxExposedPorts(unittest.TestCase):
    def test_exposed_ports_lifecycle(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        # Enable auto_resume to allow resume=True on exposed ports
        config = SandboxConfig(auto_resume=True)
        sandbox = claim_sandbox(self, client, cfg, config=config)

        sandbox.clear_exposed_ports()
        resp = sandbox.get_exposed_ports()
        self.assertEqual(len(resp.ports), 0)

        resp = sandbox.expose_port(3000, False)
        self.assertEqual(len(resp.ports), 1)
        self.assertEqual(resp.ports[0].port, 3000)
        self.assertFalse(resp.ports[0].resume)

        resp = sandbox.expose_port(3000, True)
        self.assertEqual(len(resp.ports), 1)
        self.assertTrue(resp.ports[0].resume)

        resp = sandbox.expose_port(8080, False)
        self.assertEqual(len(resp.ports), 2)

        resp = sandbox.unexpose_port(3000)
        self.assertEqual(len(resp.ports), 1)
        self.assertEqual(resp.ports[0].port, 8080)

        resp = sandbox.update_exposed_ports(
            [
                ExposedPort(port=4000, resume=True),
                ExposedPort(port=5000, resume=False),
                ExposedPort(port=6000, resume=True),
            ]
        )
        ports = {p.port: p.resume for p in resp.ports}
        self.assertEqual(ports.get(4000), True)
        self.assertEqual(ports.get(5000), False)
        self.assertEqual(ports.get(6000), True)

        sandbox.clear_exposed_ports()
        resp = sandbox.get_exposed_ports()
        self.assertEqual(len(resp.ports), 0)

        if not resp.exposure_domain:
            self.assertEqual(resp.exposure_domain, "")
