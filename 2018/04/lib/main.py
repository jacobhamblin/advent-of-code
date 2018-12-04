import re
import sys
import datetime


def move_to_midnight(date_time):
    if date_time.hour == 23:
        date_time += datetime.timedelta(minutes=(60-date_time.minute))
    return date_time


def prep_input(input_list):
    sort_func = lambda str: datetime.datetime.strptime(
        str[0:18],
        '[%Y-%m-%d %H:%M]'
    )
    input_list.sort(key=sort_func)
    date_log = {}
    for str in input_list:
        date_time = datetime.datetime.strptime(str[0:18], '[%Y-%m-%d %H:%M]')
        date_time = move_to_midnight(date_time)
        guard_id = None
        guard_id_matches = re.findall(r'#(\d+)\s', str)
        if len(guard_id_matches):
            guard_id = guard_id_matches[0]
        day = '%s-%s' % (date_time.month, date_time.day)
        entry = date_log.get(day, {'entries': []})
        if guard_id:
            entry['guard_id'] = guard_id
        else:
            entry['entries'].append((60 * date_time.hour) + date_time.minute)
        date_log[day] = entry
    return date_log


def guard_shift_reports(input):
    time_cards = {}
    #  time_cards[id] = []
    #  each array in time_cards[id] will have 60 boolean values
    return time_cards


def get_sleepiest_guard(time_cards):
    #  for guard_id in time_cards:
    return time_cards


def main():
    if len(sys.argv) < 2:
        print('missing input file')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('too many arguments')
        sys.exit(1)

    f = open(sys.argv[1],"r")
    contents = f.read().strip()
    contents_list = contents.split('\n')
    print(prep_input(contents_list))
    f.close()
    #  print(func(contents_list))
    sys.exit(0)


if __name__ == "__main__":
    main()
