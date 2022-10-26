with open("aoc/2021/d11.input") as file:
    lines = file.readlines()
    octopuses = [[int(c) for c in line.strip()] for line in lines]

print(octopuses)

def part1(octopuses : list[list[int]]) -> int:
    octopuses_state = [[[octopus, 0] for octopus in octopuses_state] for octopuses_state in octopuses]

    flashes = 0
    vectors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def flash(x, y):
        if octopuses_state[x][y][1] == 1:
            return
        if octopuses_state[x][y][0] > 9:
            octopuses_state[x][y][1] = 1
            for vector in vectors:
                v_x = x + vector[0]
                v_y = y + vector[1]
                if 0 <= v_x < len(octopuses_state) and 0 <= v_y < len(octopuses_state[x]):
                    octopuses_state[v_x][v_y][0] += 1
                    flash(v_x, v_y)

    for i in range(100):

        for x, line in enumerate(octopuses_state):
            for y, value in enumerate(line):
                value[0] += 1
        
        for x, line in enumerate(octopuses_state):
            for y, value in enumerate(line):
                flash(x, y)

        for x, line in enumerate(octopuses_state):
            for y, value in enumerate(line):
                if value[1] == 1:
                    value[1] = 0
                    value[0] = 0
                    flashes += 1
        
    return flashes


def part2(octopuses : list[list[int]]) -> int:
    octopuses_state = [[[octopus, 0] for octopus in octopuses_state] for octopuses_state in octopuses]

    flashes = 0
    day = 0
    vectors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def flash(x, y):
        if octopuses_state[x][y][1] == 1:
            return
        if octopuses_state[x][y][0] > 9:
            octopuses_state[x][y][1] = 1
            for vector in vectors:
                v_x = x + vector[0]
                v_y = y + vector[1]
                if 0 <= v_x < len(octopuses_state) and 0 <= v_y < len(octopuses_state[x]):
                    octopuses_state[v_x][v_y][0] += 1
                    flash(v_x, v_y)

    while True:
        day += 1

        for x, line in enumerate(octopuses_state):
            for y, value in enumerate(line):
                value[0] += 1
        
        for x, line in enumerate(octopuses_state):
            for y, value in enumerate(line):
                flash(x, y)

        for x, line in enumerate(octopuses_state):
            for y, value in enumerate(line):
                if value[1] == 1:
                    value[1] = 0
                    value[0] = 0
                    flashes += 1

        if flashes == len(octopuses_state) * len(octopuses_state[0]):
            return day
        
        flashes = 0

print(part1(octopuses))
print(part2(octopuses))