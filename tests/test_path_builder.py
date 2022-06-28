from page_loader.build_path.path_builder import make_html_path
from page_loader.build_path.path_dir import make_dir_path
from page_loader.build_path.path_file import make_file_path


def test_make_path_html():
    url1 = 'https://www.test.io/index.html'
    path = 'home/mydir'
    result1 = make_html_path(url1, path)
    exception1 = 'home/mydir/www-test-io-index.html'
    assert result1 == exception1
    url2 = 'test.io/index/try/one'
    result2 = make_html_path(url2, path)
    exception2 = 'home/mydir/test-io-index-try-one.html'
    assert result2 == exception2
    url3 = 'http://test.io/index/?page=2'
    result3 = make_html_path(url3, path)
    exception3 = 'home/mydir/test-io-index--page-2.html'
    assert result3 == exception3


def test_make_dir_path():
    url1 = 'https://www.test.io/index.html'
    path = 'home/mydir'
    result1 = make_dir_path(url1, path)
    exception1 = 'home/mydir/www-test-io-index_files'
    assert result1 == exception1
    url2 = 'test.io/index/try/one'
    result2 = make_dir_path(url2, path)
    exception2 = 'home/mydir/test-io-index-try-one_files'
    assert result2 == exception2
    url3 = 'http://test.io/index/?page=2'
    result3 = make_dir_path(url3, path)
    exception3 = 'home/mydir/test-io-index--page-2_files'
    assert result3 == exception3


def test_make_file_path():
    url1 = 'https://www.test.io/index.jpg'
    path = 'home/mydir'
    result1 = make_file_path(url1, path)
    exception1 = 'home/mydir/www-test-io-index.jpg'
    assert result1 == exception1
    url2 = 'test.io/index/try/one.svg'
    result2 = make_file_path(url2, path)
    exception2 = 'home/mydir/test-io-index-try-one.svg'
    assert result2 == exception2
    url3 = 'http://test.io/?page=2/lls.jpg.Sdx/ava.png'
    result3 = make_file_path(url3, path)
    exception3 = 'home/mydir/test-io--page-2-lls-jpg-Sdx-ava.png'
    assert result3 == exception3
