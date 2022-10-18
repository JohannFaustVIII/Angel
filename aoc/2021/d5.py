def part1(vents: list[tuple[tuple[int], tuple[int]]]) -> int:
    points = {}

    for vent in vents:
        start_x, start_y = vent[0]
        end_x, end_y = vent[1]

        delta_x = end_x - start_x
        delta_y = end_y - start_y

        if delta_x == 0:
            for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
                x, y = start_x, i
                if (x, y) not in points:
                    points[(x, y)] = 0
                points[(x, y)] += 1
            continue

        if delta_y == 0:
            for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
                x, y = i, start_y
                if (x, y) not in points:
                    points[(x, y)] = 0
                points[(x, y)] += 1
            continue
    
    points = {k : v for k, v in points.items() if v > 1}

    return len(points)

def part2(vents: list[tuple[tuple[int], tuple[int]]]) -> int:
    points = {}

    for vent in vents:
        start_x, start_y = vent[0]
        end_x, end_y = vent[1]

        delta_x = end_x - start_x
        delta_y = end_y - start_y

        if delta_x == 0:
            for i in range(min(start_y, end_y), max(start_y, end_y) + 1):
                x, y = start_x, i
                if (x, y) not in points:
                    points[(x, y)] = 0
                points[(x, y)] += 1
            continue

        if delta_y == 0:
            for i in range(min(start_x, end_x), max(start_x, end_x) + 1):
                x, y = i, start_y
                if (x, y) not in points:
                    points[(x, y)] = 0
                points[(x, y)] += 1
            continue

        if abs(delta_x) == abs(delta_y):
            vent_range = abs(delta_x)
            d_x = int(delta_x/vent_range)
            d_y = int(delta_y/vent_range)
            for i in range(vent_range + 1):
                x, y = start_x + i * d_x, start_y + i * d_y
                if (x, y) not in points:
                    points[(x, y)] = 0
                points[(x, y)] += 1
            continue
    
    points = {k : v for k, v in points.items() if v > 1}

    return len(points)
    

with open("aoc/2021/d5.input") as file:
    lines = file.readlines()
    vents = []

    for line in lines:
        coords = line.strip().split("->")
        start = tuple(map(lambda x : int(x), coords[0].strip().split(",")))
        end = tuple(map(lambda x : int(x), coords[1].strip().split(",")))

        vents.append((start, end))

print(part1(vents))
print(part2(vents))