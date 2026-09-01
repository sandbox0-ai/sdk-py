import unittest
import time

from sandbox0 import APIError
from tests.e2e.helpers import claim_sandbox, close_client, new_client, require_config


class TestSandboxNetwork(unittest.TestCase):
    def test_network_policy(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)
        sandbox = claim_sandbox(self, client, cfg)

        policy = sandbox.get_network_policy()
        self.assertIsNotNone(policy)

        deadline = time.monotonic() + 60
        while True:
            try:
                updated = sandbox.update_network_policy(policy)
                break
            except APIError as error:
                if error.status_code != 503 or time.monotonic() >= deadline:
                    raise
                time.sleep(1)
        self.assertEqual(updated.mode, policy.mode)
