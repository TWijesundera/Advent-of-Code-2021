from helpers.advent_input import AdventInput, Parser
from collections import Counter

from typing import List

def part1(input):
    bit_count = {}

    while line := next(input.next_line()):
        for pos, bit in enumerate(line.strip()):
            if bit_count.get(pos, None):
                counter = bit_count[pos]
                counter.update(bit)
            else:
                bit_count[pos] = Counter(bit)

    gamma = [bit.most_common(1)[0][0] for pos, bit in bit_count.items()]
    epsilon = ["0" if bit == "1" else "1" for bit in gamma]

    sol = int("".join(gamma), base=2) * int("".join(epsilon), base=2)
    print(f"Part 1 solution is: {sol}")


def part2(input):
    input_lines = input.all_lines()
    oxygen = "".join(filter_bits(input_lines, most_common_value))
    carbon = "".join(filter_bits(input_lines, least_common_value))
    print(f"Part 2 solution is: {int(oxygen, base=2) * int(carbon, base=2)}")

def most_common_value(count: Counter):
    if count.get("1") == count.get("0"):
        return "1"
    return count.most_common(1)[0][0]

def least_common_value(count: Counter):
    if count.get("1") == count.get("0"):
        return "0"
    return count.most_common()[:0:-1][0][0]

def filter_bits(lines: List, criteria, index=0):
    if len(lines) <= 1:
        return lines
    else:
        count = Counter()
        [count.update(line[index]) for line in lines]
        filtered = [line for line in lines if line[index] == criteria(count)]
        return filter_bits(filtered, criteria, index+1)

if __name__ == "__main__":
    parser = Parser()
    args = parser.get_args()
    input = AdventInput(args.input_file)
    part1(input)
    input.reset_input()
    part2(input)
