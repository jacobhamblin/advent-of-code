from lib import main


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_provided_examples():
    examples = []
    for example in examples:
        print(example)


def test_provided_part_two():
    examples = []
    for example in examples:
        print(example)
