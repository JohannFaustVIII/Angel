import math


with open("aoc/2021/d14.input") as file:
    lines = file.readlines()

    polymers = {}
    changes = {}

    for i in range(len(lines[0].strip())):
        polymer = lines[0].strip()[i:i+2]
        if len(polymer) == 2:
            if polymer not in polymers:
                polymers[polymer] = 1
            else:
                polymers[polymer] += 1

    changes = {parts[0].strip() : parts[1].strip() for parts in [line.strip().split("->") for line in lines[2:]]}

def part1(polymers : dict, changes: dict, iterations: int) -> int:

    for _ in range(iterations):
        new_polymers = {}
        for key, value in polymers.items():
            change = changes[key]
            polymer_1 = key[0] + change
            polymer_2 = change + key[1]

            if polymer_1 not in new_polymers:
                new_polymers[polymer_1] = value
            else:
                new_polymers[polymer_1] += value

            if polymer_2 not in new_polymers:
                new_polymers[polymer_2] = value
            else:
                new_polymers[polymer_2] += value

        polymers = new_polymers

    letters = {}

    for key, value in polymers.items():
        for k in key:
            if k not in letters:
                letters[k] = value
            else:
                letters[k] += value
    
    for key in letters.keys():
        letters[key] = math.ceil(letters[key]/2)

    min = -1
    max = -1

    for key, value in letters.items():
        if min == -1:
            min = value
        if max == -1:
            max = value
        
        if value < min:
            min = value
        if value > max:
            max = value

    return max - min
    
print(part1(polymers, changes, 10))
print(part1(polymers, changes, 40))