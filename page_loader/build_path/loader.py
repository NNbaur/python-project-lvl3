import requests
from page_loader.build_path.path_builder import make_html_path
from page_loader.build_path.get_images import download_images
from page_loader.build_path.update_img_urls import rebase_img_urls


def download(site: str, directory: str) -> str:
    path = make_html_path(site, directory)
    try:
        req = requests.get(site)
        content = req.text
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        img_urls = download_images(path, site, directory)
        rebase_img_urls(path, img_urls)
    except OSError:
        return 'Failed to connect. Check, that URL is correct'
    return path
