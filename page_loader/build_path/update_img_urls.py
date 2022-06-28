from page_loader.build_path.get_content import get_content
from bs4 import BeautifulSoup


def rebase_img_urls(html_path: str, img_urls: list):
    content = get_content(html_path)
    soup = BeautifulSoup(content, "html.parser")
    img = soup.find_all('img')
    count = 0
    for new_url in img:
        new_url['src'] = img_urls[count]
        count += 1
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
