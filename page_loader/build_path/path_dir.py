import re
import os


def make_dir_path(site: str, directory: str):
    clear_name = re.match(
        r'(^[\w]*://)?(.*)',
        site
    ).group(2)
    url, ext = os.path.splitext(clear_name)
    format_name = re.sub(r'[\W_]', '-', url) + '_files'
    path = os.path.join(directory, format_name)
    return path
