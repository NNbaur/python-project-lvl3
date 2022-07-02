import logging
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.build_path.get_content import get_content


def update_html_urls(html_path: str, site: str, files: dict):
    tag_dict = {'img': 'src', 'link': 'href', 'script': 'src'}
    content = get_content(html_path)
    soup = BeautifulSoup(content, "html.parser")
    for tag, attr in tag_dict.items():
        rebase_url(soup, site, tag, attr, files)

    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    logging.debug('HTML updated')


def rebase_url(soup, site: str, tag: str, attr: str, files: dict):
    count = 0
    site_domen = urlparse(site).netloc

    if tag == 'script':
        lst = soup.find_all(tag, src=True)
    else:
        lst = soup.find_all(tag)
    lst_urls = filter_local_urls(site_domen, lst, attr)

    for new_url in lst_urls:
        new_url[attr] = files[tag][count]
        count += 1
    logging.debug('URL updated')


def filter_local_urls(site_domen: str, lst: list, attr: str) -> list:
    lst_urls = []

    for new_url in lst:
        domen = urlparse(new_url[attr]).netloc

        if domen == site_domen or domen == '':
            lst_urls.append(new_url)
    logging.debug('Only local resourses choosen')
    return lst_urls
