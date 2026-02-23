import unittest

from sandbox0.apispec.models.create_cmd_context_request import CreateCMDContextRequest
from sandbox0.apispec.models.create_context_request import CreateContextRequest
from sandbox0.apispec.models.create_context_request_env_vars import CreateContextRequestEnvVars
from sandbox0.apispec.models.create_repl_context_request import CreateREPLContextRequest
from sandbox0.apispec.models.process_type import ProcessType
from sandbox0.apispec.models.pty_size import PTYSize

from tests.e2e.helpers import claim_sandbox, close_client, new_client, require_config


class TestSandboxContexts(unittest.TestCase):
    def test_context_operations(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        self.addCleanup(close_client, client)
        sandbox = claim_sandbox(self, client, cfg)

        env_vars = CreateContextRequestEnvVars()
        env_vars.additional_properties["SDK_PY_E2E_CTX"] = "true"

        repl_req = CreateContextRequest(
            type_=ProcessType.REPL,
            repl=CreateREPLContextRequest(alias="python"),
            pty_size=PTYSize(rows=24, cols=80),
            env_vars=env_vars,
            idle_timeout_sec=60,
            ttl_sec=120,
        )
        repl_ctx = sandbox.create_context(repl_req)
        self.assertTrue(repl_ctx.id)
        self.addCleanup(lambda: sandbox.delete_context(repl_ctx.id))

        contexts = sandbox.list_contexts()
        self.assertTrue(any(ctx.id == repl_ctx.id for ctx in contexts))

        fetched = sandbox.get_context(repl_ctx.id)
        self.assertEqual(fetched.id, repl_ctx.id)

        sandbox.context_input(repl_ctx.id, "print('hi')\n")
        sandbox.context_exec(repl_ctx.id, "print('exec')\n")
        sandbox.context_resize(repl_ctx.id, 40, 100)
        sandbox.context_signal(repl_ctx.id, "SIGINT")
        sandbox.context_stats(repl_ctx.id)
        sandbox.restart_context(repl_ctx.id)

        stream = sandbox.connect_ws_context(repl_ctx.id)
        stream.close()

        cmd_req = CreateContextRequest(
            type_=ProcessType.CMD,
            cmd=CreateCMDContextRequest(command=["/bin/sh", "-lc", "echo sdk-py-e2e"]),
            wait_until_done=True,
        )
        cmd_ctx = sandbox.create_context(cmd_req)
        self.assertTrue(cmd_ctx.id)
        self.addCleanup(lambda: sandbox.delete_context(cmd_ctx.id))
