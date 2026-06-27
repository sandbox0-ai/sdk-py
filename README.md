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
from sandbox0 import Client, CmdOptions

client = Client(token=os.environ["SANDBOX0_TOKEN"])

# Using context manager for automatic cleanup
with client.sandboxes.open("default") as sandbox:
    # Execute Python code (REPL - stateful)
    result = sandbox.run("python", "print('Hello, Sandbox0!')")
    print(result.output_raw, end="")
```

## CMD Streaming

```python
stream = sandbox.cmd_stream(
    "sh -c 'echo hello && echo warn >&2'",
    CmdOptions(command=["sh", "-c", "echo hello && echo warn >&2"]),
)

for output in stream.iter_outputs():
    print(output.data, end="")

done = stream.wait()
print(f"exit={done.exit_code} state={done.state}")
```

## OpenAI Agents SDK Sandbox

Install the optional adapter dependency:

```bash
pip install "sandbox0[openai-agents]"
```

Use `Sandbox0SandboxClient` anywhere the OpenAI Agents SDK expects a sandbox client:

```python
import os

from agents import Runner
from agents.run_config import RunConfig, SandboxRunConfig
from agents.sandbox import SandboxAgent

from sandbox0_openai_agents import Sandbox0SandboxClient, Sandbox0SandboxClientOptions

client = Sandbox0SandboxClient(
    token=os.environ["SANDBOX0_TOKEN"],
    base_url=os.environ.get("SANDBOX0_BASE_URL"),
)

sandbox_agent = SandboxAgent(
    name="demo",
    instructions="Use the sandbox for filesystem and command execution tasks.",
)

result = Runner.run_sync(
    sandbox_agent,
    "Create hello.txt in the sandbox, then print it.",
    run_config=RunConfig(
        sandbox=SandboxRunConfig(
            client=client,
            options=Sandbox0SandboxClientOptions(template="default"),
        ),
    ),
)
print(result.final_output)
```

The adapter keeps the OpenAI SDK workspace at `/workspace` on a Sandbox0
SandboxVolume. `delete()` releases the sandbox runtime and deletes the
workspace volume by default. Set `delete_volume_on_delete=False` when serialized
session state must resume the same workspace volume after cleanup. Use
`Sandbox0SandboxClientOptions(volume_snapshot_id="...")` for Sandbox0-native
volume snapshots; generic OpenAI SDK snapshot specs are not used by this
adapter.

## LangChain Deep Agents Sandbox

Install the optional Deep Agents adapter dependency:

```bash
pip install "sandbox0[deepagents]"
```

The package registers a Deep Agents Code sandbox provider named `sandbox0`, so
`dcode` can claim a Sandbox0 `default` template sandbox directly:

```bash
export SANDBOX0_TOKEN=...
dcode --sandbox sandbox0
```

For custom Deep Agents usage, wrap an existing Sandbox0 sandbox backend:

```python
import os
from sandbox0 import Client
from sandbox0_deepagents import Sandbox0DeepAgentsSandbox

client = Client(token=os.environ["SANDBOX0_TOKEN"])
sandbox = client.sandboxes.claim("default")
backend = Sandbox0DeepAgentsSandbox(sandbox=sandbox)

result = backend.execute("python3 - <<'PY'\nprint('hello')\nPY")
print(result.output)
```

## Documentation

- [Sandbox0 docs](https://sandbox0.ai/docs)
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
