with open("aoc/2022/d24.input") as file:
    lines = file.readlines()

    height = len(lines) - 2
    length = len(lines[0].strip()) - 2

    start = (-1, 0) # y,x
    end = (height, length - 1)

    winds = []

    for _ in range(height):
        line = []
        for _ in range(length):
            line.append([])
        winds.append(line)
    
    for y, line in enumerate(lines[1:-1]):
        for x, p in enumerate(line.strip()[1:-1]):
            if p == ">":
                for i in range(length):
                    winds[y][i].append((length, (length - x + i) % length))
            elif p == "<":
                for i in range(length):
                    winds[y][i].append((length, (length + x - i) % length))
            elif p == "v":
                for i in range(height):
                    winds[i][x].append((height, (height - y + i) % height))
            elif p == "^":
                for i in range(height):
                    winds[i][x].append((height, (height + y - i) % height))

def get_next_safe_locations(winds: list[list[tuple[int, int]]], height : int, length : int, start : tuple[int, int], end : tuple[int, int], position : tuple[int, int], rounds : int) -> list[tuple[int, int]]:
    move_vectors = (
        (0, 0),
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    )

    safe_positions = []
    for vector in move_vectors:
        y = position[0] + vector[0]
        x = position[1] + vector[1]
        next = (y, x)
        if next == start or next == end:
            safe_positions.append(next)
        elif 0 <= y < height and 0 <= x < length:
            # print("In", winds[y][x], len(winds[y][x]), y, x, rounds)
            can_next = True
            for wind in winds[y][x]:
                if rounds % wind[0] == wind[1]:
                    can_next = False
            if can_next:
                safe_positions.append(next)
    return safe_positions

def part_1(winds: list[list[tuple[int, int]]], height : int, length : int, start : tuple[int, int], end : tuple[int, int], rounds : int = 0):

    safe_positions = {start}

    while True:
        rounds += 1
        next_positions = set()


        for position in safe_positions:
            next_positions.update(get_next_safe_locations(winds, height, length, start, end, position, rounds))

        if end in next_positions:
            return rounds

        safe_positions = next_positions

def part_2(winds: list[list[tuple[int, int]]], height : int, length : int, start : tuple[int, int], end : tuple[int, int], rounds : int = 0) -> int:
    first_trip = part_1(winds, height, length, start, end)
    back_trip = part_1(winds, height, length, end, start, first_trip)
    second_trip = part_1(winds, height, length, start, end, back_trip)

    return second_trip

print(part_1(winds, height, length, start, end))
print(part_2(winds, height, length, start, end))