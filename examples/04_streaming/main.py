from __future__ import annotations

import threading
import time

from sandbox0.apispec.models.sandbox_config import SandboxConfig

from examples.common import create_client


def main() -> None:
    client = create_client()
    with client.sandboxes.open("default", config=SandboxConfig(hard_ttl=300)) as sandbox:
        print("REPL stream:")
        repl_stream = sandbox.run_stream("python")
        repl_outputs = []

        def _repl_reader() -> None:
            for output in repl_stream.iter_outputs():
                repl_outputs.append(output.data)
                if len(repl_outputs) >= 2:
                    break

        repl_thread = threading.Thread(target=_repl_reader, daemon=True)
        repl_thread.start()
        repl_stream.send_input("print('hello from repl')")
        repl_stream.send_input("print(1 + 2)")
        repl_thread.join(timeout=3)
        repl_stream.close()
        for chunk in repl_outputs:
            print(chunk, end="")

        print("CMD stream:")
        cmd_stream = sandbox.cmd_stream('bash -c "for i in 1 2 3; do echo line-$i; done"')
        for output in cmd_stream.iter_outputs():
            print(output.data, end="")
        cmd_stream.close()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
