# Sandbox0 Python SDK

The official Python SDK for Sandbox0, with typed models and ergonomic high-level APIs.

## Installation

```bash
pip3 install sandbox0
```

## Environment Variables

- `SANDBOX0_TOKEN`: required
- `SANDBOX0_BASE_URL`: optional, defaults to `https://api.sandbox0.ai`

## Quick Start

```python
from sandbox0 import Client

client = Client(token="your-token")
sandbox = client.claim_sandbox("default")
try:
    result = sandbox.run("python", "print('hello sandbox0')")
    print(result.output_raw)
finally:
    client.delete_sandbox(sandbox.id)
```

## Core Capabilities

- Sandbox lifecycle: `claim_sandbox`, `get_sandbox`, `pause_sandbox`, `resume_sandbox`, `delete_sandbox`
- REPL/CMD execution: `sandbox.run()`, `sandbox.cmd()`, `sandbox.run_stream()`, `sandbox.cmd_stream()`
- File operations: `read_file`, `write_file`, `list_files`, `move_file`, `watch_files`
- Volumes and snapshots: `create_volume`, `mount`, `create_volume_snapshot`, `restore_volume_snapshot`
- Network policy: `get_network_policy`, `update_network_policy`
- Public exposed ports: `expose_port`, `get_exposed_ports`

## Examples

Runnable examples are available in `examples/`:

- `examples/01_hello_world/main.py`
- `examples/03_files/main.py`
- `examples/04_streaming/main.py`
- `examples/06_volumes/main.py`
- `examples/08_network/main.py`
- `examples/09_expose_port/main.py`
