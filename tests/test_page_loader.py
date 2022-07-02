import os
import pytest
import tempfile
from bs4 import BeautifulSoup
from page_loader.build_path.myexception import KnownError
from page_loader.build_path.loader import download
from page_loader.build_path.path_dir import make_dir_path
from page_loader.build_path.get_content import get_content
from page_loader.build_path.get_files import download_files
from page_loader.build_path.update_html import update_html_urls


def test_download():
    url = 'www.wikipedia.org'

    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = download(url, tmpdirname)
        assert os.path.exists(full_path)


def test_download_exception():
    with pytest.raises(KnownError) as e:
        error_url = 'https://www.wikipsxedia.org'
        with tempfile.TemporaryDirectory() as tmpdirname:
            download(error_url, tmpdirname)
    assert str(e.value) == 'Error. Check log.'


def test_content_html():
    url = 'https://www.wikipedia.org'
    exp_content = get_content('tests/fixtures/result1.html')
    exp_res = BeautifulSoup(exp_content, 'html.parser')

    with tempfile.TemporaryDirectory() as tmpdirname:
        path = download(url, tmpdirname)
        content = get_content(path)
        result = BeautifulSoup(content, 'html.parser')
        result.img['src'] = 'result1_files/img1.png'
        links = result.find_all('link')
        links[0]['href'] = 'result1_files/link1.png'
        links[1]['href'] = 'result1_files/link2.ico'
        scripts = result.find_all('script', src=True)
        scripts[0]['src'] = 'result1_files/script1.js'
        scripts[1]['src'] = 'result1_files/script2.js'
        assert result == exp_res


def test_download_files():
    url = 'https://www.wikipedia.org'
    html_path = 'tests/fixtures/origin.html'

    with tempfile.TemporaryDirectory() as temp_dir:
        exp_files = download_files(html_path, url, temp_dir)
        img_path = exp_files['img'][0]
        assert os.path.isfile(os.path.join(temp_dir, img_path))
        link_path = exp_files['link'][0]
        assert os.path.isfile(os.path.join(temp_dir, link_path))
        script_path = exp_files['script'][0]
        assert os.path.isfile(os.path.join(temp_dir, script_path))


def test_download_files_exception():
    with pytest.raises(KnownError) as a:
        url = 'https://www.wikipedia.org'
        html_path = 'tests/fixtures/origin.html'
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = make_dir_path(url)
            os.mkdir(os.path.join(temp_dir, dir_path))
            download_files(html_path, url, temp_dir)
    assert str(a.value) == 'Error. Check log!'


def test_update_html():
    url = 'https://www.wikipedia.org'
    html_path = 'tests/fixtures/origin.html'
    content = get_content(html_path)
    soup = BeautifulSoup(content, 'html.parser')

    with tempfile.TemporaryDirectory() as temp_dir:
        exp_files = download_files(html_path, url, temp_dir)
        path = os.path.join(temp_dir, 'test.html')

        with open(path, 'w', encoding='utf-8') as html_file:
            html_file.write(soup.prettify())
            update_html_urls(path, url, exp_files)
        updated = get_content(path)
        soup1 = BeautifulSoup(updated, 'html.parser')
        img = soup1.img
        result1 = img['src']
        exp_res1 = exp_files['img'][0]
        assert result1 == exp_res1
        link = soup1.link
        result2 = link['href']
        exp_res2 = exp_files['link'][0]
        assert result2 == exp_res2
        script = soup1.find('script', src=True)
        result3 = script['src']
        exp_res3 = exp_files['script'][0]
        assert result3 == exp_res3
