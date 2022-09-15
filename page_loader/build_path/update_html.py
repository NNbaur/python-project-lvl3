import logging
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.build_path.get_content import get_content
from typing import NoReturn, Type


def update_html_urls(html_path: str, site: str, files: dict) -> NoReturn:
    tag_dict = {'img': 'src', 'link': 'href', 'script': 'src'}
    content = get_content(html_path)
    soup = BeautifulSoup(content, "html.parser")
    # Replace old global links by new local links
    for tag, attr in tag_dict.items():
        rebase_url(soup, site, tag, attr, files)
    # Save changes
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    logging.debug('HTML updated')


def rebase_url(
        soup: Type[bs4.BeautifulSoup],
        site: str,
        tag: str,
        attr: str,
        files: dict) -> NoReturn:
    count = 0
    site_domen = urlparse(site).netloc
    # Only scripts with tag 'src', there are links
    if tag == 'script':
        lst = soup.find_all(tag, src=True)
    else:
        lst = soup.find_all(tag)
    # Take only local urls
    lst_urls = filter_local_urls(site_domen, lst, attr)
    # Replace old global links by new local links
    for new_url in lst_urls:
        new_url[attr] = files[tag][count]
        count += 1
    logging.debug('URL updated')


def filter_local_urls(site_domen: str, lst: list, attr: str) -> list:
    lst_urls = []

    # Choose only local links for this resource
    for new_url in lst:
        # Parse urls from links in html
        domen = urlparse(new_url[attr]).netloc
        # Take only relative links or full link with current resource
        if domen == site_domen or domen == '':
            lst_urls.append(new_url)
    logging.debug('Only local resourses choosen')
    return lst_urls
