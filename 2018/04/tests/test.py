from lib import main


def expect_equal(first, second, message = 'Expected %s to be %s'):
    if first != second:
        first = str(first)
        second = str(second)
        raise Exception(message % (first, second))


def test_prep_input():
    input_block = '[1518-11-01 00:00] Guard #10 begins shift\n'\
        '[1518-11-01 00:05] falls asleep\n'\
        '[1518-11-01 00:25] wakes up\n'\
        '[1518-11-01 00:30] falls asleep\n'\
        '[1518-11-01 00:55] wakes up\n'\
        '[1518-11-01 23:58] Guard #99 begins shift\n'\
        '[1518-11-02 00:40] falls asleep\n'\
        '[1518-11-02 00:50] wakes up\n'\
        '[1518-11-03 00:05] Guard #10 begins shift\n'\
        '[1518-11-03 00:24] falls asleep\n'\
        '[1518-11-03 00:29] wakes up\n'\
        '[1518-11-04 00:02] Guard #99 begins shift\n'\
        '[1518-11-04 00:36] falls asleep\n'\
        '[1518-11-04 00:46] wakes up\n'\
        '[1518-11-05 00:03] Guard #99 begins shift\n'\
        '[1518-11-05 00:45] falls asleep\n'\
        '[1518-11-05 00:55] wakes up'
    prepped = main.prep_input(input_block.split('\n'))
    expect_equal(
        sorted([key for key in prepped]),
        ['11-1', '11-2', '11-3', '11-4', '11-5'],
    )
    entries = [
        prepped[day]['entries'] for day in prepped
    ]
    expect_equal(
        all(len(day_entries) % 2 == 0 for day_entries in entries),
        True,
    )


def test_provided_example_part_one():
    input_block = '[1518-11-01 00:00] Guard #10 begins shift\n'\
        '[1518-11-01 00:05] falls asleep\n'\
        '[1518-11-01 00:25] wakes up\n'\
        '[1518-11-01 00:30] falls asleep\n'\
        '[1518-11-01 00:55] wakes up\n'\
        '[1518-11-01 23:58] Guard #99 begins shift\n'\
        '[1518-11-02 00:40] falls asleep\n'\
        '[1518-11-02 00:50] wakes up\n'\
        '[1518-11-03 00:05] Guard #10 begins shift\n'\
        '[1518-11-03 00:24] falls asleep\n'\
        '[1518-11-03 00:29] wakes up\n'\
        '[1518-11-04 00:02] Guard #99 begins shift\n'\
        '[1518-11-04 00:36] falls asleep\n'\
        '[1518-11-04 00:46] wakes up\n'\
        '[1518-11-05 00:03] Guard #99 begins shift\n'\
        '[1518-11-05 00:45] falls asleep\n'\
        '[1518-11-05 00:55] wakes up'
    expect_equal(
        main.get_sleepiest_guard_checksum(input_block.split('\n')),
        10 * 24
    )


def test_provided_part_two():
    strings = [
    ]
    expect_equal(
        main.func(strings, True),
        expected_result,
    )
