import requests
from page_loader.build_path.path_builder import make_html_path
from page_loader.build_path.get_files import download_files
from page_loader.build_path.update_html import update_html_urls
from urllib.parse import urlparse


def download(site: str, directory: str) -> str:

    if urlparse(site).scheme == '':
        site = f'https://{site}'
    path = make_html_path(site, directory)

    try:
        req = requests.get(site)
        content = req.text

        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        urls = download_files(path, site, directory)
        update_html_urls(path, site, urls)

    except OSError:
        return 'Something goes wrong. Please, check url and path.'
    return path
