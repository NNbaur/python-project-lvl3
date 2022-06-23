import os
import re


def make_path(site: str, directory: str) -> str:
    # Build address name without scheme(http, https)
    clear_name = re.match(
        r'(^[\w]*://)?([\w.]*[/\w!@#$%^&*()_+=?]*)', site
    ).group(2)
    # Substitute symbols, besides letters and numbers in address name to '-'
    format_name = re.sub(r'[\W_]', '-', clear_name) + '.html'
    path = os.path.join(directory, format_name)
    return path
