import os

INPUT_FILE = "day_two.txt"

WIN = 6
DRAW = 3
LOSE = 0

ROCK_LST = ["A", "X"]
PAPER_LST = ["B", "Y"]
SCISSORS_LST = ["C", "Z"]

ROCK = ROCK_LST[0]
PAPER = PAPER_LST[0]
SCISSORS = SCISSORS_LST[0]

shapes = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

scores = {
    "X": {  # you need to lose
        ROCK: SCISSORS,
        PAPER: ROCK,
        SCISSORS: PAPER,
    },
    "Y": {  # you need to draw
        ROCK: ROCK,
        PAPER: PAPER,
        SCISSORS: SCISSORS
    },
    "Z": {  # you need to win
        ROCK: PAPER,
        PAPER: SCISSORS,
        SCISSORS: ROCK
    }
}


def round_result(player1, player2):
    if player1 == ROCK:
        if player2 == SCISSORS:
            return LOSE
        if player2 == PAPER:
            return WIN

    if player1 == SCISSORS:
        if player2 == PAPER:
            return LOSE
        if player2 == ROCK:
            return WIN

    if player1 == PAPER:
        if player2 == ROCK:
            return LOSE
        if player2 == SCISSORS:
            return WIN

    return DRAW


def normalize(s: str) -> str:
    if s in ROCK_LST:
        return ROCK
    if s in SCISSORS_LST:
        return SCISSORS
    return PAPER


def solve_part_one(input_file):
    score = 0
    for line in input_file:
        elf, me = line.strip().split(" ")
        me = normalize(me)
        score += shapes[me] + round_result(elf, me)
    return score


def solve_part_two(input_file):
    score = 0
    for line in input_file:
        elf, me = line.strip().split(" ")
        me = scores[me][elf]
        score += shapes[me] + round_result(elf, me)
    return score


if __name__ == '__main__':
    dir_path = os.getcwd()
    fd = open(f"{dir_path}/inputs/{INPUT_FILE}")

    # print(solve_part_one(fd))
    print(solve_part_two(fd))
