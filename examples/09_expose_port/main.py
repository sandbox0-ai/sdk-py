from __future__ import annotations

import time

from sandbox0 import CmdOptions
from sandbox0.apispec.models.sandbox_config import SandboxConfig

from examples.common import create_client


def main() -> None:
    client = create_client()
    with client.sandboxes.open(
        "default",
        config=SandboxConfig(auto_resume=True),
    ) as sandbox:
        html = "<html><body><h1>Hello from Sandbox0!</h1></body></html>"
        sandbox.write_file("/tmp/index.html", html.encode("utf-8"))
        print("Uploaded index.html via file upload API")

        print("Starting web server on port 8080...")
        server_result = sandbox.cmd(
            "python3 -m http.server 8080 --directory /tmp",
            options=CmdOptions(wait=False),
        )
        print(f"Server started, context: {server_result.context_id}")

        time.sleep(2)

        print("Exposing port 8080...")
        ports = sandbox.expose_port(8080, True)
        print(f"Exposure domain: {ports.exposure_domain}")
        print("Exposed ports:")
        for port in ports.ports:
            print(f"  - Port: {port.port}, Resume: {port.resume}, PublicURL: {port.public_url}")

        print("Verifying server is running...")
        response = sandbox.cmd("curl -s http://localhost:8080/index.html")
        print(f"Server response:\n{response.output_raw}")

        all_ports = sandbox.get_exposed_ports()
        print("All exposed ports:")
        for port in all_ports.ports:
            print(f"  - Port: {port.port}, Resume: {port.resume}, PublicURL: {port.public_url}")


if __name__ == "__main__":
    main()
