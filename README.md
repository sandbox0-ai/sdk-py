# Sandbox0 Python SDK

The official Python SDK for Sandbox0, providing typed models and ergonomic high-level APIs for managing secure code execution sandboxes.

> This SDK remains open source. Current Sandbox0 runtime development is closed source.
> Sandbox0 Cloud is the supported service. Self-hosting is no longer supported.
> Bring Your Own Cloud (BYOC) is planned and is not available yet.
> See [deployment options](https://sandbox0.ai/docs/sandbox/deployment).

## Installation

```bash
pip install sandbox0
```

## Requirements

- Python 3.9 or later

## RootFS capacity

Template `resources.ephemeralStorage` sets the initial RootFS filesystem capacity
for image imports: the default is `8Gi`, and supported values are `300Mi` through
`1Ti`, aligned to 4096 bytes. On deployments with automatic growth enabled, XFS
expands online within the configured sparse-device ceiling while the sandbox's
processes continue running. Existing generations retain their committed geometry.

Persistent blocks reside in regional object storage. Compute nodes retain bounded
caches and write journals; slow or unavailable storage can apply write backpressure.
The initial size is distinct from stored data usage and service storage quotas.
Automatic growth requires operator enablement; see the
[deployment guide](https://github.com/sandbox0-ai/sandbox0/blob/main/deploy/nomad/rootfs-autogrow.md).

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

## Independent sandbox health (unreleased)

```python
# Configure Client(..., timeout=10.0) to bound network requests.
health = client.sandboxes.get_health(sandbox_id)
print(health.runtime.liveness.state, health.execution.state, health.terminal.state)
# Equivalent: client.get_sandbox_health(sandbox_id)
```

Generations remain exact integers and are validated against the API's int64 range.

Health is returned as separate runtime launch/liveness, execution, terminal,
and storage identity/writer/I/O observations. Each includes `state`, a fixed
`reason`, its evidence `source`, and the original observation time (null when
unobserved). Guest evidence is advisory. A storage identity or writer lease does
not prove current storage I/O; that check currently remains `unknown`.

The query may run bounded fixed guest diagnostics, but never resumes or restarts
a sandbox. Paused sandboxes and active lifecycle transitions skip those probes.
Unavailable guest diagnostics are a successful observation response, not an API
failure or a reason to retry a lifecycle mutation. This API requires a server
version with the health endpoint; SDKs do not fall back to guest commands.

## Links

- [Documentation](https://sandbox0.ai/docs)
- [API Reference](https://sandbox0.ai/docs/api)
- [GitHub Repository](https://github.com/sandbox0-ai/sdk-py)
- [PyPI Package](https://pypi.org/project/sandbox0/)

## License

Apache-2.0


Conditional session receipts can be read without auto-resume or process creation:
`sandbox.find_conditional_session(original_key, generation)`.
This uses the distinct `/sessions/conditional/lookup` route and checks the original
generation. Errors never fall back to ordinary lookup or creation. A missing
receipt does not authorize replay: an earlier create may still be in flight.
The result is process information, not credential/storage qualification or proof
that the process is still running when a later action begins.

### Conditional Session attachment

`sandbox.connect_conditional_session(session_id, key, generation, attempt_id, options)` opens the distinct `/sessions/{session_id}/conditional/ws` endpoint, bound to the original conditional creation key, runtime generation and attempt. It accepts the existing Session WebSocket replay options. Every control message is checked against that binding, and generation handover revokes the connection. Errors never trigger an ordinary attachment, retry or auto-resume. Closing the connection detaches without stopping the process. This is not lifecycle, storage or credential qualification.

### Reconnect an explicitly memory-restored original attempt

```python
session = sandbox.find_restored_conditional_session(original_key, current_generation, creation_generation)
connection = sandbox.connect_restored_conditional_session(session.id, original_key, current_generation, creation_generation, original_attempt_id, options)
```

Verify the external memory-restoration lineage and your owned credential/session
history first. These helpers explicitly send `creation_runtime_generation`, which
must precede the current generation. They require the original still-running
attempt and never create a session, restart an attempt, resume the sandbox or
retry through ordinary endpoints. Existing same-generation helpers remain strict.
The restored socket can replay the original attempt's earlier-generation events;
its controls are bound to the current generation and the original attempt ID.
A subsequent handover revokes the socket. Old gateways that discard the optional
origin cannot authorize a restored original creation and must return an error.

## Explicit snapshot recovery

Use `client.sandboxes.restore_snapshot(sandbox_id, expected_runtime_generation=7, snapshot_id=snapshot_id, snapshot_generation_id=snapshot_generation_id, discard_process_state=True, idempotency_key=request_key)` to explicitly end old processes and replace writable RootFS. Keep every field and the key after an uncertain reply. `find_snapshot_restore_operation` and `get_snapshot_restore_operation` observe the original operation without submitting work. Only `succeeded` proves fresh runtime launch; `restored_rootfs_generation_id` alone proves the head change committed.

The `get_snapshot_restore_final_capture`, `read_snapshot_restore_final_capture_file` and `acknowledge_snapshot_restore_final_capture` resource methods preserve stopped-source credential custody. Acknowledge only after durable encrypted owner commit. Helpers never retry, refresh coordinates or fall back to guest execution or disk-only memory recovery. Source and successor generations must fit the contract's safe integer range.

## Read original RootFS fork provenance

```python
receipt = client.sandboxes.get_rootfs_fork(
    source_sandbox_id, expected_runtime_generation=7, idempotency_key="original-fork",
)
```

Keep the original source sandbox, generation (including zero), key and
authenticated identity. This performs one GET and never retries or submits a
fork. Missing, conflicting and pending results remain errors; a 404 is not
proof of cancellation. The receipt requires the original unchanged, never-run
paused child and retained storage evidence. Memory forks are excluded. It is
not a credential-safety attestation or a state reservation; later mutations
need their own identity conditions.

## Conditional first launch of a RootFS fork

```python
original = dict(
    fork_operation_id=receipt.operation_id, filesystem_id=receipt.target_filesystem_id,
    head_generation_id=receipt.target_head_generation_id, writer_epoch=receipt.writer_epoch,
    idempotency_key="original-child-launch",
)  # Persist these conditions before submitting.
launch = client.sandboxes.launch_rootfs_fork(receipt.target_sandbox_id, **original)
observation = client.sandboxes.get_rootfs_fork_launch(
    receipt.target_sandbox_id, **original, expected_operation_id=launch.operation_id,
)
```

Each method sends exactly one request. After a lost reply, query with the same
original conditions and key, omitting `expected_operation_id` if no receipt was
received. Never refresh the original writer epoch or fall back to ordinary
resume. Completed history retains its digest and time even when `current` is
false after later lifecycle changes. `current` is an owner snapshot, not a live
lease, health check or credential authorization. Pending has no completion
proof; neither aborted nor 404 proves physical absence. Helpers validate the
returned identity and state-specific evidence and never poll or retry for you.
