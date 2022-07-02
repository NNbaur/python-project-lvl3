import os
import logging
import requests
from progress.bar import FillingSquaresBar
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from page_loader.build_path.myexception import KnownError
from page_loader.build_path.path_dir import make_dir_path
from page_loader.build_path.get_content import get_content
from page_loader.build_path.path_file import make_file_path


def download_files(html_path, site, directory):
    dir_path_rel = make_dir_path(site)
    dir_path_full = os.path.join(directory, dir_path_rel)
    try:
        os.mkdir(dir_path_full)
    except OSError as e:
        logging.debug(e)
        logging.error('Error. This directory already exists.')
        raise KnownError('Error. Check log!') from e
    logging.debug('Directory created')
    site_domen = urlparse(site).netloc
    content = get_content(html_path)
    soup = BeautifulSoup(content, "html.parser")

    tag_dict = {'img': 'src', 'link': 'href', 'script': 'src'}
    files = {'img': [], 'link': [], 'script': []}
    with FillingSquaresBar('Downloading...', max=len(files)) as progbar:
        for tag, attr in tag_dict.items():
            download_tag_files(
                soup, tag, attr, site_domen,
                site, dir_path_rel, dir_path_full, files
            )
            progbar.next()
    logging.debug('All files downloaded')
    return files


def download_tag_files(
        soup, tag, attr, site_domen,
        site, dir_path_rel, dir_path_full, files
):

    for link in soup.find_all(tag):
        url = link.get(attr)
        domen = urlparse(url).netloc

        if domen == site_domen or domen == '':
            full_url = urljoin(site, url)
            file_path_rel = make_file_path(full_url, dir_path_rel)
            file_path_full = make_file_path(full_url, dir_path_full)
            files[tag].append(file_path_rel)
            try:
                req = requests.get(full_url)
                req.raise_for_status()
            except requests.exceptions.RequestException as e:
                logging.debug(e)
                logging.error('Connection problem. Check that url is correct')
                raise KnownError('Error. Check log.') from e
            content = req.content
            with open(file_path_full, 'wb') as f:
                f.write(content)
    logging.debug(f'Files from tags {tag} downloaded')
