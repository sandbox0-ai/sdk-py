from __future__ import annotations

import sys
import threading
import time
from pathlib import Path

# Allow running examples directly without installing the package
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from sandbox0.apispec.models.sandbox_config import SandboxConfig

from examples.common import create_client


def main() -> None:
    client = create_client()
    with client.sandboxes.open("default", config=SandboxConfig(hard_ttl=300)) as sandbox:
        directory = "/tmp/sdk-py"
        path = f"{directory}/hello.txt"

        sandbox.mkdir(directory, recursive=True)
        print("directory created")

        sandbox.write_file(path, b"hello from file\n")
        print("file written")

        content = sandbox.read_file(path)
        print(f"file content: {content.decode('utf-8').strip()}")

        entries = sandbox.list_files(directory)
        print(f"dir entries: {len(entries)}")
        for entry in entries:
            file_path = "" if entry.path.__class__.__name__ == "Unset" else entry.path
            print(f"- {file_path}")

        # Watch one event.
        stream = sandbox.watch_files(directory, recursive=True)
        first_event = {}
        done = threading.Event()

        def _reader() -> None:
            try:
                for event in stream.iter_events():
                    first_event["event"] = event
                    break
            finally:
                done.set()

        thread = threading.Thread(target=_reader, daemon=True)
        thread.start()
        sandbox.write_file(path, b"hello from file\nsecond line\n")
        done.wait(timeout=5)
        if "event" in first_event:
            event = first_event["event"]
            print(f"watch event: type={event.type} path={event.path} event={event.event}")
        else:
            print("watch timeout")
        stream.unsubscribe()

        cmd_result = sandbox.cmd("cat /tmp/sdk-py/hello.txt")
        print(f"run output:\n{cmd_result.output_raw}", end="")
        time.sleep(0.1)


if __name__ == "__main__":
    main()
