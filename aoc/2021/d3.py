with open("aoc/2021/d3.input") as file:
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]

from collections import Counter
from functools import reduce


def part1(values : list[list[str]]) -> tuple[int, int]:
    gamma = 0
    epsilon = 0

    for i in range(0, len(values[0])):
        bits = list(map(lambda x : x[i], values))
        count = Counter(bits)
        bit = int(count.most_common(1)[0][0])
        gamma = gamma * 2 + bit
        epsilon = epsilon * 2 + (1 - bit)

    return (gamma, epsilon)

solution_part1 = part1(lines)
print(solution_part1[0] * solution_part1[1])


def part2(values : list[list[str]]) -> tuple[int, int]:
    oxygen_list = values
    co2_list = values

    oxygen_index = -1
    while(len(oxygen_list) != 1):
        oxygen_index += 1
        bits = list(map(lambda x : x[oxygen_index], oxygen_list))
        count = Counter(bits)
        occurences = count.most_common()
        bit = occurences[0][0] if occurences[0][1] != occurences[1][1] else '1'
        oxygen_list = list(filter(lambda x : x[oxygen_index] == bit, oxygen_list))

    co2_index = -1
    while(len(co2_list) != 1):
        co2_index += 1
        bits = list(map(lambda x : x[co2_index], co2_list))
        count = Counter(bits)
        occurences = count.most_common()
        bit = occurences[1][0] if occurences[0][1] != occurences[1][1] else '0'
        co2_list = list(filter(lambda x : x[co2_index] == bit, co2_list))

    oxygen = int(reduce(lambda x,y : x + y, oxygen_list[0], ""), 2)
    co2 = int(reduce(lambda x,y : x + y, co2_list[0], ""), 2)

    return oxygen, co2

solution_part2 = part2(lines)
print(solution_part2)
print(solution_part2[0] * solution_part2[1])

    
