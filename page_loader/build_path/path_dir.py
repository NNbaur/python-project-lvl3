import re
import os
from urllib.parse import urlparse


def make_dir_path(site: str) -> str:
    # Add protocol to url
    if urlparse(site).scheme == '':
        site = f'https://{site}'
    clear_name = re.match(
        r'(^[\w]*://)?(.*)', site
    ).group(2)
    print(clear_name, 'hello')
    # Only netloc without path
    if urlparse(site).path == '':
        format_name = re.sub(r'[\W_]', '-', clear_name) + '_files'
        print(format_name)
    # Reject file extension in dirname
    else:
        url = os.path.splitext(clear_name)[0]
        print(url)
        format_name = re.sub(r'[\W_]', '-', url) + '_files'
    return format_name
