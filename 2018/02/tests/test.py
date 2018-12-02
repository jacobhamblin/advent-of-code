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
    examples = [
        [strings[0], [0,0]],
        [strings[1], [1,1]],
        [strings[2], [1,0]],
        [strings[3], [0,1]],
        [strings[4], [1,0]],
        [strings[5], [1,0]],
        [strings[6], [0,1]],
    ]
    for example in examples:
        expect_equal(main.has_pair_and_triplet(example[0]), example[1])


def test_provided_part_two():
    examples = []
    for example in examples:
        print(example)
