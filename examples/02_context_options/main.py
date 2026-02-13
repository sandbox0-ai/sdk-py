from __future__ import annotations

from sandbox0 import CmdOptions, RunOptions
from sandbox0.apispec.models.sandbox_config import SandboxConfig

from examples.common import create_client


def main() -> None:
    client = create_client()
    sandbox = client.claim_sandbox("default", config=SandboxConfig(hard_ttl=300))
    try:
        run_result = sandbox.run(
            "python",
            'import os, pathlib; print(pathlib.Path.cwd()); print(os.getenv("GREETING"))',
            options=RunOptions(
                cwd="/workspace",
                env_vars={"GREETING": "hello from repl"},
                ttl_sec=120,
                idle_timeout_sec=60,
            ),
        )
        print(run_result.output_raw, end="")

        cmd_result = sandbox.cmd(
            "bash -c 'echo $GREETING && pwd'",
            options=CmdOptions(
                cwd="/tmp",
                env_vars={"GREETING": "hello from cmd"},
                ttl_sec=120,
                idle_timeout_sec=60,
            ),
        )
        print(f"cmd output:\n{cmd_result.output_raw}", end="")
    finally:
        client.delete_sandbox(sandbox.id)


if __name__ == "__main__":
    main()
