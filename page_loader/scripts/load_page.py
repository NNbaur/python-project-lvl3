import argparse
import os
from page_loader.build_path.page_loader import download


def main():
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


if __name__ == '__main__':
    main()
