with open("aoc/2022/d18.input") as file:
    lines = file.readlines()

    cubes = set()

    for line in lines:
        x, y, z = [int(v) for v in line.strip().split(",")]
        cubes.add((x, y, z))


def part_1(cubes : set[tuple[int, int, int]]) -> int:
    vectors = (
        (-1, 0 , 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1)
    )
    around = []

    for cube in cubes:
        for vector in vectors:
            x = cube[0] + vector[0]
            y = cube[1] + vector[1]
            z = cube[2] + vector[2]

            free_cube = (x, y, z)
            if free_cube not in cubes:
                around.append(free_cube)

    return len(around)

def part_2(cubes : set[tuple[int, int, int]]) -> int:
    vectors = (
        (-1, 0 , 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1)
    )
    sides = 0
    visited = set()
    min_x = min([c[0] for c in cubes]) - 1
    min_y = min([c[1] for c in cubes]) - 1
    min_z = min([c[2] for c in cubes]) - 1
    max_x = max([c[0] for c in cubes]) + 1
    max_y = max([c[1] for c in cubes]) + 1
    max_z = max([c[2] for c in cubes]) + 1

    to_visit = {(min_x,min_y,min_z)}

    while to_visit:
        cube = to_visit.pop()
        visited.add(cube)

        for vector in vectors:
            x = cube[0] + vector[0]
            y = cube[1] + vector[1]
            z = cube[2] + vector[2]

            next_cube = (x, y, z)
            if next_cube in cubes:
                sides += 1
            else:
                if next_cube not in visited:
                    if min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z:
                        to_visit.add(next_cube)

    return sides

print(part_1(cubes))
print(part_2(cubes))