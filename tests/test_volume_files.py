from __future__ import annotations

import tarfile
import unittest

from sandbox0.volume_files import upload_volume_directory


class _FakeHTTPClient:
    def __init__(self) -> None:
        self.request_body = b""

    def request(self, method: str, url: str, **kwargs):
        self.request_body = kwargs["content"].read()

        class Response:
            status_code = 200
            content = b'{"success":true,"data":{"files":1,"directories":1,"symlinks":1,"bytes":5}}'
            headers = {}

            def json(self):
                return {"success": True, "data": {"files": 1, "directories": 1, "symlinks": 1, "bytes": 5}}

        return Response()


class _FakeAPI:
    def __init__(self, http_client: _FakeHTTPClient) -> None:
        self._http_client = http_client

    def get_httpx_client(self) -> _FakeHTTPClient:
        return self._http_client


class _FakeClient:
    def __init__(self, http_client: _FakeHTTPClient) -> None:
        self.api = _FakeAPI(http_client)


class TestVolumeFiles(unittest.TestCase):
    def test_upload_volume_directory_packs_directory_tree(self) -> None:
        with self.subTest("directory tar"):
            import tempfile
            from pathlib import Path

            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                root = tmp_path / "dist"
                root.mkdir()
                nested = root / "assets"
                nested.mkdir()
                (nested / "hello.txt").write_bytes(b"hello")
                (nested / "link.txt").symlink_to("hello.txt")

                http_client = _FakeHTTPClient()
                summary = upload_volume_directory(_FakeClient(http_client), "vol_1", str(root), "/apps/current")

                self.assertEqual(summary.files, 1)
                self.assertEqual(summary.directories, 1)
                self.assertEqual(summary.symlinks, 1)
                self.assertEqual(summary.bytes_, 5)

                archive_path = tmp_path / "upload.tar"
                archive_path.write_bytes(http_client.request_body)
                with tarfile.open(archive_path) as archive:
                    names = archive.getnames()
                    self.assertIn("assets", names)
                    self.assertIn("assets/hello.txt", names)
                    self.assertIn("assets/link.txt", names)
                    link = archive.getmember("assets/link.txt")
                    self.assertTrue(link.issym())
                    self.assertEqual(link.linkname, "hello.txt")
