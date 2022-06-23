import requests
from page_loader.build_path.path_builder import make_path


def download(site: str, directory: str) -> str:
    path = make_path(site, directory)
    try:
        req = requests.get(site)
        content = req.text
        with open(path, 'w') as file:
            file.write(content)
    except OSError:
        print('Failed to connect. Check, that URL is correct')
    return path
