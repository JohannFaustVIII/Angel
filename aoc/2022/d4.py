with open("aoc/2022/d4.input") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split(",") for line in lines]
    lines = [[pair.split("-") for pair in line] for line in lines]
    lines = [[[int(number) for number in pair] for pair in line] for line in lines]

def fully_contain(pair_1 : list[int], pair_2 : list[int]) -> bool:
    min_value = min(pair_1[0], pair_2[0])
    max_value = max(pair_1[1], pair_2[1])

    if min_value == pair_1[0] and max_value == pair_1[1]:
        return True
    if min_value == pair_2[0] and max_value == pair_2[1]:
        return True
    return False

def overlap(pair_1 : list[int], pair_2 : list[int]) -> bool:
    if pair_1[0] <= pair_2[0] <= pair_1[1]:
        return True
    if pair_2[0] <= pair_1[0] <= pair_2[1]:
        return True
    return False

def part_1(lines : list[list[int]]) -> int:
    counter = 0
    for pairs in lines:
        if fully_contain(pairs[0], pairs[1]):
            print(pairs)
            counter += 1

    return counter

def part_2(lines : list[list[int]]) -> int:
    counter = 0
    for pairs in lines:
        if fully_contain(pairs[0], pairs[1]) or overlap(pairs[0], pairs[1]):
            print(pairs)
            counter += 1

    return counter

print(part_1(lines))
print(part_2(lines))