import math

def map_line(line : str) -> list[tuple[int, int]]:
    result = []
    nesting = 0
    for c in line:
        if c == "[":
            nesting +=1
        elif c == "]":
            nesting -=1
        elif c != ",":
            result.append((nesting, int(c)))
    
    return result

with open("aoc/2021/d18.input") as file:
    lines = file.readlines()

    pairs = [map_line(line.strip()) for line in lines]


def reduce(pair : list[tuple[int, int]]):
    reducing = True
    while reducing:
        reducing = False
        for index, num in enumerate(pair):
            if num[0] > 4 and index + 1 < len(pair) and num[0] == pair[index + 1][0]:
                # explode with next
                previous_index = index - 1
                next_index = index + 2
                if previous_index >= 0:
                    pair[previous_index] = (pair[previous_index][0], pair[previous_index][1] + num[1])
                if next_index < len(pair):
                    pair[next_index] = (pair[next_index][0], pair[next_index][1] + pair[index + 1][1])
                pair.pop(index + 1)
                pair.pop(index)
                pair.insert(index, (num[0] - 1, 0))
                reducing = True
                break
        
        if reducing == False:
            for index, num in enumerate(pair):
                if num[1] > 9:
                    # split
                    pair.pop(index)
                    pair.insert(index, (num[0] + 1, math.floor(num[1]/2)))
                    pair.insert(index + 1, (num[0] + 1, math.ceil(num[1]/2)))
                    reducing = True
                    break
    return pair
def add_pairs(pair_1 : list[tuple[int, int]], pair_2 : list[tuple[int, int]]):
    sum = []
    for element in pair_1:
        sum.append((element[0] + 1, element[1]))
    for element in pair_2:
        sum.append((element[0] + 1, element[1]))

    return reduce(sum)

def get_magnitude(pair : list[tuple[int, int]]):
    computing = True
    while computing:
        computing = False
        if len(pair) == 1:
            return pair[0][1]
        for index, element in enumerate(pair):
            if element[0] == pair[index + 1][0]:
                pair[index] = (element[0] - 1, 3 * element[1] + 2 * pair[index + 1][1])
                pair.pop(index + 1)
                computing = True
                break

def part1(pairs : list[list[tuple[int, int]]]) -> int:
    result = pairs[0]
    for i in range(1, len(pairs)):
        result = add_pairs(result, pairs[i])

    return get_magnitude(result)

def part2(pairs : list[list[tuple[int, int]]]) -> int:
    max_magnitude = 0
    for i1, pair1 in enumerate(pairs):
        for i2, pair2 in enumerate(pairs):
            if i1 != i2:
                magnitude = get_magnitude(add_pairs(pair1, pair2))
                if magnitude > max_magnitude:
                    max_magnitude = magnitude
    return max_magnitude

print(part1(pairs))
print(part2(pairs))