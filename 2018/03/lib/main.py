import sys
import re


def overlapping_square_count(coords_lists, untouched_claim = False):
    squares = {}
    overlapping = {}
    for [id, left, top, width, height] in coords_lists:
        overlapping[id] = set()
        for x in xrange(left, left + width):
            for y in xrange(top, top + height):
                square = squares.get((x, y), [])
                if square:
                    for coords in squares[(x, y)]:
                        overlapping[coords].add(id)
                        overlapping[id].add(coords)
                square.append(id)
                squares[(x, y)] = square
    if untouched_claim:
        return [id for id in overlapping if not len(overlapping[id])][0]
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
    print(overlapping_square_count(claims, True))
    sys.exit(0)


if __name__ == "__main__":
    main()
