import os

INPUT_FILE = "day_one.txt"


def solve_part_one(input_file):
    max_elf_calories = 0
    calories = 0
    for line in input_file:
        s = line.strip()
        if s != "":
            calories += int(line.strip())
            continue
        max_elf_calories = max(max_elf_calories, calories)
        calories = 0

    return max_elf_calories


def solve_part_two(input_file):
    first = 0
    second = float('-inf')
    third = float('-inf')
    calories = 0
    for line in input_file:
        s = line.strip()
        if s != "":
            calories += int(line.strip())
            continue
        if calories > first:
            third = second
            second = first
            first = calories
        elif calories > second:
            third = second
            second = calories
        elif calories > third:
            third = calories
        calories = 0

    return first + second + third


if __name__ == '__main__':
    dir_path = os.getcwd()
    fd = open(f"{dir_path}/../inputs/{INPUT_FILE}")

    # print(solve_part_one(fd))
    print(solve_part_two(fd))
