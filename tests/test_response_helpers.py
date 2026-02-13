from __future__ import annotations

from http import HTTPStatus
import unittest

from sandbox0.apispec.models.error import Error
from sandbox0.apispec.models.error_envelope import ErrorEnvelope
from sandbox0.apispec.models.success_message_response import SuccessMessageResponse
from sandbox0.apispec.types import Response
from sandbox0.errors import APIError
from sandbox0.response import ensure_model


class ResponseHelpersTest(unittest.TestCase):
    def test_ensure_model_returns_expected_type(self) -> None:
        response = Response(
            status_code=HTTPStatus.OK,
            content=b'{"success":true}',
            headers={},
            parsed=SuccessMessageResponse(success=True),
        )

        parsed = ensure_model(response, SuccessMessageResponse)
        self.assertIsInstance(parsed, SuccessMessageResponse)
        self.assertTrue(parsed.success)

    def test_ensure_model_raises_api_error_for_error_envelope(self) -> None:
        response = Response(
            status_code=HTTPStatus.BAD_REQUEST,
            content=b'{"success":false}',
            headers={"X-Request-Id": "req-123"},
            parsed=ErrorEnvelope(
                success=False,
                error=Error(code="bad_request", message="invalid input"),
            ),
        )

        with self.assertRaises(APIError) as ctx:
            ensure_model(response, SuccessMessageResponse)

        self.assertEqual(ctx.exception.status_code, 400)
        self.assertEqual(ctx.exception.code, "bad_request")
        self.assertEqual(ctx.exception.request_id, "req-123")


if __name__ == "__main__":
    unittest.main()
