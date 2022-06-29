import requests
from page_loader.build_path.path_builder import make_html_path
from page_loader.build_path.get_images import download_images
from page_loader.build_path.update_img_urls import rebase_img_urls
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
        img_urls = download_images(path, site, directory)
        rebase_img_urls(path, img_urls)
    except OSError:
        return 'Something goes wrong. Please, check url and path.'
    return path
