with open("aoc/2021/d2.input") as file:
    lines = file.readlines()
    lines = [line.split(" ") for line in lines]
    commands = [(line[0], int(line[1])) for line in lines]


def part1(commands : list[tuple[str, int]]) -> tuple[int, int]:
    horizontal = 0
    depth = 0

    moves = {
        "forward" : (1, 0),
        "down" : (0, 1),
        "up" : (0, -1)
        }

    for command in commands:
        move = moves[command[0]]
        horizontal += move[0] * command[1]
        depth += move[1] * command[1]

    return horizontal, depth

solution = part1(commands)
print(solution[0] * solution[1])


def part2(commands : list[tuple[str, int]]) -> tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0

    moves = {
        "forward" : (1, 1, 0),
        "down" : (0, 0, 1),
        "up" : (0, 0, -1)
        }

    for command in commands:
        move = moves[command[0]]
        horizontal += move[0] * command[1]
        depth += move[1] * (aim * command[1])
        aim += move[2] * command[1]

    return horizontal, depth

solution = part2(commands)
print(solution[0] * solution[1])