import logging
import requests
from urllib.parse import urlparse
from page_loader.build_path.myexception import KnownError
from page_loader.build_path.get_files import download_files
from page_loader.build_path.path_builder import make_html_path
from page_loader.build_path.update_html import update_html_urls


def download(site: str, directory: str) -> str:
    FORMAT = "%(asctime)s - %(levelname)s" \
             "- %(funcName)s: %(lineno)d - %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    if urlparse(site).scheme == '':
        site = f'https://{site}'
    path = make_html_path(site, directory)

    try:
        req = requests.get(site)
        req.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.debug(e)
        logging.error('Connection problem. Check that url is correct')
        raise KnownError('Error. Check log.') from e
    logging.debug('Connection established')
    content = req.text
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
    urls = download_files(path, site, directory)
    update_html_urls(path, site, urls)
    return path
