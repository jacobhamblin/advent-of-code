from lib import main


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_provided_examples():
    examples = [
        [['+1', '-2', '+3', '+1'], 3],
        [['+1', '+1', '+1'], 3],
        [['+1', '+1', '-2'], 0],
        [['-1', '-2', '-3'], -6],
    ]
    for example in examples:
        expect_equal(main.frequency_steps(example[0]), example[1])
