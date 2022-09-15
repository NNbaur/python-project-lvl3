import os
import re
from urllib.parse import urlparse


def make_html_path(site: str, directory: str) -> str:
    clear_name = re.match(
        r'(^[\w]*://)?(.*)', site
    ).group(2)
    # Netloc without path
    if urlparse(site).path == '':
        format_name = re.sub(r'[\W_]', '-', clear_name) + '.html'
    # Reject file extension from url, create html name
    else:
        url = os.path.splitext(clear_name)[0]
        format_name = re.sub(r'[\W_]', '-', url) + '.html'
    path = os.path.join(directory, format_name)
    return path
