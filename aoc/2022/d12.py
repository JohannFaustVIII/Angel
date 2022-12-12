with open("aoc/2022/d12.input") as file:
    lines = file.readlines()

    map = []

    start = None
    end = None

    for index_y, line in enumerate(lines):
        row = []

        for index_x, c in enumerate([c for c in line.strip()]):
            if c == "S":
                row.append(1)
                start = (index_y, index_x)
            elif c == "E":
                row.append(ord("z") - ord("a") + 1)
                end = (index_y, index_x)
            else:
                row.append(ord(c) - ord("a") + 1)
        map.append(row)

def compute_path(map: list[list[int]], start : tuple[int, int], end : tuple[int, int]) -> int:
    width = len(map[0])
    height = len(map)
    move_vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_path = {}
    point = start
    length = 0

    to_visit = []

    while end not in min_path:
        if point not in min_path:
            min_path[point] = length

            for vector in move_vectors:
                y = point[0] + vector[0]
                x = point[1] + vector[1]
                if 0 <= x < width and 0 <= y < height:
                    if (y,x) not in min_path:
                        if map[y][x] - map[point[0]][point[1]] <= 1:
                            to_visit.append((y,x, length + 1))

        if len(to_visit) == 0:
            if end not in min_path:
                return width * height
            return min_path[end]
        to_visit = sorted(to_visit, key = lambda x : x[2])
        next_to_visit = to_visit[0]
        to_visit.pop(0)
        point = (next_to_visit[0], next_to_visit[1])
        length = next_to_visit[2]
    return min_path[end]

def part_2(map: list[list[int]], end : tuple[int, int]) -> int:
    steps = []

    for index_y, line in enumerate(map):
        for index_x, v in enumerate(line):
            if v == 1:
                # can be replaced by reverse checking, so compute path from "E" to any "a", and then find min
                # but that was fast enough
                steps.append(compute_path(map, (index_y, index_x), end))

    steps.sort()
    return steps[0]

print(compute_path(map, start, end))
print(part_2(map, end))