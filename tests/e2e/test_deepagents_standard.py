from __future__ import annotations

import unittest
from typing import Iterator

try:
    import pytest
    from langchain_tests.integration_tests import SandboxIntegrationTests
except ImportError as exc:  # pragma: no cover - exercised when dev deps are absent
    raise unittest.SkipTest("langchain-tests and pytest are required") from exc

from sandbox0_deepagents import Sandbox0DeepAgentsSandbox
from tests.e2e.helpers import close_client, load_e2e_config, new_client


class TestSandbox0DeepAgentsStandard(SandboxIntegrationTests):
    """LangChain standard tests for the Sandbox0 Deep Agents backend."""

    @classmethod
    @pytest.fixture(scope="class")
    def sandbox(cls) -> Iterator[Sandbox0DeepAgentsSandbox]:
        cfg = load_e2e_config()
        if cfg is None:
            pytest.skip("S0_E2E_BASE_URL or S0_E2E_PASSWORD not set")
        client = new_client(cfg)
        sandbox = client.sandboxes.claim("default")
        try:
            yield Sandbox0DeepAgentsSandbox(sandbox=sandbox)
        finally:
            try:
                client.sandboxes.delete(sandbox.id)
            finally:
                close_client(client)

    @pytest.mark.xfail(
        reason=(
            "langchain-tests 1.1.9 expects write() to reject existing files, "
            "while deepagents 0.7.0a2 BaseSandbox.write() is create-or-overwrite."
        ),
        strict=True,
    )
    def test_write_existing_file_fails(
        self,
        sandbox_backend,
        sandbox_test_root: str,
    ) -> None:
        super().test_write_existing_file_fails(sandbox_backend, sandbox_test_root)
