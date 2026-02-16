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

## Examples

Runnable examples are available in the `examples/` directory:

| Example                    | Description                              |
|----------------------------|------------------------------------------|
| `01_hello_world`           | Basic sandbox usage                      |
| `02_context_options`       | Context configuration options            |
| `03_files`                 | File read/write/list operations          |
| `04_streaming`             | Streaming execution output               |
| `05_templates`             | Working with sandbox templates           |
| `06_volumes`               | Persistent volumes and snapshots         |
| `07_webhook`               | Webhook event delivery                   |
| `08_network`               | Network policy configuration             |
| `09_expose_port`           | Exposing ports publicly                  |

Run an example:

```bash
cd examples/01_hello_world
SANDBOX0_TOKEN=your-token python main.py
```

## Links

- [Documentation](https://sandbox0.ai/docs)
- [API Reference](https://sandbox0.ai/docs/api)
- [GitHub Repository](https://github.com/sandbox0-ai/sdk-py)
- [PyPI Package](https://pypi.org/project/sandbox0/)

## License

Apache-2.0
