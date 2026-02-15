from __future__ import annotations

import threading
import time

from sandbox0.apispec.models.create_cmd_context_request import CreateCMDContextRequest
from sandbox0.apispec.models.create_context_request import CreateContextRequest
from sandbox0.apispec.models.create_repl_context_request import CreateREPLContextRequest
from sandbox0.apispec.models.process_type import ProcessType
from sandbox0.apispec.models.sandbox_config import SandboxConfig

from examples.common import create_client


def main() -> None:
    client = create_client()
    with client.sandboxes.open("default", config=SandboxConfig(hard_ttl=300)) as sandbox:
        # Example 1: REPL stream using create_context + connect_ws_context
        print("REPL stream:")
        repl_request = CreateContextRequest(
            type_=ProcessType.REPL,
            repl=CreateREPLContextRequest(language="python"),
        )
        repl_ctx = sandbox.create_context(request=repl_request)
        repl_stream = sandbox.connect_ws_context(repl_ctx.id)
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

        # Example 2: CMD stream using create_context + connect_ws_context
        print("CMD stream:")
        cmd_request = CreateContextRequest(
            type_=ProcessType.CMD,
            cmd=CreateCMDContextRequest(
                command=["bash", "-c", "for i in 1 2 3; do echo line-$i; done"]
            ),
            wait_until_done=False,
        )
        cmd_ctx = sandbox.create_context(request=cmd_request)
        cmd_stream = sandbox.connect_ws_context(cmd_ctx.id)
        for output in cmd_stream.iter_outputs():
            print(output.data, end="")
        cmd_stream.close()
        sandbox.delete_context(context_id=cmd_ctx.id)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
