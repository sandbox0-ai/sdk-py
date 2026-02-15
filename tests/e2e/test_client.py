import unittest

from sandbox0 import Client

from tests.e2e.helpers import close_client, e2e_token, require_config


class TestClient(unittest.TestCase):
    def test_client_options_and_api(self) -> None:
        cfg = require_config(self)
        token = e2e_token(cfg)

        client = Client(
            token=token,
            base_url=cfg.base_url,
            timeout=20.0,
            user_agent="sdk-py-e2e",
            headers={"X-SDK-E2E": "1"},
        )
        self.addCleanup(close_client, client)

        http_client = client.api.get_httpx_client()
        self.assertEqual(http_client.headers.get("User-Agent"), "sdk-py-e2e")
        self.assertEqual(http_client.headers.get("X-SDK-E2E"), "1")
        self.assertIn("Authorization", http_client.headers)

        sandbox = client.sandbox("sandbox-id")
        self.assertEqual(sandbox.id, "sandbox-id")

        ws_url = client.websocket_url("/api/v1/sandboxes")
        self.assertTrue(ws_url.startswith("ws"))
