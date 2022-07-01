import os
import sys
import argparse
from page_loader.build_path.loader import download
from page_loader.build_path.myexception import KnownError


def main():
    try:
        parser = argparse.ArgumentParser(description='Page loader')
        parser.add_argument(
            '-o',
            '--output',
            help='set directory path',
            default=os.getcwd()
        )
        parser.add_argument('site_adress', type=str)

        args = parser.parse_args()
        answer = download(
            args.site_adress,
            args.output
        )
        print(answer)
    except KnownError:
        sys.exit(1)


if __name__ == '__main__':
    main()
