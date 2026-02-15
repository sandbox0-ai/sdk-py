import unittest

from tests.e2e.helpers import claim_sandbox, close_client, new_client, require_config


class TestSandboxNetwork(unittest.TestCase):
    def test_network_policy(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)
        sandbox = claim_sandbox(self, client, cfg)

        policy = sandbox.get_network_policy()
        self.assertIsNotNone(policy)

        updated = sandbox.update_network_policy(policy)
        self.assertEqual(updated.mode, policy.mode)
