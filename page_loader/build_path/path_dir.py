import re
import os
from urllib.parse import urlparse


def make_dir_path(site: str):

    if urlparse(site).scheme == '':
        site = f'https://{site}'
    clear_name = re.match(
        r'(^[\w]*://)?(.*)', site
    ).group(2)

    if urlparse(site).path == '':
        format_name = re.sub(r'[\W_]', '-', clear_name) + '_files'
    else:
        url = os.path.splitext(clear_name)[0]
        format_name = re.sub(r'[\W_]', '-', url) + '_files'
    return format_name
