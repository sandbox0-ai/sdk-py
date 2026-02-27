import unittest

from sandbox0.apispec.models.get_api_v1_sandboxes_status import GetApiV1SandboxesStatus
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.sandbox_config_env_vars import SandboxConfigEnvVars
from sandbox0.apispec.models.sandbox_update_config import SandboxUpdateConfig
from sandbox0.apispec.models.sandbox_update_request import SandboxUpdateRequest
from sandbox0.apispec.models.tpl_sandbox_network_policy import TplSandboxNetworkPolicy
from sandbox0.apispec.models.tpl_sandbox_network_policy_mode import TplSandboxNetworkPolicyMode
from sandbox0.apispec.models.webhook_config import WebhookConfig
from sandbox0.sessions import SandboxSession

from tests.e2e.helpers import claim_sandbox, close_client, new_client, require_config


class TestSandboxes(unittest.TestCase):
    def test_sandbox_lifecycle(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        env_vars = SandboxConfigEnvVars()
        env_vars.additional_properties["SDK_PY_E2E"] = "true"
        config = SandboxConfig(
            env_vars=env_vars,
            ttl=300,
            hard_ttl=600,
            auto_resume=True,
            network=TplSandboxNetworkPolicy(mode=TplSandboxNetworkPolicyMode.ALLOW_ALL),
            webhook=WebhookConfig(url="https://example.com/webhook", secret="secret", watch_dir="/workspace"),
        )

        sandbox = claim_sandbox(self, client, cfg, config=config)

        fetched = client.sandboxes.get(sandbox.id)
        self.assertEqual(fetched.id, sandbox.id)

        status = client.sandboxes.status(sandbox.id)
        self.assertEqual(status.sandbox_id, sandbox.id)

        updated = client.sandboxes.update(
            sandbox.id,
            SandboxUpdateRequest(config=SandboxUpdateConfig(auto_resume=False)),
        )
        self.assertFalse(updated.auto_resume)

        paused = client.sandboxes.pause(sandbox.id)
        self.assertTrue(paused.paused)

        resumed = client.sandboxes.resume(sandbox.id)
        self.assertTrue(resumed.resumed)

        refresh = client.sandboxes.refresh(sandbox.id)
        self.assertEqual(refresh.sandbox_id, sandbox.id)
        self.assertEqual(client.sandboxes.sandbox("sandbox-id").id, "sandbox-id")

    def test_sandbox_open_session(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        with client.sandboxes.open(cfg.template) as sandbox:
            self.assertTrue(sandbox.id)

        session = client.sandboxes.open(cfg.template)
        self.assertIsInstance(session, SandboxSession)
        sandbox = session.sandbox
        self.assertTrue(sandbox.id)
        session.close()

    def test_list_sandboxes(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)

        # Create a sandbox to ensure there's at least one
        sandbox = claim_sandbox(self, client, cfg)

        # Test list via client method
        sandboxes = client.list_sandboxes(
            status=GetApiV1SandboxesStatus.RUNNING,
            limit=10,
        )
        self.assertIsInstance(sandboxes, list)
        self.assertGreater(len(sandboxes), 0)
        found = any(sb.id == sandbox.id for sb in sandboxes)
        self.assertTrue(found, f"Sandbox {sandbox.id} not found in list")

        # Test list via sandboxes resource
        sandboxes2 = client.sandboxes.list(
            status="running",
            template_id=cfg.template,
            limit=10,
        )
        self.assertIsInstance(sandboxes2, list)
        self.assertGreater(len(sandboxes2), 0)
        found2 = any(sb.id == sandbox.id for sb in sandboxes2)
        self.assertTrue(found2, f"Sandbox {sandbox.id} not found in resource list")

        # Test with paused filter (should not include running sandbox)
        sandboxes3 = client.list_sandboxes(paused=True, limit=10)
        self.assertIsInstance(sandboxes3, list)
        found3 = any(sb.id == sandbox.id for sb in sandboxes3)
        self.assertFalse(found3, f"Running sandbox {sandbox.id} should not be in paused list")
