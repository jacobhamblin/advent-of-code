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


def guard_timecards(date_log):
    guard_timecards = {}
    for day_str in date_log:
        day = date_log[day_str]
        existing_records = guard_timecards.get(day['guard_id'], [])
        new_record = [False] * 60
        i = 0;
        entries = day.get('entries')
        while i < len(entries):
            for minute in range(entries[i], entries[i + 1]):
                new_record[minute] = True
            i += 2
        existing_records.append(new_record)
        guard_timecards[day['guard_id']] = existing_records
    return guard_timecards


def get_most_common_sleepy_minute(shifts):
    best = {'minute': -1, 'count': 0}
    for i in xrange(0,60):
        count = 0
        for shift in shifts:
            if shift[i]:
                count += 1
        if count > best['count']:
            best['minute'] = i
            best['count'] = count
    return best['minute']


def get_sleepiest_guard_checksum(input_block):
    date_log = prep_input(input_block)
    timecards = guard_timecards(date_log)
    most_minutes = {'id': 0, 'minutes': 0, 'minute': -1}
    for guard_id in timecards:
        shift_reports = timecards[guard_id]
        total_minutes = 0
        for shift in shift_reports:
            total_minutes += sum(shift)
        if total_minutes > most_minutes['minutes']:
            most_minutes['id'] = guard_id
            most_minutes['minutes'] = total_minutes
    most_minutes['minute'] = get_most_common_sleepy_minute(
        timecards[most_minutes['id']]
    )
    return int(most_minutes['id']) * most_minutes['minute']


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
