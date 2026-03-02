from __future__ import annotations

import hmac
from hashlib import sha256


def verify_webhook_signature(secret: str, payload: bytes, signature: str) -> bool:
    """Validate X-Sandbox0-Signature using HMAC-SHA256 over raw payload bytes."""
    normalized_signature = signature.strip()
    if not normalized_signature:
        return False

    try:
        provided = bytes.fromhex(normalized_signature)
    except ValueError:
        return False

    expected = hmac.new(secret.encode("utf-8"), payload, sha256).digest()
    return hmac.compare_digest(expected, provided)
