from __future__ import annotations

import os

from sandbox0.apispec.models.sandbox_config import SandboxConfig
from sandbox0.apispec.models.webhook_config import WebhookConfig

from examples.common import create_client, required_env


def main() -> None:
    webhook_url = required_env("SANDBOX0_WEBHOOK_URL")
    webhook_secret = os.getenv("SANDBOX0_WEBHOOK_SECRET", "")

    client = create_client()
    with client.sandboxes.open(
        "default",
        config=SandboxConfig(
            hard_ttl=300,
            webhook=WebhookConfig(
                url=webhook_url,
                secret=webhook_secret,
                watch_dir="/tmp33/webhook-demo",
            ),
        ),
    ) as sandbox:
        sandbox.run("bash", "echo webhook test")
        print("process started")

        client.sandboxes.pause(sandbox.id)
        print("sandbox paused")
        client.sandboxes.resume(sandbox.id)
        print("sandbox resumed")

        try:
            sandbox.cmd('/bin/sh -c "exit 2"')
        except Exception as err:
            print(f"expected command error: {err}")
        print("process crashed")

        base_dir = "/tmp33/webhook-demo"
        sandbox.mkdir(base_dir, recursive=True)
        sandbox.write_file(base_dir + "/file.txt", b"hello")
        sandbox.move_file(base_dir + "/file.txt", base_dir + "/file-renamed.txt")
        sandbox.cmd(f'/bin/sh -c "chmod 600 {base_dir}/file-renamed.txt"')
        sandbox.delete_file(base_dir + "/file-renamed.txt")
        print("file modified")


if __name__ == "__main__":
    main()
