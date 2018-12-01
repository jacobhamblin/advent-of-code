import sys


def sum_matches(str, halfway = False):
    if not str:
        return 0
    matches = []
    step = 1
    if halfway:
        step = len(str) / 2
    for index, char in enumerate(str):
        if char == str[(index + step) % len(str)]:
            matches.append(int(char))
    return sum(matches)


def main():
    if len(sys.argv) < 2:
        print('missing input file')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('too many arguments')
        sys.exit(1)

    f = open(sys.argv[1],"r")
    contents = f.read().strip()
    f.close()
    print(sum_matches(contents, True))
    sys.exit(0)


if __name__ == "__main__":
    main()
