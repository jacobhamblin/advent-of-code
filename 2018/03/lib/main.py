import sys
import re


def overlapping_square_count(coords_lists):
    squares = {}
    for [id, left, top, width, height] in coords_lists:
        for x in xrange(left, left + width):
            for y in xrange(top, top + height):
                square = squares.get((x, y), [])
                square.append(id)
                squares[(x, y)] = square
    return len([
        square for square in squares
        if len(squares[square]) > 1
    ])



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
    reg = re.compile('[0-9]')
    claims = map(lambda str: re.findall(r'-?\d+', str), contents_list)
    for index, claim in enumerate(claims):
        claims[index] = map(lambda str: int(str), claim)
    print(overlapping_square_count(claims))
    sys.exit(0)


if __name__ == "__main__":
    main()
