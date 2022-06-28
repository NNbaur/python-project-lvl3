import os
import re


def make_html_path(site: str, directory: str) -> str:
    clear_name = re.match(
        r'(^[\w]*://)?(.*)',
        site
    ).group(2)
    url, ext = os.path.splitext(clear_name)
    format_name = re.sub(r'[\W_]', '-', url) + '.html'
    path = os.path.join(directory, format_name)
    return path
