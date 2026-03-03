import unittest

from sandbox0.apispec.models.pool_strategy import PoolStrategy


class TestPoolStrategy(unittest.TestCase):
    def test_from_dict_defaults_auto_scale_to_false_when_missing(self) -> None:
        pool = PoolStrategy.from_dict({"minIdle": 2, "maxIdle": 10})

        self.assertEqual(pool.min_idle, 2)
        self.assertEqual(pool.max_idle, 10)
        self.assertFalse(pool.auto_scale)


if __name__ == "__main__":
    unittest.main()
