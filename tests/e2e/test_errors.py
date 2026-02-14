import unittest

from sandbox0 import APIError


class TestErrors(unittest.TestCase):
    def test_api_error_string(self) -> None:
        err = APIError(status_code=400, code="bad_request", message="invalid input")
        self.assertIn("bad_request", str(err))
