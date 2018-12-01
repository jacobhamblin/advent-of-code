import sys


def frequency_steps(list_changes, initial = 0):
    list_changes = [int(str_num) for str_num in list_changes]
    return initial + sum(list_changes)


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
    f.close()
    print(frequency_steps(contents_list))
    sys.exit(0)


if __name__ == "__main__":
    main()
