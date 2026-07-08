import unittest
from http import HTTPStatus

from sandbox0 import APIError, CLAIM_START_THROTTLED_CODE, is_claim_start_throttled
from sandbox0.apispec.models.error import Error
from sandbox0.apispec.models.error_envelope import ErrorEnvelope
from sandbox0.apispec.models.success_sandbox_response import SuccessSandboxResponse
from sandbox0.apispec.types import Response
from sandbox0.response import ensure_data


class TestErrors(unittest.TestCase):
    def test_api_error_string(self) -> None:
        err = APIError(status_code=400, code="bad_request", message="invalid input")
        self.assertIn("bad_request", str(err))

    def test_claim_start_throttled_helper(self) -> None:
        err = APIError(
            status_code=429,
            code=CLAIM_START_THROTTLED_CODE,
            message="Claim/start admission is throttled",
            retry_after=4,
        )

        self.assertTrue(err.is_claim_start_throttled())
        self.assertTrue(is_claim_start_throttled(err))
        self.assertEqual(err.retry_after, 4)

    def test_retry_after_from_error_response(self) -> None:
        response = Response(
            status_code=HTTPStatus.TOO_MANY_REQUESTS,
            content=b"",
            headers={"Retry-After": "4"},
            parsed=ErrorEnvelope(
                success=False,
                error=Error(
                    code=CLAIM_START_THROTTLED_CODE,
                    message="Claim/start admission is throttled",
                ),
            ),
        )

        with self.assertRaises(APIError) as raised:
            ensure_data(response, SuccessSandboxResponse)

        err = raised.exception
        self.assertTrue(is_claim_start_throttled(err))
        self.assertEqual(err.retry_after, 4)
