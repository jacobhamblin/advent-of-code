import sys


def has_pair_and_triplet(str):
    chars_seen = {}
    double_present = 0
    triple_present = 0
    for char in str:
        existing_presence = chars_seen.get(char, 0)
        chars_seen[char] = existing_presence + 1
    for key in chars_seen:
        if chars_seen[key] == 2 and not double_present:
            double_present = 1
        if chars_seen[key] == 3 and not triple_present:
            triple_present = 1
    return [double_present, triple_present]


def checksum(array_of_ids):
    pairs = 0
    triplets = 0
    for id_string in array_of_ids:
        [pair, triplet] = has_pair_and_triplet(id_string)
        pairs += pair
        triplets += triplet
    return pairs * triplets
    

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
    #  print(func(contents_list))
    sys.exit(0)


if __name__ == "__main__":
    main()
