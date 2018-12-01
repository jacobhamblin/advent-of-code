import sys

def sum_matches(str):
    if not str:
        return 0
    matches = []
    last_char = str[len(str) - 1]
    for char in str:
        if (char == last_char):
            matches.append(int(char))
        last_char = char
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
    print(sum_matches(contents))
    sys.exit(0)


if __name__ == "__main__":
    main()
