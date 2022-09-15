import re
import os


def make_file_path(site: str, dir_path: str) -> str:
    full_name = re.match(
        r'(^[\w]*://)?(.*)',
        site
    )
    clear_name = full_name.group(2)
    url, ext = os.path.splitext(clear_name)
    # Add file extension
    ext = '.html' if ext == '' else ext
    format_name = re.sub(r'[\W_]', '-', url) + ext
    path = os.path.join(dir_path, format_name)
    return path
