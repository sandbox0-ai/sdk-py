from __future__ import annotations

import json
import unittest

import httpx

from sandbox0.response_normalize import normalize_response_json


class ResponseNormalizeTest(unittest.TestCase):
    def test_normalize_null_map_and_array_keys(self) -> None:
        response = httpx.Response(
            status_code=201,
            headers={"content-type": "application/json"},
            content=json.dumps(
                {
                    "success": True,
                    "data": {
                        "env_vars": None,
                        "contexts": None,
                    },
                }
            ).encode("utf-8"),
        )

        normalize_response_json(response)
        payload = response.json()
        self.assertEqual(payload["data"]["env_vars"], {})
        self.assertEqual(payload["data"]["contexts"], [])

    def test_normalize_null_values_inside_known_map(self) -> None:
        response = httpx.Response(
            status_code=200,
            headers={"content-type": "application/json"},
            content=json.dumps(
                {
                    "data": {
                        "env_vars": {
                            "TOKEN": None,
                            "NAME": "ok",
                        }
                    }
                }
            ).encode("utf-8"),
        )

        normalize_response_json(response)
        payload = response.json()
        self.assertEqual(payload["data"]["env_vars"]["TOKEN"], "")
        self.assertEqual(payload["data"]["env_vars"]["NAME"], "ok")


if __name__ == "__main__":
    unittest.main()
