from lib import main


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_provided_examples():
    strings = [
    ]
    expected_results = [
    ]
    for index, str in enumerate(strings):
        expect_equal(
            main.func(strings[index]),
            expected_results[index],
        )
    expect_equal(main.checksum(strings), 12)


def test_provided_part_two():
    strings = [
    ]
    expected_result
    expect_equal(
        main.func(strings),
        expected_result,
    )
