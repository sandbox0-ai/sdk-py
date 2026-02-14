import threading
import unittest

from sandbox0.sandbox import CmdOptions, RunOptions

from tests.e2e.helpers import claim_sandbox, new_client, require_config


def wait_for_stream_output(stream, timeout_sec: int = 10) -> bool:
    result = {"received": False, "error": None}

    def _worker() -> None:
        try:
            for output in stream.iter_outputs():
                if output.data or output.source:
                    result["received"] = True
                    return
        except Exception as exc:
            result["error"] = exc

    thread = threading.Thread(target=_worker, daemon=True)
    thread.start()
    thread.join(timeout_sec)
    if thread.is_alive():
        try:
            stream.close()
        except Exception:
            pass
        thread.join(1)
        return False
    if result["error"] is not None:
        raise result["error"]
    return result["received"]


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

    def test_streams(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        sandbox = claim_sandbox(self, client, cfg)

        run_stream = sandbox.run_stream("python")
        run_stream.send_input("print('stream')\n")
        received = wait_for_stream_output(run_stream, timeout_sec=15)
        try:
            run_stream.close()
        except Exception:
            pass
        self.assertTrue(received)

        cmd_stream = sandbox.cmd_stream("sh -c \"echo stream\"")
        received = wait_for_stream_output(cmd_stream, timeout_sec=15)
        try:
            cmd_stream.close()
        except Exception:
            pass
        self.assertTrue(received)
