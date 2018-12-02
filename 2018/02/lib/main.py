import itertools
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


def common_characters(first_string, second_string):
    common_chars = ''
    count = 0
    for index, char in enumerate(first_string):
        if (char == second_string[index]):
            count += 1
            common_chars += char
    return [count, common_chars]


def common_characters_best_match(array_of_ids):
    str_of_highest_parity = ''
    peak_parities = {}
    default = [-1, '']
    for first_string, second_string in itertools.combinations(array_of_ids, 2):
        [count, common_chars] = common_characters(first_string, second_string)
        existing_record_first = peak_parities.get(first_string, default)
        existing_record_second = peak_parities.get(second_string, default)
        if count > existing_record_first[0]:
            peak_parities[first_string] = [count, common_chars]
        if count > existing_record_second[0]:
            peak_parities[second_string] = [count, common_chars]
        if count > peak_parities.get(str_of_highest_parity, default)[0]:
            str_of_highest_parity = first_string
    return peak_parities.get(str_of_highest_parity)[1]


def get_common_characters_of_best_match(array_of_ids):
    common_characters_list
    

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
    print(common_characters_best_match(contents_list))
    sys.exit(0)


if __name__ == "__main__":
    main()
