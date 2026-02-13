from __future__ import annotations

import unittest

from sandbox0.apispec.types import UNSET
from sandbox0.sandbox import Sandbox


class SandboxBuildersTest(unittest.TestCase):
    def test_build_env_vars_returns_unset_when_none(self) -> None:
        built = Sandbox._build_env_vars(None)
        self.assertIs(built, UNSET)

    def test_build_env_vars_copies_map_into_model(self) -> None:
        built = Sandbox._build_env_vars({"GREETING": "hello"})
        self.assertEqual(built.additional_properties, {"GREETING": "hello"})


if __name__ == "__main__":
    unittest.main()
