with open("aoc/2021/d15.input") as file:
    lines = file.readlines()

    points = [[int(s) for s in line.strip()] for line in lines]

def compute_path(points: list[list[int]]) -> int:
    width = len(points[0])
    height = len(points)
    move_vectors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    point = (0, 0)
    risk = 0
    min_risks = {}

    to_visit = []

    while (width - 1, height - 1) not in min_risks:
        if point not in min_risks:
            min_risks[point] = risk

            for vector in move_vectors:
                x = point[0] + vector[0]
                y = point[1] + vector[1]

                if 0 <= x < width and 0 <= y < height:
                    if (x,y) not in min_risks:
                        to_visit.append((x, y, risk + points[y][x]))
        
        to_visit = sorted(to_visit, key = lambda x : x[2])

        next_to_visit = to_visit[0]
        to_visit.pop(0)
        point = (next_to_visit[0], next_to_visit[1])
        risk = next_to_visit[2]

    return min_risks[(width - 1, height - 1)]

def make_bigger_map(points: list[list[int]]) -> list[list[int]]:
    result = [[0 for i in range(len(points[0]) * 5)] for j in range(len(points) * 5)]
    for y in range(5):
        for x in range(5):
            for p_y, line in enumerate(points):
                for p_x, point in enumerate(line):
                    actual_y = p_y + y * len(points)
                    actual_x = p_x + x * len(points[0])
                    risk = point + x + y
                    risk = risk if risk <= 9 else risk - 9
                    result[actual_y][actual_x] = risk
    return result

print(compute_path(points))
print(compute_path(make_bigger_map(points)))