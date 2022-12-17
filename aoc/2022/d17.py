from math import floor

with open("aoc/2022/d17.input") as file:
    line = file.readline()

    moves = [-1 if c == "<" else 1 for c in line.strip()]

def part_1(moves : list[int]):
    spawn_rocks = (((-1, 0), (0, 0), (1, 0), (2, 0)), ((0, 0), (-1, 1), (0, 1), (1, 1), (0, 2)), ((-1, 0), (0, 0), (1, 0), (1, 1), (1, 2)), ((-1, 0), (-1, 1), (-1, 2), (-1, 3)), ((-1, 0), (0, 0), (-1, 1), (0, 1)))
    TURNS = 2022
    static_rocks = set()

    max_heights = [0 for _ in range(7)]
    max_height = 0
    move = 0

    for turn in range(TURNS):
        spawn = spawn_rocks[turn % len(spawn_rocks)]
        rock = [[s[0] + 3, s[1] + max_height + 4] for s in spawn]

        while True:
            rock_move = moves[move % len(moves)]
            move += 1

            moved = [[r[0] + rock_move, r[1]] for r in rock]

            if all([r[0] >= 0 and r[0] < 7 and (r[0], r[1]) not in static_rocks for r in moved]):
                rock = moved

            down = [[r[0], r[1] - 1] for r in rock]

            if any([r[1] == 0 or (r[0], r[1]) in static_rocks for r in down]):
                for r in rock:
                    if r[1] > max_heights[r[0]]:
                        max_heights[r[0]] = r[1]
                    static_rocks.add((r[0], r[1]))
                break
            else:
                rock = down
        max_height = max(max_heights)

    return max_height

def part_2(moves : list[int]):
    spawn_rocks = (((-1, 0), (0, 0), (1, 0), (2, 0)), ((0, 0), (-1, 1), (0, 1), (1, 1), (0, 2)), ((-1, 0), (0, 0), (1, 0), (1, 1), (1, 2)), ((-1, 0), (-1, 1), (-1, 2), (-1, 3)), ((-1, 0), (0, 0), (-1, 1), (0, 1)))
    TURNS = 1000000000000
    static_rocks = set()

    max_heights = [0 for _ in range(7)]
    max_height = 0
    move = 0

    height_by_turn = {}
    states = {}

    for turn in range(TURNS):
        spawn = spawn_rocks[turn % len(spawn_rocks)]
        rock = [[s[0] + 3, s[1] + max_height + 4] for s in spawn]

        while True:
            rock_move = moves[move % len(moves)]
            move += 1

            moved = [[r[0] + rock_move, r[1]] for r in rock]

            if all([r[0] >= 0 and r[0] < 7 and (r[0], r[1]) not in static_rocks for r in moved]):
                rock = moved

            down = [[r[0], r[1] - 1] for r in rock]

            if any([r[1] == 0 or (r[0], r[1]) in static_rocks for r in down]):
                for r in rock:
                    if r[1] > max_heights[r[0]]:
                        max_heights[r[0]] = r[1]
                    static_rocks.add((r[0], r[1]))
                break
            else:
                rock = down
        max_height = max(max_heights)
        height_by_turn[turn] = max_height
        next_rock = turn % len(spawn_rocks)
        next_move = move % len(moves)
        turn_top = tuple([val - min(max_heights) for val in max_heights])

        key = (turn_top, next_rock, next_move)

        if key not in states.keys():
            states[key] = turn
        else:
            previous_turn = states[key]

            diff = turn - previous_turn
            
            rounds = floor((TURNS - previous_turn) / diff)

            ahead = (TURNS - previous_turn) - diff * rounds

            return height_by_turn[previous_turn] + rounds * (height_by_turn[turn] - height_by_turn[previous_turn]) + (height_by_turn[previous_turn + ahead - 1] - height_by_turn[previous_turn])

    return max_height


print(f"Part 1 = {part_1(moves)}")
print(f"Part 2 = {part_2(moves)}")
