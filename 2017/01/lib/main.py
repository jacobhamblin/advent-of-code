import sys

def num_matches(str):
    if not str:
        return 0
    if len(str) == 1:
        return 1
    matches = 0
    last_char = str[len(str) - 1]
    for char in str:
        if (char == last_char):
            matches += 1
        last_char = char
    return matches


def main():
    if len(sys.argv) < 2:
        print('missing str argument')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('too many arguments')
        sys.exit(1)

    print(num_matches(sys.argv[1]))
    sys.exit(0)


if __name__ == "__main__":
    main()
