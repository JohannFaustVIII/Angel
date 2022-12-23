with open("aoc/2022/d23.input") as file:
    lines = file.readlines()

    elves = []

    for index_y, line in enumerate(lines):
        for index_x, p in enumerate(line):
            if p == "#":
                elves.append((index_y, index_x))

print(elves)

def part_1(elves : list[tuple[int, int]]) -> int:
    
    TURNS = 10

    around = (
        (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
    )

    vectors = [
        (((-1, -1), (-1, 0), (-1, 1)), (-1, 0)),
        (((1, -1), (1, 0), (1, 1)), (1, 0)),
        (((-1, -1), (0, -1), (1, -1)), (0, -1)),
        (((-1, 1), (0, 1), (1, 1)), (0, 1))
    ]

    for i in range(TURNS):
        propositions = {}

        for elf in elves:
            if all([(elf[0] + a[0], elf[1] + a[1]) not in elves for a in around]):
                continue
            else:
                for vecs, next in vectors:
                    if all([(elf[0] + vec[0], elf[1] + vec[1]) not in elves for vec in vecs]):
                        next_position = (elf[0] + next[0], elf[1] + next[1])
                        if next_position not in propositions.keys():
                            propositions[next_position] = []
                        propositions[next_position].append(elf)
                        break
        
        next_elves = set(elves)

        for prop, elves in propositions.items():
            if len(elves) != 1:
                continue
            next_elves.remove(elves[0])
            next_elves.add(prop)


        elves = next_elves
        vectors.append(vectors.pop(0))

    ys = [elf[0] for elf in elves]
    xs = [elf[1] for elf in elves]

    max_y = max(ys)
    min_y = min(ys)
    max_x = max(xs)
    min_x = min(xs)

    return (max_y - min_y + 1) * (max_x - min_x + 1) - len(elves)

def part_2(elves : list[tuple[int, int]]) -> int:
    
    around = (
        (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
    )

    vectors = [
        (((-1, -1), (-1, 0), (-1, 1)), (-1, 0)),
        (((1, -1), (1, 0), (1, 1)), (1, 0)),
        (((-1, -1), (0, -1), (1, -1)), (0, -1)),
        (((-1, 1), (0, 1), (1, 1)), (0, 1))
    ]

    round = 0
    while True:
        round += 1

        propositions = {}

        for elf in elves:
            if all([(elf[0] + a[0], elf[1] + a[1]) not in elves for a in around]):
                continue
            else:
                for vecs, next in vectors:
                    if all([(elf[0] + vec[0], elf[1] + vec[1]) not in elves for vec in vecs]):
                        next_position = (elf[0] + next[0], elf[1] + next[1])
                        if next_position not in propositions.keys():
                            propositions[next_position] = []
                        propositions[next_position].append(elf)
                        break
        
        next_elves = set(elves)

        for prop, elves in propositions.items():
            if len(elves) != 1:
                continue
            next_elves.remove(elves[0])
            next_elves.add(prop)

        if len(propositions) == 0:
            return round

        elves = next_elves
        vectors.append(vectors.pop(0))                 

print(part_1(elves))
print(part_2(elves))
