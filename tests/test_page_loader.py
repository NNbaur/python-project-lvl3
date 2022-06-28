import os
import tempfile
from bs4 import BeautifulSoup
from page_loader.build_path.loader import download
from page_loader.build_path.get_content import get_content
from page_loader.build_path.get_images import download_images
from page_loader.build_path.update_img_urls import rebase_img_urls


def test_download():
    url = 'https://www.wikipedia.org'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = download(url, tmpdirname)
        assert os.path.exists(full_path)
    error_url = 'https://www.wikipsxedia.org'
    error_message = 'Failed to connect. Check, that URL is correct'
    with tempfile.TemporaryDirectory() as tmpdirname:
        download(error_url, tmpdirname)
        assert error_message



def test_content_html():
    url = 'https://www.wikipedia.org'
    exp_content = get_content('tests/fixtures/result1.html')
    exp_res = BeautifulSoup(exp_content, "html.parser")
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = download(url, tmpdirname)
        content = get_content(path)
        result = BeautifulSoup(content, "html.parser")
        result.img['src'] = "result1_img/1.png"
    assert result == exp_res


def test_download_image():
    url = 'https://www.wikipedia.org'
    html_path = 'tests/fixtures/origin.html'
    with tempfile.TemporaryDirectory() as temp_dir:
        exp_image = download_images(html_path, url, temp_dir)
        file_path = exp_image[0]
        assert os.path.isfile(file_path)


def test_update_html():
    url = 'https://www.wikipedia.org'
    html_path = 'tests/fixtures/origin.html'
    content = get_content(html_path)
    soup = BeautifulSoup(content, "html.parser")
    with tempfile.TemporaryDirectory() as temp_dir:
        exp_image = download_images(html_path, url, temp_dir)
        path = os.path.join(temp_dir, 'test.html')
        with open(path, 'w', encoding='utf-8') as html_file:
            html_file.write(soup.prettify())
            rebase_img_urls(path, exp_image)
        updated = get_content(path)
        soup1 = BeautifulSoup(updated, 'html.parser')
        img = soup1.img
        result = img['src']
        exp_res = exp_image[0]
        assert result == exp_res

