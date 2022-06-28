import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve
from page_loader.build_path.get_content import get_content
from page_loader.build_path.path_dir import make_dir_path
from page_loader.build_path.path_file import make_file_path


def download_images(html_path, site, directory):
    content = get_content(html_path)
    soup = BeautifulSoup(content, "html.parser")
    dir_path = make_dir_path(site, directory)
    os.mkdir(dir_path)
    img_urls = []
    for link in soup.find_all('img'):
        url = link.get('src')
        full_url = urljoin(site, url)
        file_path = make_file_path(full_url, dir_path)
        img_urls.append(file_path)
        urlretrieve(full_url, file_path)
    return img_urls
