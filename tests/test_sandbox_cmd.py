from unittest import TestCase

from sandbox0.apispec.models.context_response import ContextResponse
from sandbox0.apispec.models.process_type import ProcessType
from sandbox0.sandbox import CmdOptions, Sandbox


class TestSandboxCmd(TestCase):
    def test_cmd_result_exposes_split_output(self) -> None:
        sandbox = Sandbox(id="sb_123", client=object())
        captured = {}

        def fake_create_context(request):
            captured["request"] = request
            return ContextResponse(
                id="ctx_123",
                type_=ProcessType.CMD,
                running=False,
                paused=False,
                created_at="2026-06-22T00:00:00Z",
                output_raw="outerr",
                stdout="out",
                stderr="err",
                exit_code=7,
                state="crashed",
            )

        sandbox.create_context = fake_create_context  # type: ignore[method-assign]

        result = sandbox.cmd("ignored", CmdOptions(command=["/bin/sh", "-c", "printf out; printf err >&2; exit 7"]))

        self.assertEqual(result.sandbox_id, "sb_123")
        self.assertEqual(result.context_id, "ctx_123")
        self.assertEqual(result.output_raw, "outerr")
        self.assertEqual(result.stdout, "out")
        self.assertEqual(result.stderr, "err")
        self.assertEqual(result.exit_code, 7)
        self.assertEqual(result.state, "crashed")
        self.assertEqual(captured["request"].cmd.command, ["/bin/sh", "-c", "printf out; printf err >&2; exit 7"])
        self.assertIs(captured["request"].wait_until_done, True)
