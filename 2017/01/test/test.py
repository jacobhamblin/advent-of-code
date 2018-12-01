from lib import main


def expect_equal(first, second, message):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_returns_int():
    matches = main.sum_matches('54354')
    expect_equal(type(matches), int, 'Expected %s to be an %s')
    matches = main.sum_matches('1231')
    expect_equal(type(matches), int, 'Expected %s to be an %s')
    matches = main.sum_matches('')
    expect_equal(type(matches), int, 'Expected %s to be an %s')


def test_matches_one_digit():
    matches = main.sum_matches('3')
    expect_equal(matches, 3, 'Expected %s to be %s')
    matches = main.sum_matches('9')
    expect_equal(matches, 9, 'Expected %s to be %s')


def test_matches_consecutive():
    matches = main.sum_matches('2233')
    expect_equal(matches, 5, 'Expected %s to be %s')
    matches = main.sum_matches('2443')
    expect_equal(matches, 4, 'Expected %s to be %s')
    matches = main.sum_matches('244443')
    expect_equal(matches, 12, 'Expected %s to be %s')


def test_matches_circular():
    matches = main.sum_matches('2233')
    expect_equal(matches, 5, 'Expected %s to be %s')
    matches = main.sum_matches('11')
    expect_equal(matches, 2, 'Expected %s to be %s')
    matches = main.sum_matches('1221')
    expect_equal(matches, 3, 'Expected %s to be %s')
    matches = main.sum_matches('4567')
    expect_equal(matches, 0, 'Expected %s to be %s')
