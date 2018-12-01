import sys


def frequency_steps(list_changes, initial = 0):
    return initial + sum(list_changes)


def first_repeated_frequency(list_changes, initial = 0):
    return list_changes


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
    nums_list = [int(str_num) for str_num in contents_list]
    f.close()
    print(frequency_steps(nums_list))
    sys.exit(0)


if __name__ == "__main__":
    main()
