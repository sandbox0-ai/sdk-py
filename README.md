# Sandbox0 Python SDK

The official Python SDK for Sandbox0, providing typed models and ergonomic high-level APIs for managing secure code execution sandboxes.

## Installation

```bash
pip install sandbox0
```

## Requirements

- Python 3.9 or later

## Configuration

| Environment Variable | Required | Default                   | Description          |
|---------------------|----------|---------------------------|----------------------|
| `SANDBOX0_TOKEN`    | Yes      | -                         | API authentication token |
| `SANDBOX0_BASE_URL` | No       | `https://api.sandbox0.ai` | API base URL         |

## Quick Start

```python
import os
from sandbox0 import Client

client = Client(token=os.environ["SANDBOX0_TOKEN"])

# Using context manager for automatic cleanup
with client.sandboxes.open("default") as sandbox:
    # Execute Python code (REPL - stateful)
    result = sandbox.run("python", "print('Hello, Sandbox0!')")
    print(result.output_raw, end="")
```

## Documentation

- [Sandbox0 docs](https://sandbox0.ai/docs)
- [Template sidecars and shared volumes](https://sandbox0.ai/docs/template/sidecars)
- [Volume mounts](https://sandbox0.ai/docs/volume/mounts)

## Bootstrap Mounts At Claim Time

```python
from sandbox0.apispec.models.claim_mount_request import ClaimMountRequest
from sandbox0.apispec.models.create_sandbox_volume_request import CreateSandboxVolumeRequest

volume = client.volumes.create(CreateSandboxVolumeRequest())

sandbox = client.sandboxes.claim(
    "default",
    mounts=[
        ClaimMountRequest(
            sandboxvolume_id=volume.id,
            mount_point="/workspace/data",
        )
    ],
    wait_for_mounts=True,
    mount_wait_timeout_ms=45000,
)

for mount in sandbox.bootstrap_mounts:
    print(mount.sandboxvolume_id, mount.state)
```

## Links

- [Documentation](https://sandbox0.ai/docs)
- [API Reference](https://sandbox0.ai/docs/api)
- [GitHub Repository](https://github.com/sandbox0-ai/sdk-py)
- [PyPI Package](https://pypi.org/project/sandbox0/)

## License

Apache-2.0
