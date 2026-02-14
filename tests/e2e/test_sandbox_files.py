import time
import unittest

from tests.e2e.helpers import claim_sandbox, new_client, require_config, wait_for_watch_event


class TestSandboxFiles(unittest.TestCase):
    def test_file_operations(self) -> None:
        cfg = require_config(self)
        client = new_client(cfg)
        sandbox = claim_sandbox(self, client, cfg)

        base_dir = f"/tmp/sdk-py-e2e-{time.time_ns()}"
        file_path = f"{base_dir}/hello.txt"
        moved_path = f"{base_dir}/moved.txt"

        sandbox.mkdir(base_dir, recursive=True)
        sandbox.write_file(file_path, b"hello e2e")
        sandbox.stat_file(file_path)
        self.assertEqual(sandbox.read_file(file_path), b"hello e2e")
        entries = sandbox.list_files(base_dir)
        self.assertTrue(any(entry.name == "hello.txt" for entry in entries))
        sandbox.move_file(file_path, moved_path)

        watch = sandbox.watch_files(base_dir, recursive=True)

        def _cleanup() -> None:
            try:
                watch.unsubscribe()
            except Exception:
                pass

        self.addCleanup(_cleanup)

        sandbox.write_file(f"{base_dir}/watch.txt", b"watch")

        event = wait_for_watch_event(watch, timeout_sec=10)
        self.assertIsNotNone(event, "timed out waiting for watch event")
        self.assertTrue(event.path)

        sandbox.delete_file(moved_path)
        sandbox.delete_file(base_dir)
