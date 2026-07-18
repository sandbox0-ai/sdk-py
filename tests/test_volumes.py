from datetime import datetime, timezone
from unittest import TestCase

from sandbox0.apispec.models.sandbox_volume import SandboxVolume


class TestVolumes(TestCase):
    def test_metered_storage_round_trips(self) -> None:
        volume = SandboxVolume.from_dict(
            {
                "id": "vol_123",
                "team_id": "team_123",
                "user_id": "user_123",
                "backend": "s0fs",
                "metered_storage_bytes": 8_734_523_392,
                "storage_observed_at": "2026-07-18T08:30:00Z",
                "created_at": "2026-07-18T08:00:00Z",
                "updated_at": "2026-07-18T08:30:00Z",
            }
        )

        self.assertEqual(volume.metered_storage_bytes, 8_734_523_392)
        self.assertEqual(
            volume.storage_observed_at,
            datetime(2026, 7, 18, 8, 30, tzinfo=timezone.utc),
        )
        self.assertEqual(
            volume.to_dict()["storage_observed_at"],
            "2026-07-18T08:30:00+00:00",
        )

    def test_metered_storage_preserves_explicit_null(self) -> None:
        volume = SandboxVolume.from_dict(
            {
                "id": "vol_s3",
                "team_id": "team_123",
                "user_id": "user_123",
                "backend": "s3",
                "metered_storage_bytes": None,
                "storage_observed_at": None,
                "created_at": "2026-07-18T08:00:00Z",
                "updated_at": "2026-07-18T08:30:00Z",
            }
        )

        self.assertIsNone(volume.metered_storage_bytes)
        self.assertIsNone(volume.storage_observed_at)
        self.assertIsNone(volume.to_dict()["metered_storage_bytes"])
        self.assertIsNone(volume.to_dict()["storage_observed_at"])
