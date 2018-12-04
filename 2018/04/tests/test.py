from lib import main


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_provided_examples():
    strings = [
    ]
    expect_equal(main.func(strings), 4)


def test_provided_part_two():
    strings = [
    ]
    expect_equal(
        main.func(strings, True),
        expected_result,
    )
