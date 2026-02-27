from __future__ import annotations

import sys
from pathlib import Path

# Allow running examples directly without installing the package
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from sandbox0 import CmdOptions, RunOptions
from sandbox0.apispec.models.create_context_request import CreateContextRequest
from sandbox0.apispec.models.create_context_request_env_vars import CreateContextRequestEnvVars
from sandbox0.apispec.models.create_repl_context_request import CreateREPLContextRequest
from sandbox0.apispec.models.process_type import ProcessType
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.types import UNSET

from examples.common import create_client


def main() -> None:
    client = create_client()
    with client.sandboxes.open("default", config=SandboxConfig(hard_ttl=300)) as sandbox:
        # Create a custom REPL context with specific cwd, env vars, and TTL.
        # This is useful when you need fine-grained control over the context settings.
        custom_ctx = sandbox.create_context(
            request=CreateContextRequest(
                type_=ProcessType.REPL,
                repl=CreateREPLContextRequest(alias="python"),
                cwd="/workspace",
                env_vars=CreateContextRequestEnvVars.from_dict({"GREETING": "hello from repl"}),
                ttl_sec=120,
                idle_timeout_sec=60,
            )
        )
        print(f"Created context: {custom_ctx.id}")

        # Run using the custom context via context_id.
        run_result = sandbox.run(
            "python",
            'import os, pathlib; print(pathlib.Path.cwd()); print(os.getenv("GREETING"))',
            options=RunOptions(context_id=custom_ctx.id),
        )
        print(run_result.output_raw, end="")

        # Cmd always creates a new context, so options work directly.
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


if __name__ == "__main__":
    main()
