import hmac
import unittest
from hashlib import sha256

from sandbox0 import verify_webhook_signature


def sign_like_procd(secret: str, payload: bytes) -> str:
    return hmac.new(secret.encode("utf-8"), payload, sha256).hexdigest()


class TestWebhookSignature(unittest.TestCase):
    def test_verify_webhook_signature(self) -> None:
        secret = "sandbox0-webhook-secret"
        payload = b'{"event_id":"evt_1","event_type":"sandbox.ready","sandbox_id":"sb_1"}'
        valid_signature = sign_like_procd(secret, payload)

        self.assertTrue(verify_webhook_signature(secret, payload, valid_signature))
        self.assertTrue(verify_webhook_signature(secret, payload, valid_signature.upper()))
        self.assertFalse(verify_webhook_signature(secret, payload, sign_like_procd("wrong-secret", payload)))
        self.assertFalse(
            verify_webhook_signature(
                secret,
                b'{"event_id":"evt_1","event_type":"sandbox.killed","sandbox_id":"sb_1"}',
                valid_signature,
            )
        )
        self.assertFalse(verify_webhook_signature(secret, payload, "not-hex"))
        self.assertFalse(verify_webhook_signature(secret, payload, ""))


if __name__ == "__main__":
    unittest.main()
