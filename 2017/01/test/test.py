from lib import main


def expect_equal(first, second, message):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_returns_int():
    matches = main.num_matches('54354')
    expect_equal(type(matches), int, 'Expected %s to be an %s')
    matches = main.num_matches('1231')
    expect_equal(type(matches), int, 'Expected %s to be an %s')
    matches = main.num_matches('')
    expect_equal(type(matches), int, 'Expected %s to be an %s')
