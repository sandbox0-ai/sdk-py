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

## Usage Windows

Usage windows are immutable, team-scoped usage records. Retain `next_cursor` to
incrementally import only newly recorded windows:

```python
page = client.list_usage_windows(
    cursor=saved_cursor,
    limit=250,
    window_type="sandbox.runtime_mib_milliseconds",
)

for window in page.windows:
    print(window.window_id, window.value, window.unit)

saved_cursor = page.next_cursor
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

The adapter keeps the OpenAI SDK workspace at `/workspace` in the Sandbox0
root filesystem. It can create a rootfs snapshot when a session stops and use
that snapshot when a replacement sandbox is needed.

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

## Create A Template From A Sandbox

Capture the current root filesystem of an existing sandbox into a new template:

```python
from sandbox0 import CreateTemplateFromSandboxOptions
from sandbox0.apispec.models.template_from_sandbox_create_request import (
    TemplateFromSandboxCreateRequest,
)
from sandbox0.apispec.models.template_from_sandbox_spec_overrides import (
    TemplateFromSandboxSpecOverrides,
)

template = client.create_template_from_sandbox(
    TemplateFromSandboxCreateRequest(
        template_id="python-ready",
        sandbox_id=sandbox.id,
        spec_overrides=TemplateFromSandboxSpecOverrides(
            display_name="Python Ready",
            tags=["python"],
        ),
    ),
    CreateTemplateFromSandboxOptions(
        idempotency_key="python-ready-v1",
        wait=True,
        timeout_sec=600,
    ),
)

print(template.template_id, template.status.creation.state)
```

Without `wait=True`, creation returns as soon as Sandbox0 accepts the request.
The rootfs capture point is `status.creation.captured_at`, not request
acceptance, so keep the source sandbox available until capture completes. A
running source is briefly write-barriered and remains running afterward. Call
`client.wait_template_ready("python-ready")` to wait later. A client-side
timeout or interruption stops local waiting but does not cancel creation of the
immutable RootFS base on the server.

## Links

- [Documentation](https://sandbox0.ai/docs)
- [API Reference](https://sandbox0.ai/docs/api)
- [GitHub Repository](https://github.com/sandbox0-ai/sdk-py)
- [PyPI Package](https://pypi.org/project/sandbox0/)

## License

Apache-2.0
