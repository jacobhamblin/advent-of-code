from lib import main


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_provided_examples():
    #  inputs
    #  '#1 @ 1,3: 4x4'
    #  '#2 @ 3,1: 4x4'
    #  '#3 @ 5,5: 2x2'
    strings = [
        [1, 1, 3, 4, 4],
        [2, 3, 1, 4, 4],
        [3, 5, 5, 2, 2],
    ]
    expect_equal(main.overlapping_square_count(strings), 4)


def test_provided_part_two():
    strings = [
        [1, 1, 3, 4, 4],
        [2, 3, 1, 4, 4],
        [3, 5, 5, 2, 2],
    ]
    expected_result = 3
    expect_equal(
        main.overlapping_square_count(strings, True),
        expected_result,
    )
