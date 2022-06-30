import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve
from page_loader.build_path.get_content import get_content
from page_loader.build_path.path_dir import make_dir_path
from page_loader.build_path.path_file import make_file_path


def download_files(html_path, site, directory):
    dir_path = make_dir_path(site, directory)
    os.mkdir(dir_path)
    site_domen = urlparse(site).netloc
    content = get_content(html_path)
    soup = BeautifulSoup(content, "html.parser")

    files = {'img': [], 'link': [], 'script': []}

    download_tag_files(
        soup, 'img', 'src', site_domen,
        site, dir_path, files
    )
    download_tag_files(
        soup, 'link', 'href', site_domen,
        site, dir_path, files
    )
    download_tag_files(
        soup, 'script', 'src', site_domen,
        site, dir_path, files
    )
    return files


def download_tag_files(soup, tag, attr, site_domen, site, dir_path, files):

    for link in soup.find_all(tag):
        url = link.get(attr)
        domen = urlparse(url).netloc

        if domen == site_domen or domen == '':
            full_url = urljoin(site, url)
            file_path = make_file_path(full_url, dir_path)
            files[tag].append(file_path)
            urlretrieve(full_url, file_path)
