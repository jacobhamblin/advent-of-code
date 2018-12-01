from lib import main


def expect_equal(first, second, message):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


