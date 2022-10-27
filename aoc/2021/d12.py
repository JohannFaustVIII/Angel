from curses.ascii import islower


with open("aoc/2021/d12.input") as file:
    lines = file.readlines()
    roads = {}
    for line in lines:
        caves = line.strip().split("-")
        if caves[0] not in roads:
            roads[caves[0]] = []
        if caves[1] not in roads:
            roads[caves[1]] = []

        roads[caves[0]].append(caves[1])
        roads[caves[1]].append(caves[0])

print(roads)

def part1(roads: dict, limit: int) -> int:
    visits = {key: 0 for key in roads.keys()}

    def go_next(roads: dict, current_cave: str):
        if current_cave == "end":
            return 1
        if current_cave.islower() and visits[current_cave] == limit:
            return 0
        
        visits[current_cave] += 1

        paths = 0

        for next in roads[current_cave]:
            if next != "start":
                paths += go_next(roads, next)

        visits[current_cave] -=1

        return paths
        
    return go_next(roads, "start")

def part2(roads: dict) -> int:
    visits = {key: 0 for key in roads.keys()}

    def go_next(roads: dict, current_cave: str, double_visit: bool):
        if current_cave == "end":
            return 1
        if current_cave.islower() and visits[current_cave] > 0:
            if double_visit:
                return 0
            else:
                double_visit = True
        
        visits[current_cave] += 1

        paths = 0

        for next in roads[current_cave]:
            if next != "start":
                paths += go_next(roads, next, double_visit)

        visits[current_cave] -=1

        return paths
        
    return go_next(roads, "start", False)

print(part1(roads, 1))
print(part2(roads))