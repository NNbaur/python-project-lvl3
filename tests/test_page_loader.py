import tempfile
from page_loader.build_path.page_loader import download
import os


def test_download():
    url = 'https://requests.readthedocs.io/en/latest/user/install'
    with tempfile.TemporaryDirectory() as tmpdirname:
        path_to_download = tmpdirname
        full_path = download(url, path_to_download)
        assert os.path.exists(full_path)
        with open(full_path, 'r') as f1:
            result = f1.read()
    with open('tests/fixtures/result1.html', 'r') as f2:
        expected_res = f2.read()
    assert result == expected_res