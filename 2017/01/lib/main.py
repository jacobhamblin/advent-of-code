import sys

def num_matches(str):
    if not str:
        return 0
    matches = 0
    last_char = str[len(str) - 1]
    for char in str:
        if (char == last_char):
            matches += 1
        last_char = char
    return matches


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
    print(num_matches(contents))
    sys.exit(0)


if __name__ == "__main__":
    main()
