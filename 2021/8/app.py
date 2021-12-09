# import numpy as np
# import pandas as pd
from pprint import pprint


def load():
    f = open("input")
    input = f.readlines()
    # print(input)
    return input


number_mapping = {
    "012456": 0,
    "25": 1,
    "02346": 2,
    "02356": 3,
    "1235": 4,
    "01356": 5,
    "013456": 6,
    "025": 7,
    "0123456": 8,
    "012356": 9,
}


if __name__ == "__main__":
    # Pseudocode
    # 1. Check length 2 sequence:
    #     -> Know index 2 and 5, but not which is which
    # 2. Check length 3 sequence:
    #     -> What's not ambiguously 2 or 5, is 0
    # 3. Check length 4 sequence:
    #     -> What's not 2 or 5 is 3 or 1 ambiguously
    # 4. Check length 7 sequence:
    #     -> What's not in all other is 4 or 6 ambiguously
    # 5. Check both length 6 sequences:
    #     -> What the differing values are 2 or 4 ambiguously
    #     -> Allows us to then know what 2 is definitively
    # 6.
    position_map = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6}
    count_unique = 0
    input = load()
    total_output = 0
    for line in input:
        clean_line = line.rstrip().split("|")
        known_segments = {
            2: list(),
            3: list(),
            4: list(),
            5: list(),
            6: list(),
            7: list(),
        }
        for i in [2, 3, 4, 5, 6, 7]:
            for seq in clean_line[0].split():
                if len(seq) == i:
                    chars_in_seq = [char for char in seq]
                    chars_in_seq.sort()
                    known_segments[i].append(chars_in_seq)
        pprint(known_segments)

        one_combo = known_segments[2][0]
        print(one_combo)
        # print(known_segments[3][0])
        zero = str()
        for char in known_segments[3][0]:
            if char not in one_combo:
                zero = char
        # print(known_segments[4][0])
        four_combo = [x for x in known_segments[4][0] if x not in one_combo]
        print(four_combo)
        somewhat_known_before_eight = [zero]
        for char in known_segments[4][0]:
            somewhat_known_before_eight.append(char)
        # print(somewhat_known_before_eight)
        eight_combo = [
            x for x in known_segments[7][0] if x not in somewhat_known_before_eight
        ]
        # print(eight_combo)
        # print(known_segments[5])
        len_five_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
        for i in range(3):
            for char in known_segments[5][i]:
                len_five_count[char] += 1

        three = str()
        one = str()
        for char in four_combo:
            if len_five_count[char] == 1:
                one = char
            else:
                three = char
        # pprint(len_five_count)
        six = str()
        four = str()
        for char in eight_combo:
            if len_five_count[char] == 1:
                four = char
            else:
                six = char

        # pprint(known_segments[5])
        len_six_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
        for i in range(3):
            for char in known_segments[6][i]:
                len_six_count[char] += 1
        # print(len_six_count)

        two = str()
        five = str()
        for char in one_combo:
            if len_six_count[char] == 2:
                two = char
            else:
                five = char
        solved_positions = [zero, one, two, three, four, five, six]
        # for position in solved_positions:
        #     print(position)
        # print(solved_positions)
        output = list()
        for seq in clean_line[1].split():
            string_position = list()
            # print(seq)
            for char in seq:
                string_position.append(solved_positions.index(char))
            string_position.sort()
            string_position = [str(x) for x in string_position]
            string_position = "".join(string_position)
            # print(string_position)
            # print(number_mapping[string_position])
            output.append(str(number_mapping[string_position]))
        output = int("".join(output))
        # print(output)
        total_output += output
    print(total_output)
