import os

from typing import List

INPUT_FILE = "day_four.txt"


def fully_contained(first, second: List[int]) -> bool:
    min_first, max_first = int(first[0]), int(first[1])
    min_second, max_second = int(second[0]), int(second[1])
    return (min_first <= min_second and max_first >= max_second) \
        or (min_second <= min_first and max_second >= max_first)


def overlaps(first, second: List[int]) -> bool:
    min_first, max_first = int(first[0]), int(first[1])
    min_second, max_second = int(second[0]), int(second[1])
    return min_first <= min_second <= max_first


def solve_part_one(input_file):
    count = 0
    for line in input_file:
        first_segment, second_segment = line.strip().split(",")
        count += 1 if fully_contained(first_segment.split("-"), second_segment.split("-")) else 0
    return count


def solve_part_two(input_file):
    count = 0
    for line in input_file:
        first_segment, second_segment = line.strip().split(",")
        first_pair = first_segment.split("-")
        second_pair = second_segment.split("-")
        partial_overlap = overlaps(first_pair, second_pair) or overlaps(second_pair, first_pair)
        count += 1 if partial_overlap or fully_contained(first_pair, second_pair) else 0

    return count


if __name__ == '__main__':
    dir_path = os.getcwd()
    fd = open(f"{dir_path}/inputs/{INPUT_FILE}")

    # print(solve_part_one(fd))
    print(solve_part_two(fd))
