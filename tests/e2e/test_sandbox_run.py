import unittest

from sandbox0.sandbox import CmdOptions, RunOptions

from tests.e2e.helpers import claim_sandbox, new_client, require_config


class TestSandboxRun(unittest.TestCase):
    def test_run_and_cmd(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        sandbox = claim_sandbox(self, client, cfg)

        run_result = sandbox.run(
            "python",
            "print('hello')\n",
            RunOptions(
                ttl_sec=120,
                idle_timeout_sec=60,
                cwd="/tmp",
                env_vars={"SDK_PY_E2E": "true"},
                pty_rows=24,
                pty_cols=80,
            ),
        )
        self.assertTrue(run_result.context_id)

        sandbox.run(
            "python",
            "print('reuse')\n",
            RunOptions(context_id=run_result.context_id),
        )

        cmd_result = sandbox.cmd(
            "echo hello",
            CmdOptions(
                command=["sh", "-c", "echo hello"],
                ttl_sec=120,
                idle_timeout_sec=60,
                cwd="/tmp",
                env_vars={"SDK_PY_E2E_CMD": "true"},
                pty_rows=24,
                pty_cols=80,
            ),
        )
        self.assertTrue(cmd_result.context_id)
