from lib import main


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_provided_examples():
    strings = [
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabbcd',
        'abcdee',
        'ababab'
    ]
    expected_results = [
        [0,0],
        [1,1],
        [1,0],
        [0,1],
        [1,0],
        [1,0],
        [0,1],
    ]
    for index, str in enumerate(strings):
        expect_equal(
            main.has_pair_and_triplet(strings[index]),
            expected_results[index],
        )
    expect_equal(main.checksum(strings), 12)


def test_provided_part_two():
    strings = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz',
    ]
    expected_result = 'fgij'
    expect_equal(
        main.common_characters_best_match(strings),
        expected_result,
    )
