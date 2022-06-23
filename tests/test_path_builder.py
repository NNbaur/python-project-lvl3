from page_loader.build_path.path_builder import make_path


def test_make_path():
    url1 = 'https://www.test.io/index.html'
    path = 'home/mydir'
    result1 = make_path(url1, path)
    exception1 = 'home/mydir/www-test-io-index.html'
    assert result1 == exception1
    url2 = 'test.io/index/try/one'
    result2 = make_path(url2, path)
    exception2 = 'home/mydir/test-io-index-try-one.html'
    assert result2 == exception2
    url3 = 'http://test.io/index/?page=2'
    result3 = make_path(url3, path)
    exception3 = 'home/mydir/test-io-index--page-2.html'
    assert result3 == exception3

