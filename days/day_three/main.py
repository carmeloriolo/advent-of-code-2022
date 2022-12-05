import os

INPUT_FILE = "day_three.txt"


def calculate_overlapping_priorities(first, second):
    arr = [0] * 128
    for s in first:
        a = ord(s)
        arr[a] += 1
    for s in second:
        a = ord(s)
        if arr[a] > 0:
            return a - 96 if a > 96 else a - 38

    return 0


def solve_part_one(input_file):
    priorities_sum = 0
    for line in input_file:
        rucksack = line.strip()
        num_of_items = len(rucksack)
        size_of_compartment = int(num_of_items / 2)
        first_compartment = rucksack[:size_of_compartment]
        second_compartment = rucksack[size_of_compartment:]
        priorities_sum += calculate_overlapping_priorities(first_compartment, second_compartment)

    return priorities_sum


def solve_part_two(input_file):
    pass


if __name__ == '__main__':
    dir_path = os.getcwd()
    fd = open(f"{dir_path}/inputs/{INPUT_FILE}")

    print(solve_part_one(fd))
    # print(solve_part_two(fd))
