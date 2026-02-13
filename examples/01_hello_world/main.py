from __future__ import annotations

from sandbox0.apispec.models.sandbox_config import SandboxConfig

from examples.common import create_client


def main() -> None:
    client = create_client()
    sandbox = client.claim_sandbox("default", config=SandboxConfig(hard_ttl=300))
    try:
        run_result = sandbox.run("python", "x=2")
        print(run_result.output, end="")
        run_result = sandbox.run("python", "print(x)")
        print(run_result.output, end="")

        print('\nRunning command: /bin/sh -c "x=3"')
        sandbox.cmd('/bin/sh -c "x=3"')
        print('Running command: /bin/sh -c "echo $x"')
        cmd_result = sandbox.cmd('/bin/sh -c "echo $x"')
        print(cmd_result.output, end="")
    finally:
        client.delete_sandbox(sandbox.id)


if __name__ == "__main__":
    main()
