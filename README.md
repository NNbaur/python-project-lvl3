### Hexlet tests and linter status:
[![Actions Status](https://github.com/NNbaur/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/NNbaur/python-project-lvl3/actions) [![Actions Status](https://github.com/NNbaur/python-project-lvl3/actions/workflows/github-actions-project3.yml/badge.svg)](https://github.com/NNbaur/python-project-lvl3/actions) <a href="https://codeclimate.com/github/NNbaur/python-project-lvl3/maintainability"><img src="https://api.codeclimate.com/v1/badges/b34a94e5c22cad64295a/maintainability" /></a> <a href="https://codeclimate.com/github/NNbaur/python-project-lvl3/test_coverage"><img src="https://api.codeclimate.com/v1/badges/b34a94e5c22cad64295a/test_coverage" /></a>

### Description
______
PageLoader is a command line utility that downloads pages from the Internet and saves them to your computer.
Together with the page, it downloads all the resources (images, styles and js) making it possible to open the page without the Internet.
### How to install
______
```
pip install git+https://github.com/NNbaur/python-project-lvl3.git
```

or

```
$ git clone https://github.com/NNbaur/python-project-lvl3 
$ cd ProjectDirectory
$ make install
$ make build
$ make package-install
```
### Usage
______

#### As external library
```
from page_loader.build_path.loader import download

down = download(site, directory)

# directory: default - current directory
```
#### As CLI tool
```
page-loader [-h] [-o OUTPUT] site_adress

Page loader

positional arguments:
  site_adress

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        set directory path
```


How to work page-loader:

[![asciicast](https://asciinema.org/a/505097.svg)](https://asciinema.org/a/505097)