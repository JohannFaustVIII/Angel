with open("aoc/2021/d7.input") as file:
    line = file.readline()

    positions = list(map(lambda x: int(x), line.strip().split(",")))

def finder(positions : list[int], formula) -> int:
    return min([sum([formula(i, position) for position in positions]) for i in range(max(positions)+1)])

def part1_formula(position : int, target : int) -> int:
    return abs(target-position)

def part2_formula(position : int, target : int) -> int:
    count = abs(target-position)
    return int((1 + count) * count / 2)

print(finder(positions,part1_formula))
print(finder(positions,part2_formula))
