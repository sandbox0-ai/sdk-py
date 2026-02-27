import unittest

from sandbox0.apispec.models.create_context_request import CreateContextRequest
from sandbox0.apispec.models.create_repl_context_request import CreateREPLContextRequest
from sandbox0.apispec.models.process_type import ProcessType
from sandbox0.sandbox import CmdOptions, RunOptions

from tests.e2e.helpers import claim_sandbox, close_client, new_client, require_config


class TestSandboxRun(unittest.TestCase):
    def test_run_and_cmd(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)
        sandbox = claim_sandbox(self, client, cfg)

        # Create a custom REPL context with specific settings
        custom_ctx = sandbox.create_context(
            request=CreateContextRequest(
                type_=ProcessType.REPL,
                repl=CreateREPLContextRequest(alias="python"),
                cwd="/tmp",
                env_vars={"SDK_PY_E2E": "true"},
                ttl_sec=120,
                idle_timeout_sec=60,
                pty_size={"rows": 24, "cols": 80},
            )
        )
        self.assertTrue(custom_ctx.id)

        # Run using the custom context
        run_result = sandbox.run(
            "python",
            "print('hello')\n",
            RunOptions(context_id=custom_ctx.id),
        )
        self.assertEqual(run_result.context_id, custom_ctx.id)

        # Reuse the context
        sandbox.run(
            "python",
            "print('reuse')\n",
            RunOptions(context_id=run_result.context_id),
        )

        # Cmd always creates a new context, so options work directly
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
