with open("aoc/2022/d14.input") as file:
    lines = file.readlines()

    rocks = set()

    for line in lines:

        previous = None
        actual = None

        steps = line.strip().split("->")

        for step in steps:
            actual = step.strip().split(",")
            actual = (int(actual[0]), int(actual[1]))

            if previous and actual:
                for x in range(min(previous[0], actual[0]), max(previous[0], actual[0]) + 1):
                    for y in range(min(previous[1], actual[1]), max(previous[1], actual[1]) + 1):
                        rocks.add((x,y))
            previous = actual

def next_cord(sand : tuple[int, int], rocks : set[tuple[int, int]], sands : set[tuple[int, int]]):
    down = (sand[0], sand[1] + 1)
    if down not in rocks and down not in sands:
        return True, down
    left = (sand[0] - 1, sand[1] + 1)
    if left not in rocks and left not in sands:
        return True, left
    right = (sand[0] + 1, sand[1] + 1)
    if right not in rocks and right not in sands:
        return True, right
    return False, None

def part_1(rocks: set[tuple[int, int]]) -> int:

    count = 0
    sands = set()
    max_depth = max([rock[1] for rock in rocks])

    while True:
        new_sand = (500, 0)
        if new_sand in sands:
            return count
        while True:
            can_next, next = next_cord(new_sand, rocks, sands)
            if can_next:
                new_sand = next
                if new_sand[1] > max_depth:
                    return count
            else:
                break
        count += 1
        sands.add(new_sand)
    return count

def next_cord_2(sand : tuple[int, int], rocks : set[tuple[int, int]], sands : set[tuple[int, int]], max_depth : int):
    floor = max_depth + 2
    if sand[1] == floor - 1:
        return False, None
    down = (sand[0], sand[1] + 1)
    if down not in rocks and down not in sands and down[1]:
        return True, down
    left = (sand[0] - 1, sand[1] + 1)
    if left not in rocks and left not in sands:
        return True, left
    right = (sand[0] + 1, sand[1] + 1)
    if right not in rocks and right not in sands:
        return True, right
    return False, None

def part_2(rocks: set[tuple[int, int]]) -> int:

    count = 0
    sands = set()
    max_depth = max([rock[1] for rock in rocks])

    while True:
        new_sand = (500, 0)
        if new_sand in sands:
            return count
        while True:
            can_next, next = next_cord_2(new_sand, rocks, sands, max_depth)
            if can_next:
                new_sand = next
            else:
                break
        count += 1
        sands.add(new_sand)
    return count

print(part_1(rocks))
print(part_2(rocks))