from __future__ import annotations

from sandbox0.apispec.models.network_egress_policy import NetworkEgressPolicy
from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.tpl_sandbox_network_policy import TplSandboxNetworkPolicy
from sandbox0.apispec.models.tpl_sandbox_network_policy_mode import TplSandboxNetworkPolicyMode

from examples.common import create_client


def main() -> None:
    client = create_client()
    sandbox = client.claim_sandbox(
        "default",
        config=SandboxConfig(
            hard_ttl=600,
            network=TplSandboxNetworkPolicy(mode=TplSandboxNetworkPolicyMode.ALLOW_ALL),
        ),
    )
    try:
        current = sandbox.get_network_policy()
        print(f"current policy: {current}")

        shell = '/bin/curl -s -o /dev/null -w "%{http_code}\\n" --max-time 3 https://github.com'
        print(sandbox.cmd(shell).output_raw, end="")

        sandbox.update_network_policy(TplSandboxNetworkPolicy(mode=TplSandboxNetworkPolicyMode.BLOCK_ALL))
        print(sandbox.cmd(shell).output_raw, end="")

        sandbox.update_network_policy(
            TplSandboxNetworkPolicy(
                mode=TplSandboxNetworkPolicyMode.BLOCK_ALL,
                egress=NetworkEgressPolicy(allowed_domains=["github.com"]),
            )
        )
        print(sandbox.cmd(shell).output_raw, end="")
    finally:
        client.delete_sandbox(sandbox.id)


if __name__ == "__main__":
    main()
