from unittest import TestCase

from sandbox0.apispec.models.refresh_response import RefreshResponse
from sandbox0.apispec.models.sandbox import Sandbox
from sandbox0.apispec.models.sandbox_summary import SandboxSummary


class TestSandboxExpirationDecoding(TestCase):
    def test_disabled_expirations_decode_as_none(self) -> None:
        timestamps = {
            "created_at": "2026-08-03T00:00:00Z",
            "updated_at": "2026-08-03T00:00:00Z",
            "expires_at": None,
            "hard_expires_at": None,
        }
        sandbox = Sandbox.from_dict(
            {
                "id": "sb_disabled_ttl",
                "template_id": "default",
                "team_id": "team_1",
                "status": "running",
                "paused": False,
                "auto_resume": True,
                "pod_name": "sandbox-pod",
                "runtime_generation": 1,
                "claimed_at": "2026-08-03T00:00:00Z",
                **timestamps,
            }
        )
        summary = SandboxSummary.from_dict(
            {
                "id": "sb_disabled_ttl",
                "template_id": "default",
                "status": "running",
                "paused": False,
                "runtime_generation": 1,
                **timestamps,
            }
        )
        refresh = RefreshResponse.from_dict(
            {
                "sandbox_id": "sb_disabled_ttl",
                "expires_at": None,
                "hard_expires_at": None,
            }
        )

        for value in (sandbox, summary, refresh):
            self.assertIsNone(value.expires_at)
            self.assertIsNone(value.hard_expires_at)
