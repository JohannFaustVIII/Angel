with open("aoc/2022/d2.input") as file:
    lines = file.readlines()

    turns = []

    for line in lines:
        turn = line.strip().split()
        turns.append((turn[0], turn[1]))

def part1(turns : list[tuple[str, str]]) -> int:

    option = {
        "A" : "R",
        "B" : "P",
        "C" : "S",
        "X" : "R",
        "Y" : "P",
        "Z" : "S"
    }

    value = {
        "R" : 1,
        "P" : 2,
        "S" : 3
    }

    beats = {
        "R" : "S",
        "P" : "R",
        "S" : "P"
    }

    points = 0

    for turn in turns:
        enemy_move = option[turn[0]]
        my_move = option[turn[1]]

        points += value[my_move]

        if enemy_move == my_move:
            points += 3
        elif beats[my_move] == enemy_move:
            points += 6

    return points

def part2(turns : list[tuple[str, str]]) -> int:

    option = {
        "A" : "R",
        "B" : "P",
        "C" : "S",
    }

    value = {
        "R" : 1,
        "P" : 2,
        "S" : 3
    }

    win = {
        "R" : "S",
        "P" : "R",
        "S" : "P"
    }

    lose = {
        "R" : "P",
        "P" : "S",
        "S" : "R"
    }

    result_value = {
        "X" : 0,
        "Y" : 3,
        "Z" : 6
    }

    points = 0

    for turn in turns:
        enemy_move = option[turn[0]]
        result = turn[1]
        my_move = win[enemy_move] if result == "X" else enemy_move if result == "Y" else lose[enemy_move]

        points += value[my_move]
        points += result_value[result]

    return points

print(part1(turns))
print(part2(turns))