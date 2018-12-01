import sys

def num_matches(str):
    if not str:
        return 0
    return 1

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
